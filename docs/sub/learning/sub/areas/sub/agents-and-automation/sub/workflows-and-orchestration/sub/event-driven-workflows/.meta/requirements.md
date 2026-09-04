# Documentation Requirements

## Requirements

- Teach event-driven agent workflows as bounded agents/services coordinated through typed events delivered by a runtime, broker, queue, or message bus, while keeping authoritative workflow state explicit when replay, reconciliation, or audit requires a durable source of truth.
- Define an event contract with the fields needed by the use case, including event/schema version, stable event identity, producer/version, workflow/task/correlation/causation identities, occurrence/publication time, partition/ordering key, payload/artifact references, data classification/permissions, expected consumers, delivery/retention semantics, expiry, and replay policy.
- Treat event payload content as untrusted handler input; events should carry data/contracts rather than hidden executable control logic.
- Define each handler/agent contract explicitly: subscriptions and accepted versions, filtering/authorization, required state/artifacts, input/output schema, model/tools/permissions/side effects, idempotency/deduplication scope, timeout/retry/dead-letter behavior, emitted events/terminal results, and concurrency/ordering/resource assumptions.
- Reject unknown/incompatible event-schema versions rather than guessing how to process them.
- Teach delivery semantics explicitly: at-most-once, at-least-once, or effectively-once through idempotency/deduplication. Do not infer global ordering where only partition/key ordering exists.
- Make clear that broker-level `exactly once` claims do not guarantee exactly-once external side effects. External APIs, files, databases, tools, and model calls can still duplicate work after timeout, retry, or ambiguous acknowledgement.
- Teach stable event/operation identities, prior-processing checks, compare-and-set/reservation where appropriate, provider idempotency, transactional/outbox-style result+event persistence, and reconciliation of ambiguous outcomes before retrying consequential effects.
- Record correlation/causation and define conflict rules for out-of-order or stale events, late cancellation, retries older than a newer state version, concurrent updates, clock differences, and expired workflows. Prefer state/sequence/generation versions over wall-clock assumptions where correctness depends on ordering.
- Design backpressure explicitly for model workloads: queue/concurrency limits, tenant/workflow quotas, priority/admission, maximum event age, batching/capacity assumptions, shedding/delay/fail-closed behavior, and alert thresholds. Bursts must not create unbounded model/API cost, accelerator allocation, or context growth.
- Classify failures before retrying: transport/provider transients, capacity/rate limits, malformed/unsupported events, stale/unauthorized state, semantic model failure, deterministic validation failure, and ambiguous irreversible effects require different handling.
- Use bounded backoff only for eligible failures. Poison/exhausted work requires a dead-letter/quarantine path with ownership, reason, attempts, cost exposure, and a safe replay procedure; repeated semantic model failure normally calls for rerouting, human review, or terminal failure rather than identical redelivery.
- Teach replay as a controlled operation: validate handler/version compatibility, suppress or make external effects idempotent, define schema migration, prevent reintroduction of expired secrets/permissions, and re-check whether current policy still permits historical input.
- Account for model nondeterminism during replay. Pin exact model/runtime/prompt/tool artifacts and parameters when reproducibility matters, and preserve accepted terminal artifacts/decisions instead of assuming replay recreates identical outputs.
- Define workflow terminal state explicitly through expected task/branch completion, correlation/join rules, timeout/missing-event behavior, cancellation propagation, success/partial/failure/expired states, artifact/review gates, and resource/billing cleanup. An idle queue is not proof of completion.
- Teach security boundaries: authenticate producers, authorize event types/targets, validate schemas/sizes/artifact references/signatures where required, preserve tenant/environment/data-class isolation, avoid reusable credentials/unnecessary personal data in events, restrict handler tools/side effects independently from prompt content, and apply audit/deletion policy across brokers/logs/DLQs/artifacts.
- Teach pattern fit: use event-driven workflows for genuinely asynchronous/distributed, long-running, callback, monitoring/incident, hosted-job/resource-lifecycle, high-volume independent, or cross-process/language/machine work where decoupling is valuable. Prefer synchronous calls or simple pipelines when broker/schema/replay/reconciliation machinery adds no material value.
- Evaluate accepted/rejected/duplicate/stale/dead-letter events; delivery/queue/handler/end-to-end latency; retry and semantic/transient failures; ordering/state-conflict incidents; duplicate-side-effect failures; backlog age/throughput/saturation/dropped work; terminal outcomes; cleanup leaks; accepted-result cost; and replay/recovery success.
- Use AutoGen Core/runtime/message-and-communication references only as framework evidence. Keep framework-specific APIs and mutable implementation behavior source-backed rather than turning them into generic event-driven truth.
- Link generic distributed-system, idempotency, retry, recovery, observability, and capacity semantics to their AI Engineering/canonical concept owners rather than duplicating them here.

## Validation

- Event delivery semantics are not conflated with end-to-end side-effect guarantees.
- Queue idleness is never used as the sole workflow-completion condition.
- Replay examples account for external side effects, schema/version drift, permissions, and model nondeterminism.
- Retry behavior distinguishes semantic/deterministic failures from eligible transient failures.
- Framework examples do not become timeless API or protocol facts.
