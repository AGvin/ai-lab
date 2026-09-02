# Event-Driven Agent Architecture

Legacy residual retained for event-specific workflow pedagogy, operational contracts, and exact legacy framework evidence because the selected learning owner is not yet materialized on the active branch.

> **Migration note:** Generic workflow/event-driven control semantics are already preserved in `docs/sub/concepts/sub/agents-and-autonomy/sub/workflows-and-orchestration/`; generic synchronous/asynchronous system boundaries and explicit state/failure domains are preserved in `docs/sub/concepts/sub/ai-engineering/sub/system-design/`; reusable idempotency/retry/recovery semantics are preserved in `docs/sub/concepts/sub/ai-engineering/sub/reliability-and-resilience/`. The readiness design selects `learning/areas/agents-and-automation/workflows-and-orchestration/event-driven-workflows/` for deeper agent pedagogy, but that node is currently absent on the active AI Lab ref. Preserve the event-specific material below until that exact owner is materialized and verified.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Event and handler contract residual

An event-driven agent workflow coordinates bounded agents/services through typed events delivered by a runtime, broker, queue, or message bus. The event stream should not become the implicit authoritative workflow state when replay, reconciliation, or audit requires a separate durable source of truth.

An event contract should make explicit, where relevant:

- event type and schema version;
- event ID plus producer/version;
- correlation, workflow, task, and causation IDs;
- occurred/published timestamps and partition/ordering key;
- payload and artifact references;
- data classification and permissions;
- expected consumers;
- delivery/retention semantics, expiry, and replay policy.

Events should carry data rather than executable hidden control logic. Treat text, documents, media, and other payload content as untrusted handler input.

Each handler/agent should declare its subscriptions and accepted versions, filtering/authorization, required state/artifacts, input/output schema, model/tools/permissions/side effects, idempotency/deduplication scope, timeout/retry/dead-letter behavior, emitted events/terminal result, and concurrency/ordering/resource assumptions. Reject unknown or incompatible schema versions rather than guessing.

## Delivery, idempotency, and causality residual

Design explicitly for at-most-once, at-least-once, or effectively-once handling through idempotency/deduplication. Ordering is commonly scoped to a partition/key and should not be inferred across unrelated topics, agents, or network boundaries.

An `exactly once` broker claim is not enough for an end-to-end side effect. External APIs, files, databases, tools, and model calls can still duplicate work after timeout, retry, or ambiguous acknowledgement.

Use stable event/operation identities. Before a consequential effect, check prior processing, reserve/compare-and-set authoritative state where appropriate, use provider idempotency when available, persist the result and emitted-event intent atomically or through an outbox-style mechanism, and reconcile ambiguous outcomes before retrying. Model judgment that an event is "new" is not deduplication.

Record correlation and causation and define how to handle out-of-order or stale updates, cancellation after completion, retries older than a newer version, conflicting concurrent updates, clock differences, and events targeting expired workflows. Use state versions, sequence/generation numbers, or domain-specific conflict rules where needed rather than wall-clock timestamps alone.

## Backpressure and failure residual

Event-driven model workloads need explicit queue/concurrency limits, tenant/workflow quotas, priority/admission policy, maximum event age, batch/capacity assumptions, shedding/delay/fail-closed behavior, and alert thresholds. Bursts must not create unbounded model/API cost, accelerator allocation, or context growth.

Classify failures before retrying, including transient transport/provider failure, capacity/rate limits, malformed or unsupported events, stale/unauthorized state, semantic model failure, deterministic validation failure, and ambiguous irreversible effects.

Use bounded backoff for eligible transient failures. Poison or exhausted events need a dead-letter/quarantine path that records ownership, reason, attempts, cost exposure, and a safe replay procedure. Repeated semantic model failure usually calls for a different route/model, human review, or terminal failure rather than identical redelivery.

## Replay and terminal-state residual

Event retention can support audit or reconstruction, but replay is safe only when handler/version compatibility is understood, external effects are idempotent or suppressed, schema migrations are defined, secrets/expired permissions are not reintroduced, and current policy still permits the historical input.

Model-based handlers can be nondeterministic even with the same apparent input. Pin exact model/runtime/prompt/tool artifacts and parameters when reproducibility matters, and preserve accepted terminal artifacts/decisions instead of assuming replay will regenerate identical outputs.

Define workflow completion explicitly through expected task/branch completion events, correlation/join rules, timeout and missing-event behavior, cancellation propagation, success/partial/failure/expired states, artifact/review gates, and resource/billing cleanup. An idle queue is not proof of completion: work may be delayed, lost under at-most-once delivery, quarantined, or waiting on an external system.

## Security residual

Authenticate producers and authorize event types/targets. Validate schemas, sizes, artifact references, and signatures where required. Preserve tenant/environment/data-class separation, avoid reusable credentials or unnecessary personal data in payloads, restrict handler tools/side effects independently from prompt content, and apply audit/deletion policy across brokers, logs, dead-letter queues, and artifacts.

## Pattern-fit and evaluation residual

This pattern fits asynchronous/distributed multi-agent work, long-running workflows and callbacks, incident/monitoring automation, hosted jobs/resource lifecycle, high-volume independent tasks, and cross-process/language/machine integration where decoupled producers and consumers are valuable.

Prefer a synchronous call or simple fixed pipeline when broker/schema/replay/reconciliation machinery adds no material value, strict global ordering cannot be provided, every action requires complete shared context, latency is harmed by asynchronous hops, or side effects cannot be made idempotent or reconciled.

For evaluation, distinguish accepted/rejected/duplicate/stale/dead-letter events; delivery/queue/handler/end-to-end latency; retry and semantic/transient failure rates; ordering/state-conflict incidents; duplicate-side-effect failures; backlog age/throughput/saturation/dropped work; terminal workflow outcomes; cleanup leaks; accepted-result cost; and replay/recovery success.

## Legacy evidence-provenance residual

The legacy source cited AutoGen Core as an established event-driven multi-agent framework and used these exact references:

- [AutoGen Core](https://microsoft.github.io/autogen/stable/index.html)
- [AutoGen agent runtime environments](https://microsoft.github.io/autogen/stable/user-guide/core-user-guide/core-concepts/architecture.html)
- [AutoGen messages and communication](https://microsoft.github.io/autogen/stable/user-guide/core-user-guide/framework/message-and-communication.html)

Preserve these exact framework references until the selected event-driven learning owner is materialized and their current/historical evidence disposition is verified.

These event-specific pedagogical, operational, and evidence fragments remain migration source material until their exact learning owner is ready.
