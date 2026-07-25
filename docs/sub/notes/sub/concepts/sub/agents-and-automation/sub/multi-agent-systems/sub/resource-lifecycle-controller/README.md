# Resource Lifecycle Controller Architecture

A resource lifecycle controller treats model processes, GPU pods, endpoints, storage, sessions, and other billable or stateful infrastructure as first-class workflow resources with authoritative state and verified closure.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Status

Established control-plane pattern adapted for agent and model systems.

## Core idea

```text
workflow or agent -> resource controller -> provider or local supervisor
                          |
                          v
authoritative resource state, lease, readiness, jobs, artifacts, teardown, billing closure
```

Workers request capability. The resource controller owns allocation, readiness, leases, admission, draining, teardown, and reconciliation through deterministic control-plane operations.

A worker reporting completion is not proof that a billable resource stopped.

## Distinguish related patterns

- **Resource lifecycle controller:** owns infrastructure state and safe transitions.
- **Orchestrator-worker:** owns task decomposition, delegation, and result synthesis.
- **Event-driven:** may deliver lifecycle events and callbacks but does not by itself define authoritative resource state.
- **Graph or DAG:** may encode lifecycle stages and dependencies.
- **Hosted API call:** may use provider-managed model residency while still creating customer-managed jobs, files, sessions, caches, or endpoints.

The same model must not be responsible for both claiming its task is complete and authoritatively declaring the surrounding infrastructure closed.

## Resource classes

The controller may manage:

- always-running and always-resident models;
- reachable services with lazy model loading;
- models retained for a bounded idle timeout;
- task-specific temporary local processes or containers;
- mutually exclusive models sharing one RAM or VRAM envelope;
- external hosted API jobs, files, sessions, and caches;
- on-demand GPU pods, VMs, serverless workers, or managed endpoints;
- attached storage, snapshots, network endpoints, reserved capacity, and other child resources.

Each class requires explicit desired and observed state semantics.

## Controller contract

Record:

```text
Controller ID and version:
Supported providers and resource classes:
Authoritative resource record schema:
Desired and observed states:
Lease, expiry, and fencing policy:
Capacity and mutual-exclusion groups:
Readiness and capability probes:
Admission and job ownership:
Artifact persistence requirements:
Drain, stop, deletion, and reconciliation policy:
Billing and retained-child-resource policy:
Retry, quarantine, escalation, and human authority:
```

Model-generated prose is not the authoritative resource record.

## Stable lifecycle

Map provider-specific states into a stable lifecycle such as:

```text
DECLARED -> RESERVED -> START_REQUESTED -> PROVISIONING -> READY
READY -> BUSY -> DRAINING -> PERSISTING -> STOP_REQUESTED
STOP_REQUESTED -> TERMINATING -> STOPPED -> BILLING_CHECK -> CLOSED
                                      \-> CLEANUP_FAILED -> QUARANTINED
```

Do not jump directly from worker completion to `CLOSED`. Durable artifact verification, compute shutdown, child-resource inventory, and billing closure are separate gates.

## Separation of responsibility

A safe design separates:

- **task owner:** decides that capability is required;
- **resource controller:** provisions and observes infrastructure;
- **worker:** performs the bounded model task;
- **validator or reviewer:** checks the artifact;
- **approval authority:** authorizes high-cost, destructive, or exceptional operations;
- **reconciler:** detects orphaned, stale, contradictory, or leaked resources.

One implementation may hold several roles only when permissions, evidence, and failure consequences remain acceptable.

## Provisioning

Before creation or load, verify:

- task need and valid owner;
- exact model, runtime, hardware, storage, region, and data policy;
- quota, budget, maximum lifetime, and fallback;
- local capacity and mutual-exclusion reservation;
- stable operation and idempotency key;
- cleanup owner if the initiating workflow disappears.

After timeout, query authoritative provider state before creating a replacement. A lost response does not prove that provisioning failed.

## Readiness

Separate liveness from readiness. A ready resource should prove, where applicable:

- expected resource identity and region;
- correct model, artifact revision, quantization, runtime, and adapter;
- required storage and network access;
- model loaded on the intended device;
- expected modalities, context, tools, and schema;
- a bounded capability probe;
- acceptable latency and memory envelope.

A reachable proxy or HTTP 200 response is not sufficient evidence that the correct model is ready.

## Leases and fencing

Every active resource should have:

- owner workflow and task;
- lease expiry and renewal policy;
- monotonic fencing generation where competing controllers are possible;
- hard maximum lifetime;
- recovery owner.

An expired lock can leak cost. A lease without fencing can let a stale controller stop or mutate a resource owned by a newer workflow.

## Admission and residency

Before accepting a job, verify:

- current state is compatible;
- capacity, queue, RAM, VRAM, disk, context, and concurrency remain within the tested envelope;
- data class and permissions match;
- deadline leaves time for execution, validation, persistence, and cleanup;
- a conflicting model or task does not own the resource group.

Idle policies should use a soft drain deadline and a hard maximum lifetime. Health probes and unauthorized traffic should not keep expensive resources resident indefinitely.

## Artifact durability

Before teardown, verify required outputs outside ephemeral storage:

- durable URI or path;
- expected object count;
- size and checksum;
- prompts, parameters, seeds, model versions, logs, and provenance;
- downstream read access;
- retention and deletion policy;
- resume state where required.

A successful upload request is not proof that an artifact is complete and readable.

## Teardown and billing closure

The controller should:

1. close admission;
2. inventory and drain active jobs;
3. persist and validate artifacts;
4. request unload, scale-to-zero, stop, terminate, or delete idempotently;
5. poll authoritative provider or supervisor state;
6. verify local process and device release;
7. enumerate compute, endpoint, storage, snapshot, IP, cache, file, session, and reserved-capacity children;
8. retain only explicitly owned resources;
9. retry or escalate cleanup failures;
10. release leases and close the record only after evidence is complete.

A stopped compute instance can still leave billable or data-bearing children.

## Reconciliation

Run a periodic reconciler in addition to event callbacks. It should:

- list system-owned provider and local resources;
- match them to resource records;
- detect missing, duplicate, orphaned, expired, or contradictory instances;
- fence stale owners;
- resume persistence or cleanup;
- verify billing closure;
- alert on unresolved cost or data exposure.

Reconcile after controller restart and provider or network outage.

## Failure and degraded operation

Define behavior for:

- quota or capacity unavailable;
- resource created but endpoint unreachable;
- wrong model loaded;
- OOM during load or execution;
- artifact persistence failure;
- stop accepted but resource remains active;
- credential expiry during cleanup;
- controller crash in every intermediate state;
- provider state contradiction;
- network partition during create or terminate.

Possible responses include retry, replacement, restoration of the prior resident model, a separately validated hosted or local fallback, queueing with expiry, fail-closed cancellation, quarantine, or human intervention.

## Suitable uses

- on-demand GPU and media-generation services;
- local systems that swap mutually exclusive models;
- always-on generalists with temporary specialists;
- asynchronous hosted model jobs;
- autoscaled endpoints and warm pools;
- workflows where infrastructure cost or data retention continues after inference;
- long-running systems that must recover after controller failure.

## Poor fits

Avoid a separate controller when:

- the model call is fully stateless and the provider exposes no customer-managed lifecycle object;
- one local in-process model has no dynamic load, shared capacity, or cleanup requirement;
- control-plane complexity exceeds the resource risk and cost.

Even then, retain enough state to validate requests, outputs, retries, and provider data retention.

## Strengths

- separates task success from infrastructure closure;
- prevents duplicate allocation and stale ownership;
- makes readiness, residency, and mutual exclusion explicit;
- supports recovery and periodic reconciliation;
- reduces leaked compute, storage, sessions, and endpoints;
- creates auditable cost and data-retention evidence.

## Limitations

- requires provider adapters and state normalization;
- control-plane operations can be eventually consistent;
- leases, fencing, and reconciliation add substantial complexity;
- provider billing state may lag compute state;
- cleanup permissions are high-impact;
- a controller can become a critical failure and security boundary.

## Evaluation metrics

Record:

- provisioning and readiness success;
- duplicate allocation and stale-owner incidents;
- cold and warm startup latency;
- peak and idle resource use;
- artifact persistence and checksum success;
- stop-request-to-stopped and stopped-to-billing-closed latency;
- orphaned resource count and duration;
- cleanup retries, quarantines, and human interventions;
- useful, idle, provisioning, draining, and leaked cost;
- infrastructure cost per accepted result.

## Detailed operational guidance

Use the canonical [Resource Lifecycle Orchestration](../../../../../../../comparisons/sub/model-selection/sub/orchestration/sub/resource-lifecycle/) guide for the complete state machine, authoritative record, leases, idempotency, readiness proof, persistence, billing reconciliation, fault injection, and compact lifecycle record.

## Evidence and established usage

Agent runtimes such as AutoGen's manage agent communication, identity, and lifecycle across standalone or distributed environments. The broader controller pattern applies established control-plane, distributed-systems, and infrastructure lifecycle practices to model and agent resources.

Sources:

- [AutoGen agent runtime environments](https://microsoft.github.io/autogen/stable/user-guide/core-user-guide/core-concepts/architecture.html)
- [AutoGen distributed agent runtime](https://microsoft.github.io/autogen/stable/user-guide/core-user-guide/framework/distributed-agent-runtime.html)

## Related concepts

- [Multi-Agent Systems](../..)
- [Event-Driven Architecture](../event-driven/)
- [Graph or DAG Workflow](../graph-dag-workflow/)
- [Orchestrator-Worker Architecture](../orchestrator-worker/)
- [Human Approval Gates](../human-approval-gates/)
