# Documentation Requirements

## Requirements

- Use the reader-facing title `Reliability and Resilience`.
- Define reliability as the ability of an AI-enabled system or component to perform required functions without failure under stated conditions and over the relevant period, and resilience as the ability to withstand adverse events or changes, degrade safely when necessary, and recover acceptable operation. Treat them as related but distinct properties.
- Scope the concept to AI-engineering systems whose failure surface can include model semantic failures, invalid or unsafe model/tool requests, tool/API/network failures, rate/resource limits, validation failures, workflow-state loss, infrastructure faults, and ambiguous external side effects.
- Preserve idempotency as an important reliability property of an operation/effect contract: repeating the same logical operation under the defined idempotency scope does not create additional unintended effects after the intended effect has been applied. Do not create a separate canonical `idempotency` child from the legacy merge source.
- Make clear that idempotency is normally enforced by the tool, service, workflow, or application layer rather than by prompting or model memory. Stable request identities, deduplication records, conditional updates, and state reconciliation are implementation examples rather than universal requirements.
- Explain that not every operation can be made strictly idempotent and that compensation, reconciliation, human intervention, or another recovery strategy can be necessary when effects are irreversible or only partially reversible.
- Preserve retries as bounded re-attempts for failures classified as retryable under the operation contract. Distinguish transient, permanent, partial, and ambiguous failures; a model or workflow must not treat every exception, validation failure, permission denial, invalid request, or unsupported operation as retryable.
- Explain that an unacknowledged request or timeout can leave side-effect state ambiguous. Do not infer that an external action failed to occur merely because its acknowledgement was lost; reconcile authoritative external state or use an idempotency/deduplication contract before retrying consequential writes.
- Explain exponential or otherwise increasing backoff, jitter, attempt limits, retry budgets, server-provided retry guidance, and escalation as common mechanisms for controlling retry amplification without prescribing one universal schedule or numeric policy.
- Explain that retries at several nested layers can multiply load and amplify an outage. Retry ownership and budgets must therefore be coordinated across the complete call/workflow path rather than independently added everywhere.
- Make clear that retrying model generation can produce a different output but does not repair missing evidence, invalid requirements, unavailable capabilities, denied permissions, corrupt state, or another persistent root cause by itself.
- Define failure recovery as broader than retrying: recovery can resume from durable state or checkpoints, switch to a fallback/degraded mode, reconcile an ambiguous side effect, compensate for a completed effect, request human intervention, or terminate safely with enough state/evidence for later continuation.
- Distinguish rollback from compensation. Distributed or external side effects may not support restoring the exact prior world state, and a compensating action can itself fail or have different semantics from true rollback.
- Require recoverable workflows to preserve authoritative execution state and known external effects at meaningful boundaries. Conversation history, generated summaries, or a model's claimed memory are not authoritative ledgers of whether an external operation actually completed.
- Treat deterministic validation failures and safety/authorization failures as explicit workflow state that must be handled or escalated; do not silently continue generation/execution merely because the model can propose another answer.
- Explain that reliability/resilience design requires observability sufficient to distinguish attempts, outcomes, partial effects, terminal states, fallbacks, and recovery actions; the exact logging/tracing implementation remains outside the concept definition.
- Keep concrete provider status codes, retryable-error tables, backoff constants, idempotency-key syntax, state/checkpoint schemas, compensation procedures, fallback-model choices, incident playbooks, and project-specific recovery workflows with their applicable catalog, engineering, learning, evidence, or project owners.
- Use the canonical entity references as research inputs for reliability/resilience, retry amplification, and idempotent-retry boundaries when reader-facing rendering is activated.

## Validation

- The page does not create separate canonical `idempotency`, `retries`, or `failure-recovery` child nodes from the legacy merge sources.
- Reliability and resilience are distinguished rather than used as synonyms.
- A timeout or missing acknowledgement is not treated as proof that a consequential side effect did not occur.
- Retrying is limited to classified/eligible operations and is not presented as a universal response to every failure.
- Model regeneration is not presented as a root-cause fix for invalid requirements, missing data, denied permissions, unsupported actions, or corrupted state.
- Idempotency is not treated as a prompting property or as universally available for every operation.
- Recovery is broader than retries and acknowledges compensation/reconciliation when strict rollback is impossible.
- Conversational/model memory is not treated as authoritative execution state for external side effects.
- Legacy distributed-systems tutorials and concrete retry/recovery recipes remain outside this AI-specific concept owner unless separately selected.
