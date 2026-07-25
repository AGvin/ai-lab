# Resource Lifecycle Orchestration

Use this guide to design and evaluate orchestration for resident models, lazy-loaded models, idle-timeout services, temporary workers, hosted APIs, and billable GPU resources.

## Translations

- English

## Status

Initial canonical operational guidance verified on 2026-07-25. Provider state names, billing semantics, API behavior, quotas, and cleanup guarantees differ; bind every implementation to the exact provider, control plane, resource type, and verification date.

## Core rule

A model worker and the infrastructure that runs it are different control subjects.

A worker can truthfully report that inference or generation completed while:

- the model process remains resident;
- the endpoint remains reachable and billable;
- the GPU pod remains running;
- attached storage, reserved capacity, public IPs, or load balancers remain allocated;
- output still exists only on ephemeral storage;
- the provider has accepted a shutdown request but not completed it.

**A worker reporting completion is not proof that a billable resource stopped.** Resource state and billing state must be verified independently through the authoritative control plane.

## Resource classes

Classify every model or service before scheduling it.

### Always-online and resident

The service process is running and the model remains loaded in RAM or VRAM.

Use when:

- traffic is continuous or latency-sensitive;
- load and warm-up time is material;
- predictable first-response latency justifies idle occupancy;
- enough memory remains for required concurrent services.

Record:

- process and endpoint owner;
- exact loaded artifact and revision;
- minimum reserved RAM and VRAM;
- KV-cache and batching envelope;
- health, readiness, and liveness probes;
- restart and model-reload policy;
- idle cost and maximum accepted residency.

### Always-available but lazy-loaded

The service endpoint or runtime is available, but weights load on first use or after eviction.

Use when:

- the runtime should remain reachable;
- weight residency is too expensive to keep permanently;
- cold-start latency is acceptable or can be hidden by prefetching.

Record cold versus warm behavior separately. A reachable endpoint is not proof that the requested model is loaded and ready.

### Idle-timeout resident

The model remains loaded for a bounded period after the last eligible use, then unloads or scales to zero.

Define:

- which events refresh the idle timer;
- whether queued, streaming, child, retry, and review jobs count as active;
- grace period and drain behavior;
- maximum residency independent of activity;
- whether unload releases only model memory or terminates the billable resource;
- race handling when a new task arrives during drain or termination.

An idle timeout is a cost policy, not a safety guarantee. The orchestrator must still verify the resulting state.

### Task-specific temporary model or service

A local process, container, model, or service is loaded for a bounded task or batch and released afterward.

Use when:

- tasks are infrequent;
- several artifacts must share the same hardware sequentially;
- specialist quality justifies switching overhead;
- the task has a clear terminal artifact and completion gate.

Persist all required state before unload. Do not assume in-process conversation state, cache, or temporary files survive replacement.

### External hosted API

The provider manages model residency, but the orchestrator still manages request, session, file, batch, endpoint, and retention lifecycles exposed to the customer.

Record:

- exact model and endpoint IDs;
- account, project, region, and authentication boundary;
- synchronous, streaming, batch, or asynchronous job semantics;
- uploaded-file, vector-store, session, thread, cache, and output retention;
- request idempotency and duplicate-charge behavior;
- rate limits, quotas, timeouts, and cancellation;
- provider deprecation and version migration policy.

“No local resource” does not mean “no lifecycle.” Hosted files, jobs, caches, sessions, and reserved endpoints may remain billable or retain data.

### On-demand GPU pod or managed endpoint

A GPU host, pod, job, serverless worker, autoscaled endpoint, or similar resource is provisioned through an API, MCP server, workflow system, or provider control plane.

Use when:

- specialist demand is bursty;
- local hardware is unavailable or insufficient;
- startup latency is acceptable;
- the workflow can persist artifacts and prove teardown.

Treat the provider resource ID as a first-class workflow artifact from the first successful create response until billing closure is verified.

### Mutually exclusive local models

Two or more models cannot remain loaded together because their combined RAM, VRAM, runtime, or device requirements exceed the safe envelope.

Declare a mutual-exclusion group such as:

```text
resource_group: gpu-0-primary
capacity: 24 GB VRAM
members:
  - qwen3-30b-a3b-q4
  - flux-image-worker
  - whisper-large-worker
policy: one-heavy-member-at-a-time
```

Scheduling must reserve the group before unload or load begins. Prompt-level coordination is insufficient when several agents can issue concurrent resource operations.

## Resource record

Maintain one authoritative record per resource instance:

```text
Resource record ID:
Resource class:
Provider or host:
Provider resource ID:
Account, project, region, and zone:
Control-plane endpoint and API version:
Owner workflow and owner task:
Exact model, artifact, revision, runtime, and quantization:
Requested hardware and storage:
Mutual-exclusion group and capacity reservation:
Data classification and permitted inputs:
Created at:
Lease owner and lease expiry:
Desired state:
Last observed provider state:
Last observed service state:
Readiness evidence:
Active jobs and dependent artifacts:
Idle deadline and maximum lifetime:
Shutdown deadline:
Billable child resources:
Last reconciliation attempt:
Terminal state and verification evidence:
```

Do not use a model-generated natural-language summary as the authoritative state. Store identifiers, timestamps, states, and evidence in deterministic structured data.

## Lifecycle state machine

Provider-specific states should be mapped into a stable orchestration state machine.

| State | Meaning | Required evidence before transition |
| --- | --- | --- |
| `DECLARED` | Resource requirement and policy exist; nothing has been requested | Exact assignment, budget, data class, owner, capacity, and fallback |
| `RESERVED` | Local capacity, quota, lease, and mutual-exclusion group are reserved | Reservation token or lease with expiry |
| `START_REQUESTED` | Idempotent create, start, load, or scale request was sent | Request ID, idempotency key, desired resource specification |
| `PROVISIONING` | Authoritative control plane reports creation or startup in progress | Provider resource ID and observed non-ready state |
| `READY_CHECK` | Infrastructure exists; service and model readiness are being verified | Reachable control and data planes |
| `READY` | Correct service, artifact, storage, permissions, and capability probe passed | Readiness evidence bound to resource and model revision |
| `BUSY` | One or more accepted jobs own the resource | Job IDs, leases, input policy, deadlines, and expected artifacts |
| `DRAINING` | No new work accepted; active jobs are finishing or being cancelled | Closed admission, active-job inventory, drain deadline |
| `PERSISTING` | Required outputs, logs, metadata, and checkpoints are copied and verified | Durable locations, size, checksum, and access verification |
| `STOP_REQUESTED` | Idempotent unload, scale-to-zero, stop, or terminate request was sent | Request ID and shutdown deadline |
| `TERMINATING` | Provider or local supervisor reports shutdown in progress | Reconciled observed state |
| `STOPPED` | Compute or model residency is no longer active | Process, service, device, or provider-state proof |
| `BILLING_CHECK` | Remaining billable resources are enumerated and reconciled | Inventory of compute, endpoint, IP, volume, snapshot, and reservation state |
| `CLOSED` | Required artifacts persist and no unintended billable or data-bearing resource remains | Terminal evidence and released lease |
| `CLEANUP_FAILED` | Stop, persistence, deletion, or billing reconciliation failed | Failure class, attempts, next retry, and escalation owner |
| `QUARANTINED` | Resource cannot safely receive work or be deleted automatically | Incident record, blocked admission, and human or privileged owner |

A workflow should not jump directly from `BUSY` to `CLOSED`. Persistence, stop verification, and billing reconciliation are separate gates.

## Complete on-demand lifecycle

### 1. Need check

Confirm:

- the task cannot be completed acceptably by an already available deterministic tool, model, or service;
- the selected resource supports the exact modality, artifact, runtime, and quality tier;
- cold-start and queue latency fit the workflow;
- the task is still valid and has not already completed elsewhere.

### 2. Policy and budget check

Before allocation, verify:

- permitted data class, region, account, provider, model, and use;
- license, output, retention, and consent constraints;
- maximum startup cost, running cost, duration, storage, transfer, and retry budget;
- maximum lifetime and hard shutdown deadline;
- fallback behavior when allocation is denied or delayed.

### 3. Reserve capacity and obtain a lease

Reserve local VRAM, provider quota, concurrency, and mutual-exclusion groups before changing runtime state.

The lease should include:

- owner workflow and task;
- resource or capacity group;
- creation time and expiry;
- renewal rules;
- fencing token or monotonic generation where concurrent controllers are possible;
- recovery owner if the orchestrator disappears.

A lock without an expiry can leak capacity. An expiry without fencing can allow a stale controller to stop or reuse a resource owned by a newer workflow.

### 4. Start idempotently

Use an idempotency key derived from a stable operation ID, not a conversational phrase. Persist the create request and response before retrying.

After timeout or transport failure:

1. query by idempotency key, operation ID, provider resource ID, tags, or owner metadata;
2. determine whether the original request succeeded;
3. reuse or clean up the existing resource;
4. create another resource only when duplicate allocation is ruled out.

### 5. Verify authoritative infrastructure state

Poll the provider or local supervisor rather than trusting the create response. Record every observed state and terminal failure.

Verify:

- expected resource ID, type, region, hardware, image, and storage;
- network endpoint and access policy;
- mounted durable and ephemeral paths;
- expected process or container identity;
- absence of conflicting prior workloads.

### 6. Prove model and service readiness

A TCP connection or HTTP 200 health response may only prove that a proxy is alive.

A readiness probe should establish, where applicable:

- correct model ID, artifact revision, quantization, tokenizer, runtime, and adapter;
- weights loaded on the intended device;
- expected context, modality, tools, and output schema;
- required storage readable and writable;
- a bounded capability probe succeeds;
- probe output is not a cached response from another deployment;
- observed latency and memory remain within the profile.

Keep liveness and readiness separate. A live but not ready service should not receive production work.

### 7. Execute under a job lease

Every job should bind:

- resource record and fencing generation;
- input and output IDs;
- task acceptance criteria;
- quality tier;
- timeout and cancellation policy;
- retry and escalation budget;
- durable artifact destination;
- cleanup dependency.

Refresh the resource idle timer only for accepted activity. Rejected health probes, unauthorized requests, and stale workers should not keep a costly resource resident indefinitely.

### 8. Verify result before release

Do not release the resource from a worker's completion message alone. Verify:

- terminal job state;
- expected number and type of outputs;
- decoder, schema, test, or domain validation;
- no missing pages, frames, segments, files, or dependent tasks;
- review and escalation state;
- whether another approved job still depends on the resource.

### 9. Persist artifacts durably

Before teardown, copy every required artifact outside ephemeral storage and verify:

- durable URI or path;
- file or object count;
- size and checksum;
- metadata, prompts, parameters, seeds, versions, logs, and provenance;
- access from the downstream consumer;
- encryption, retention, and deletion policy;
- checkpoint or resume state when work may continue later.

A successful upload request is not proof that the durable object is complete and readable.

### 10. Drain and stop idempotently

Close admission before shutdown. Inventory active jobs, cancel or finish them according to policy, and set a drain deadline.

Send an idempotent unload, scale-to-zero, stop, or terminate request. Repeated stop calls should converge on the same desired state and should not recreate, duplicate, or orphan resources.

### 11. Verify provider and local state

Continue reconciliation until the authoritative state is terminal or the cleanup deadline expires.

Check separately:

- model unloaded;
- process or container stopped;
- GPU pod, VM, job, or endpoint terminated or scaled to zero;
- network endpoint removed where required;
- device memory and local capacity released;
- lease released only after the intended state is observed.

### 12. Reconcile billing and child resources

Enumerate resources that may bill or retain data independently:

- persistent and ephemeral volumes;
- snapshots and images;
- object storage;
- static or public IP addresses;
- load balancers and gateways;
- reserved capacity or autoscaling minimums;
- managed endpoints and replicas;
- caches, uploaded files, sessions, vector stores, batch jobs, and logs.

The compute resource can be stopped while a child resource remains billable. Close only when intended retained resources are documented and unintended resources are absent.

### 13. Retry cleanup and escalate

Classify cleanup failure:

- transient provider error;
- permission or credential failure;
- dependency still active;
- stale lease or competing controller;
- unknown or inconsistent provider state;
- artifact persistence failure;
- quota, billing, or API defect.

Use bounded exponential backoff with jitter for transient failures. Escalate with the resource ID, owner, cost exposure, last observed state, attempts, next deadline, and safe manual action. Never hide a cleanup failure behind a successful task result.

## Residency policy

### Admission control

Before admitting work, verify:

- resource is `READY` or already `BUSY` under compatible concurrency;
- lease and fencing token are current;
- data class and permissions are compatible;
- RAM, VRAM, disk, queue, context, and concurrency limits remain within the tested envelope;
- deadline leaves enough time for execution, persistence, and cleanup.

### Idle timeout

Use both:

- a **soft idle deadline** that begins drain or unload;
- a **hard maximum lifetime** that prevents indefinite residency even under faulty activity refresh.

State transitions and deadlines should use monotonic time where possible. Wall-clock changes must not extend a billable lease unexpectedly.

### Warm pools

A warm pool trades cost for latency. Record:

- minimum and maximum warm instances;
- supported artifact set;
- preloading and eviction policy;
- queue threshold that triggers scale-out;
- maximum idle and absolute lifetime;
- ownership transfer and state sanitization between tenants or tasks;
- cost per accepted result compared with cold start.

### Mutually exclusive workers

Use a deterministic scheduler, not model negotiation, to enforce:

- capacity reservation;
- unload and stop completion before replacement load;
- artifact persistence before eviction;
- priority and starvation policy;
- rollback when the replacement fails readiness;
- return to the previous resident model when required.

If a replacement model fails to load, the orchestrator should know whether to restore the previous model, use a hosted fallback, queue work, or fail closed.

## Hosted API lifecycle

For synchronous APIs, preserve request IDs, usage, response status, retry eligibility, and output validation.

For asynchronous or batch APIs, model the full job lifecycle:

```text
SUBMITTED -> ACCEPTED -> QUEUED -> RUNNING -> SUCCEEDED | FAILED | CANCELLED | EXPIRED
```

Do not infer success from submission. Poll, receive a signed callback, or use another authoritative completion mechanism. Handle duplicate callbacks and out-of-order events idempotently.

For uploaded provider files or sessions:

- define purpose and owner;
- restrict access;
- record provider object IDs;
- verify processing state;
- delete or retain according to policy;
- verify deletion when required;
- preserve local evidence that does not expose the deleted content unnecessarily.

## Concurrency and conflict control

Resource operations are state-changing and should normally be serialized per resource instance.

Use:

- compare-and-set version or generation;
- lease with fencing token;
- idempotent operation IDs;
- deterministic admission queue;
- dependency graph for shared storage and artifacts;
- explicit ownership transfer;
- reconciliation after controller restart.

Test races such as:

- start and stop requested concurrently;
- idle timeout fires while a job is accepted;
- two workflows create duplicate pods after a timeout;
- a stale controller stops a resource leased by a newer workflow;
- a new task arrives while the resource is draining;
- artifact persistence and volume deletion overlap;
- provider callback arrives after cancellation;
- local process stops but provider state remains running.

## Failure and degraded operation

Define behavior for:

- provider or network outage;
- quota exhaustion or capacity unavailable;
- resource created but endpoint unreachable;
- endpoint reachable but wrong model loaded;
- model OOM during warm-up or execution;
- artifact copy incomplete or checksum mismatch;
- stop request accepted but state remains active;
- control-plane credentials expire;
- orchestrator crashes after create or before cleanup;
- provider reports an unknown or contradictory state.

Possible responses include:

- retry the same control-plane operation;
- restart or replace the resource;
- restore the previous resident model;
- route to a separately validated hosted or local fallback;
- queue work with expiry;
- cancel dependent jobs;
- fail closed;
- quarantine the resource and require human intervention.

Degraded mode must have its own quality, privacy, latency, and cost profile. A fallback route is not valid merely because it returns output.

## Security and data handling

- Grant the orchestrator only the control-plane permissions required for the declared resource classes.
- Separate model-data access from infrastructure-delete authority where risk warrants it.
- Store credentials in an approved secret manager; do not place them in model prompts, logs, or artifacts.
- Tag resources with non-secret owner, task, environment, expiry, and cost-allocation identifiers.
- Sanitize reused workers, memory, caches, volumes, and sessions between incompatible data classes.
- Do not upload data merely because a hosted fallback is available; routing policy must permit the exact provider and context.
- Preserve audit evidence while minimizing personal, confidential, biometric, and generated-media source data.
- Require stronger approval for destructive cleanup of shared or persistent resources.

## Reconciliation loop

Event-driven callbacks improve latency but do not replace periodic reconciliation.

A reconciler should:

1. list or query resources owned by the system;
2. match them to authoritative resource records;
3. detect missing, duplicate, orphaned, expired, or contradictory instances;
4. renew valid leases or fence stale owners;
5. resume persistence or cleanup;
6. close resources whose terminal evidence is complete;
7. alert on unresolved cost or data exposure.

Run reconciliation after orchestrator restart and at a frequency appropriate to cost exposure and provider behavior.

## Metrics and acceptance gates

Measure at least:

- allocation success and failure rate;
- duplicate allocation rate;
- queue, provision, model-load, readiness, and first-job latency;
- warm versus cold acceptance and latency;
- peak and idle RAM and VRAM;
- utilization and idle-residency ratio;
- jobs per resource lifetime;
- artifact persistence success and checksum failure;
- stop-request-to-stopped latency;
- stopped-to-billing-closed latency;
- leaked or orphaned resource count and duration;
- cleanup retries and human interventions;
- provider-state disagreement incidents;
- cost while useful, idle, provisioning, draining, and cleanup-failed;
- total infrastructure cost per accepted result.

Suggested production gates include:

- no job accepted before readiness proof;
- no teardown before required artifact verification;
- no resource record closed without provider-state and billing reconciliation;
- no unlimited startup, inference, or cleanup retry loop;
- every active resource has a non-expired owner or a documented recovery owner;
- every retained child resource has an explicit owner, purpose, retention, and cost policy.

## Test scenarios

Validate the lifecycle with controlled fault injection:

- duplicate create request after client timeout;
- provider capacity unavailable;
- wrong model or revision responds at the endpoint;
- readiness probe passes transport but fails capability;
- OOM during model load;
- orchestrator restarts in every non-terminal state;
- idle timeout races with a new job;
- worker completes while artifact upload fails;
- stop API returns success but resource stays active;
- volume or endpoint remains after compute termination;
- credential expiry during cleanup;
- stale controller attempts a stop after lease transfer;
- provider sends duplicated and out-of-order callbacks;
- network partitions during create and terminate;
- fallback route violates data policy or quality tier and must fail closed.

A lifecycle is not production-ready until recovery is tested from intermediate states, not only the happy path.

## Compact lifecycle record

Use this record or equivalent structured data:

```text
Workflow and task:
Resource record and provider IDs:
Resource class and lifecycle policy:
Exact model, artifact, runtime, hardware, endpoint, and region:
Data class and permissions:
Mutual-exclusion group, reservation, lease, expiry, and fencing generation:
Need, policy, and budget decision:
Create operation and idempotency key:
Observed provider and service states:
Readiness probes and exact model evidence:
Jobs, deadlines, retries, and dependent artifacts:
Durable artifact paths, counts, sizes, checksums, and validation:
Drain and stop operation:
Compute, endpoint, storage, IP, reservation, cache, and session reconciliation:
Cleanup failures, retry schedule, and escalation owner:
Useful, idle, startup, drain, and leaked cost:
Terminal state and closure evidence:
Verified date and re-evaluation triggers:
```

The lifecycle state machine, records, gates, and test plan are repository-authored operational guidance. They organize established distributed-systems, infrastructure, workflow, and safety practices and make no claim of novelty.

## Related pages

- [Choosing Models for Agent Orchestration](../..)
- [Choosing Model Portfolios for Combined Workloads](../../../combined-workloads/)
- [Concrete Model Portfolio Profiles](../../../combined-workloads/sub/environment-profiles/)
- [Agent Role Selection](../../../agent-role-selection/)
- [Defining Model Reliability Profiles](../../../reliability-profiles/)
- [Multi-Agent Systems](../../../../../../../concepts/sub/agents-and-automation/sub/multi-agent-systems/)
- [Agent Orchestration Tools](../../../../../../../../../software/sub/agent-orchestration/)
