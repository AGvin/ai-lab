# Resource Lifecycle Orchestration

Design and evaluate orchestration for resident models, lazy-loaded services, idle-timeout workers, temporary GPU resources, hosted APIs, and mutually exclusive local models.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Status

Implemented operational guidance verified on 2026-07-25. Provider states, billing semantics, APIs, quotas, and cleanup guarantees differ; bind every implementation to the exact provider, control plane, resource type, and verification date.

## Core rule

A model worker and the infrastructure that runs it are different control subjects.

A worker can finish inference while the process, endpoint, GPU pod, storage, reservation, address, cache, or load balancer remains active or billable. A provider can accept a stop request without completing it.

**A worker completion report is not proof that a billable resource stopped.** Verify resource and billing state independently through the authoritative control plane.

## Resource classes

### Resident

The service and model remain loaded. Use when sustained or latency-sensitive demand justifies idle occupancy. Measure idle cost, memory pressure, health, queueing, and restart behavior.

### Lazy-loaded

The endpoint remains available but loads the model on demand. Distinguish endpoint readiness from model readiness and account for cold-start failure, load latency, and memory admission.

### Idle-timeout

A loaded model remains resident for a bounded idle interval. Renew activity from authoritative accepted work, not untrusted traffic. Prevent timeout races with new leases or jobs.

### Temporary

The resource is created for a bounded task or batch and must reach a verified terminal state. Record ownership, deadline, budget, expiry, cleanup policy, and all child resources.

### Hosted API

No local residency is controlled, but endpoint, version, quota, provider health, region, retention, rate limit, cost, and fallback remain lifecycle concerns.

### Mutually exclusive

Two models or services cannot coexist under the available RAM, VRAM, ports, storage, or runtime constraints. Place them in an explicit exclusion group and schedule unload, persistence, load, readiness, and rollback as state transitions.

## Authoritative resource record

Create a durable record before a state-changing operation. Include:

- internal resource and workflow IDs;
- provider, account, project, region, resource type, and provider IDs;
- exact model, artifact, runtime, hardware, endpoint, and storage;
- owner, task, environment, data class, permissions, and cost allocation;
- requested, observed, and reconciled states;
- operation IDs and idempotency keys;
- lease holder, fencing generation, expiry, and heartbeat;
- dependent jobs, artifacts, services, and child resources;
- budget, deadline, idle policy, and teardown policy;
- last observation, evidence, error, retry, and escalation owner.

Do not treat a model-generated narrative as authoritative state.

## Lifecycle state machine

A practical state model may include:

```text
Requested
AdmissionPending
Provisioning
ProviderRunning
ServiceStarting
Ready
Busy
Idle
Draining
Persisting
StopRequested
ProviderStopping
Stopped
BillingPending
Closed
Failed
CleanupFailed
Quarantined
```

Define allowed transitions, transition owner, timeout, retry, rollback, evidence, and terminal conditions. Unknown or contradictory provider state must not silently become `Ready` or `Closed`.

## Admission and reservation

Before allocation:

1. verify task need, data eligibility, permissions, and quality tier;
2. select the exact resource and fallback;
3. check provider availability, quotas, and budget;
4. reserve mutually exclusive local resources or external capacity;
5. create the authoritative record and idempotency key;
6. reject duplicate or stale requests through compare-and-set or fencing.

Admission should fail closed when the required data, cost, permission, or cleanup policy is unknown.

## Idempotency, leases, and fencing

State-changing operations must tolerate retries after timeouts and controller restarts.

Use:

- stable idempotency keys for create, start, drain, stop, and delete;
- compare-and-set version or generation;
- bounded leases with renewable expiry;
- fencing tokens that reject stale owners;
- one serialized operation stream per resource instance;
- deterministic ownership transfer;
- reconciliation after every controller restart.

A lease expiry does not itself prove the resource stopped. It authorizes recovery or takeover under the declared policy.

## Readiness proof

A provider `running` state is not sufficient. Verify:

- the expected endpoint and authentication;
- exact model, revision, runtime, and required auxiliary files;
- health and capability probes;
- minimum free memory or storage;
- required data volume and artifact access;
- test inference or generation under a bounded probe;
- deadline and lease validity.

Prevent jobs from entering before readiness evidence is attached to the current resource generation.

## Execution and residency

During work:

- bind jobs to the resource generation and lease;
- enforce queue, concurrency, context, memory, and budget limits;
- preserve prompts, parameters, tool calls, seeds, inputs, outputs, and provenance as required;
- monitor OOM, saturation, timeout, cancellation, provider error, and quality failure;
- renew the lease only for valid accepted work;
- reject stale callbacks and duplicate jobs;
- persist required state before model swap or shutdown.

The orchestrator must not schedule concurrent work to mutually exclusive services.

## Artifact persistence

Before teardown, copy required artifacts to durable approved storage and verify:

- expected paths and counts;
- size, checksum, format, and readability;
- metadata, provenance, prompt, parameters, seed, model identity, and timestamps;
- access controls, encryption, retention, and deletion policy;
- downstream availability and ownership.

A successful copy request is not proof that all artifacts are durable and valid.

## Drain and teardown

1. stop accepting new jobs;
2. fence stale producers and wait for or cancel bounded active work;
3. persist and verify required artifacts;
4. request service shutdown or scale-to-zero;
5. request compute termination;
6. reconcile endpoint, storage, address, reservation, cache, session, and other child resources;
7. verify provider terminal state;
8. verify billing closure or the provider-specific non-billable condition;
9. close the internal record only after evidence is complete.

Shared or persistent resources require stronger authorization and explicit ownership before deletion.

## Billing reconciliation

Track useful, idle, provisioning, draining, stopping, and cleanup-failed time separately. Record provider billing units, timestamps, retained child resources, reserved capacity, and delayed closure semantics.

Do not declare zero cost merely because compute is stopped. Storage, IPs, endpoints, reservations, subscriptions, minimum units, or transfer charges may remain.

Escalate unresolved cost exposure with resource IDs, owner, elapsed time, attempted operations, observed states, and estimated continuing cost.

## Races and concurrency

Test and control:

- concurrent start and stop;
- timeout while a new job is accepted;
- duplicate create after client timeout;
- stale controller acting after lease transfer;
- work arriving while draining;
- artifact persistence overlapping deletion;
- callback after cancellation;
- local process exit while provider state remains active.

Use serialized per-resource operations, dependency-aware cleanup, and explicit ownership transfer.

## Failure and degraded operation

Define behavior for:

- provider or network outage;
- quota or capacity failure;
- resource created but endpoint unavailable;
- endpoint available with the wrong model;
- OOM during load or execution;
- incomplete or corrupt artifact persistence;
- stop accepted but resource still active;
- expired credentials during cleanup;
- orchestrator crash in every non-terminal state;
- unknown or contradictory provider state.

Permitted responses may include bounded retry, restart, replacement, restoration of a prior resident model, separately validated fallback, queue with expiry, cancellation, fail-closed behavior, quarantine, or human intervention.

A fallback needs its own quality, privacy, latency, permission, and cost profile.

## Reconciliation loop

Callbacks improve latency but do not replace periodic reconciliation.

The reconciler should:

1. enumerate owned resources and child resources;
2. match them to authoritative records;
3. detect missing, duplicate, orphaned, expired, and contradictory instances;
4. renew valid leases or fence stale owners;
5. resume persistence, drain, stop, or cleanup;
6. confirm provider and billing closure;
7. alert on unresolved cost, data, permission, or security exposure.

Run reconciliation after controller restart and at a frequency proportionate to risk and cost exposure.

## Security and data handling

- grant least-privilege control-plane permissions;
- separate data access from destructive infrastructure authority where appropriate;
- keep credentials in an approved secret manager, not prompts, logs, or artifacts;
- tag resources with non-secret ownership, environment, expiry, and cost identifiers;
- sanitize reused workers, caches, volumes, memory, and sessions between incompatible data classes;
- permit hosted fallback only for the exact approved provider, endpoint, region, and data class;
- preserve audit evidence while minimizing personal, confidential, biometric, and source-media data.

## Metrics and acceptance gates

Measure:

- allocation, duplicate-allocation, and readiness failure rates;
- queue, provision, model-load, readiness, and first-job latency;
- warm and cold acceptance and latency;
- peak and idle RAM and VRAM;
- utilization, idle-residency ratio, and jobs per lifetime;
- artifact persistence and checksum failures;
- stop-request-to-stopped and stopped-to-billing-closed latency;
- leaked or orphaned resource count, duration, and cost;
- cleanup retries, provider-state disagreements, and human interventions;
- infrastructure cost per accepted result.

Production gates should require:

- no job before readiness proof;
- no teardown before required artifact verification;
- no record closure before provider and billing reconciliation;
- no unlimited startup, execution, or cleanup retries;
- every active resource has a valid owner or recovery owner;
- every retained child resource has an owner, purpose, retention, and cost policy.

## Fault-injection suite

Test:

- duplicate create after timeout;
- provider capacity unavailable;
- wrong model at the endpoint;
- transport-ready but capability-unready service;
- OOM during model load;
- controller restart in every non-terminal state;
- idle timeout racing with a new job;
- worker completion while artifact upload fails;
- successful stop response while compute remains active;
- surviving storage, endpoint, IP, or reservation after termination;
- credential expiry during cleanup;
- stale stop after lease transfer;
- duplicated or out-of-order callbacks;
- network partition during create and terminate;
- fallback that violates data or quality policy and must fail closed.

A lifecycle is not production-ready until intermediate-state recovery is tested, not only the happy path.

## Lifecycle record

```text
Workflow, task, resource record, and provider IDs:
Resource class, policy, owner, lease, expiry, and fencing generation:
Exact model, artifact, runtime, hardware, endpoint, region, and data class:
Need, permission, availability, and budget decision:
Create, start, readiness, jobs, retries, and observed states:
Artifacts, durable paths, counts, sizes, checksums, and validation:
Drain, stop, compute, endpoint, storage, address, and billing reconciliation:
Cleanup failures, retry schedule, escalation owner, and continuing cost:
Terminal state, closure evidence, verified date, and re-evaluation triggers:
```

## Related pages

- [Choosing Models for Agent Orchestration](../..)
- [Combined Workloads](../../../combined-workloads/)
- [Concrete Model Portfolio Profiles](../../../combined-workloads/sub/environment-profiles/)
- [Agent Role Selection](../../../agent-role-selection/)
- [Reliability Profiles](../../../reliability-profiles/)
- [Multi-Agent Systems](../../../../../../../concepts/sub/agents-and-automation/sub/multi-agent-systems/)
- [Agent Orchestration Tools](../../../../../../../../../software/sub/agent-orchestration/)
- [General repository disclaimer](../../../../../../../../../disclaimer/)
