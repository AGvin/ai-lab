# Resource Lifecycle Controller Architecture

Legacy residual retained for AI-resource control-plane pedagogy, lifecycle/reconciliation contracts, and exact legacy framework evidence because its selected engineering/agent-operations learning owners are not yet materialized on the active branch.

> **Migration note:** Generic infrastructure/system boundaries are preserved in `docs/sub/concepts/sub/ai-engineering/sub/system-design/`; retry/recovery semantics are preserved in `docs/sub/concepts/sub/ai-engineering/sub/reliability-and-resilience/`; reusable cost/capacity/budget semantics are preserved in `docs/sub/concepts/sub/ai-engineering/sub/cost-and-capacity/`. The readiness design routes operational teaching across selected AI-engineering and agent operations nodes rather than creating a duplicate agent concept, but relevant selected learning nodes such as `ai-engineering/infrastructure-and-hardware/cloud-and-rented-capacity/` and `agents-and-automation/operations-and-control/cost-and-resource-budgets/` are currently absent on the active AI Lab ref. Preserve the lifecycle-specific material below until those owners are materialized and verified.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Authoritative resource-control residual

A resource lifecycle controller treats model processes, GPU pods, endpoints, storage, sessions, hosted jobs, caches, and other billable/stateful infrastructure as first-class workflow resources with authoritative desired/observed state and verified closure.

Workers request capability; deterministic control-plane code owns allocation, readiness, leases, admission, draining, teardown, and reconciliation. Worker completion is not proof that a billable resource stopped or that retained children were removed.

For each supported resource class, define where relevant:

- authoritative resource-record schema and provider/local identity;
- desired/observed lifecycle states;
- lease/expiry/fencing and ownership rules;
- capacity or mutual-exclusion group;
- readiness/capability probes and job admission;
- artifact persistence requirements;
- drain/stop/delete/reconciliation policy;
- billing/retained-child-resource closure policy;
- retry/quarantine/escalation/human authority.

Model-generated prose is not the authoritative resource record.

## Lifecycle and responsibility residual

Normalize provider-specific states into a stable lifecycle that distinguishes declaration/reservation/start/provisioning/readiness/busy/draining/persistence/stop/termination/stopped/billing-closure and cleanup-failure/quarantine states as needed.

Do not jump from task completion directly to `CLOSED`: durable artifact verification, compute shutdown, child-resource inventory, lease release, and billing/data-retention closure are separate gates.

Keep responsibility explicit between task owner, resource controller, worker, artifact/result validator, approval authority for exceptional/high-impact operations, and reconciler for stale/orphaned/contradictory state. One implementation may hold several roles only when authority and failure consequences remain acceptable.

## Provisioning and readiness residual

Before creation/load, verify owner/task need, exact model/runtime/hardware/storage/region/data-policy requirements, quota/budget/max lifetime/fallback, local capacity or mutual exclusion, stable operation identity/idempotency key, and a cleanup owner if the initiating workflow disappears.

After an ambiguous provisioning timeout, query authoritative provider/local state before creating a replacement.

Separate liveness from readiness. A useful readiness contract may verify resource identity/region, model/artifact/runtime revision, required storage/network access, intended device placement, expected modalities/context/tools/schema, a bounded capability probe, and tested latency/memory envelope. A reachable proxy or generic HTTP success does not prove the correct model/workload capability is ready.

## Lease, fencing, admission, and residency residual

Active resources should have an owner workflow/task, lease expiry/renewal policy, hard maximum lifetime, recovery owner, and a monotonic fencing generation where competing controllers are possible.

An expired lock without cleanup can leak cost; a lease without fencing can let a stale controller mutate or stop a resource now owned by a newer workflow.

Before job admission, verify compatible lifecycle state, tested capacity/queue/RAM/VRAM/disk/context/concurrency envelope, data/permission boundaries, enough remaining deadline for execution/validation/persistence/cleanup, and absence of conflicting ownership in shared resource groups.

Idle/residency policy should distinguish soft drain from a hard lifetime. Health probes or incidental traffic should not keep expensive resources resident indefinitely unless policy explicitly intends that behavior.

## Artifact durability and teardown residual

Before teardown, verify required outputs outside ephemeral storage, including durable location, expected object count/size/checksum where relevant, provenance/config needed for reproduction, downstream readability/access, retention/deletion policy, and resume state when required.

A successful upload request is not proof that the required artifact is complete and readable.

A safe teardown sequence may:

1. close new admission;
2. inventory/drain active work;
3. persist and validate required artifacts;
4. request unload/scale-to-zero/stop/terminate/delete idempotently;
5. poll authoritative provider/supervisor state;
6. verify local process/device release;
7. enumerate compute, endpoints, storage, snapshots, addresses, caches, files, sessions, reserved capacity, and other children;
8. retain only explicitly owned resources;
9. retry/escalate cleanup failure;
10. release leases and close only after required billing/data-retention evidence is complete.

A stopped compute instance can still leave billable or data-bearing children.

## Reconciliation and degraded-operation residual

Use periodic reconciliation in addition to callbacks when leaked/stale resources matter. Reconciliation should enumerate system-owned provider/local resources, match authoritative records, detect missing/duplicate/orphaned/expired/contradictory instances, fence stale owners, resume persistence/cleanup, verify closure, and surface unresolved cost/data exposure.

Reconcile after controller restart and provider/network outage rather than assuming missed events will self-heal.

Define behavior for capacity/quota failure, created-but-unreachable resources, wrong model/runtime readiness, OOM/load failure, artifact persistence failure, stop accepted while resource remains active, credential expiry during cleanup, controller crash in intermediate states, provider-state contradiction, or network partition during create/terminate. Depending on policy, recovery can include bounded retry, replacement, restoration of prior resident capability, separately validated fallback, queue-with-expiry, fail-closed cancellation, quarantine, or human intervention.

## Pattern-fit and evaluation residual

A dedicated controller is useful for on-demand GPU/media services, local mutually-exclusive model residency, always-on generalists with temporary specialists, asynchronous hosted jobs, autoscaled endpoints/warm pools, resources whose cost/data retention persists beyond inference, and systems that must recover after controller failure.

Avoid a separate lifecycle controller when the provider operation is genuinely stateless and exposes no customer-managed lifecycle object, or when one local in-process model has no dynamic load/shared-capacity/cleanup risk large enough to justify the control plane.

Evaluate provisioning/readiness success, duplicate allocation/stale-owner incidents, cold/warm startup, useful versus idle/provisioning/draining/leaked resource cost, artifact persistence/checksum success, stop-to-stopped and stopped-to-billing-closed latency, orphan duration/count, cleanup retries/quarantines/human interventions, and infrastructure cost per accepted result.

## Legacy evidence-provenance residual

The legacy source cited AutoGen runtime documentation as framework evidence for agent communication/identity/lifecycle in standalone or distributed environments:

- [AutoGen agent runtime environments](https://microsoft.github.io/autogen/stable/user-guide/core-user-guide/core-concepts/architecture.html)
- [AutoGen distributed agent runtime](https://microsoft.github.io/autogen/stable/user-guide/core-user-guide/framework/distributed-agent-runtime.html)

Preserve these exact framework references until the selected engineering/agent-operations learning/evidence owners are materialized and their current/historical evidence disposition is verified.

These resource-lifecycle-specific pedagogical, operational, and evidence fragments remain migration source material until their exact owners are ready.
