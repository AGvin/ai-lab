# Documentation Requirements

## Requirements

- Use the reader-facing title `Fallback Architectures` and introduce legacy `fallback models` as one common implementation form.
- Define a fallback architecture as a system-level reliability/degradation pattern that selects an explicitly allowed alternative behavior or execution path when a preferred path is unavailable, failing, rejected, timed out, capacity-limited, policy-ineligible, or otherwise unable to satisfy the current request's requirements.
- Keep the concept broader than a second model endpoint. Fallback actions can include another model/provider/deployment, a lower-capability deterministic implementation, cached/default data, reduced-feature mode, queued/deferred processing, human escalation, safe refusal/fail-closed behavior, or another bounded alternative appropriate to the operation.
- Distinguish fallback from retry. A retry attempts the same logical operation/path again under an expectation of transient recovery; a fallback changes the strategy/path or response contract. Retry and circuit breaking can precede or combine with fallback, but unbounded retry is not a fallback architecture.
- Distinguish fallback from normal model routing. Routing selects among healthy/eligible alternatives as part of ordinary policy; fallback is specifically a degraded/recovery path triggered because the preferred path cannot or should not continue. A system can implement fallback through the same router infrastructure while retaining separate semantics.
- Define fallback triggers explicitly: timeout, error class, rate/capacity signal, circuit-breaker state, unavailable capability, validation/schema failure, policy rejection, quality/uncertainty threshold, budget/deadline exhaustion, or operator intervention as applicable. Do not treat every failure identically.
- Preserve hard authorization, privacy, residency, retention, licensing, trust-boundary, safety, and data-handling constraints across fallback paths. Availability must not silently authorize sending protected data or privileged actions to a less trusted provider/environment.
- Treat fail-closed behavior as a valid fallback where no alternate path satisfies mandatory constraints. Returning an explicit unavailable/degraded response can be safer and more correct than using an ineligible lower-trust/lower-capability path.
- Define the degraded service contract. Alternate models/paths can differ in modality, context length, schema/tool support, output format, quality, safety/refusal behavior, language support, latency, and consistency; callers/users should not assume transparent equivalence when those differences are material.
- Validate compatibility at the system boundary. Prompts/templates, structured-output schemas, tool definitions, authentication, context/state serialization, tokenization, request size, and result parsing can require path-specific handling before an alternate model/service is safe to use.
- Explain that fallback chains must be bounded and cycle-safe. Repeated fallback across multiple failing dependencies can create retry storms, cascading load, high cost, long tail latency, duplicate side effects, or loops unless attempts/deadlines/budgets and recovery state are controlled.
- Coordinate side-effecting operations with idempotency/state/recovery semantics. If a primary path may have partially completed a tool/action before failing, a fallback must not repeat or conflict with the side effect without deterministic reconciliation.
- Use circuit breakers, health/availability signals, rate/capacity indicators, or other dependency-state mechanisms as possible trigger inputs rather than universal requirements. A fallback should avoid continuing to hammer a dependency known to be persistently unhealthy.
- Test fallback paths regularly under representative failure/degradation scenarios. A configured alternate path that is stale, incompatible, unprovisioned, unlicensed, rate-limited, or never exercised is not reliable merely because configuration exists.
- Observe primary failures and fallback activations separately. Fallback success must not hide persistent primary-path degradation; record trigger reason, selected alternative, outcome, user-visible degradation, policy decision, and recovery transition at an appropriate privacy-safe level.
- Explain recovery/re-entry criteria where applicable. Returning to the preferred path after an outage or degraded condition can require health checks, circuit-breaker half-open probes, cooldowns, capacity restoration, or operator approval rather than switching back on every isolated success.
- Keep concrete fallback model/provider lists, current compatibility/availability, retry counts/timeouts, circuit thresholds, cached/default values, prices, incident responses, service-specific degradation policies, and deployment recommendations with their applicable catalog, project, evidence, reliability, or decision owners.
- Use the canonical entity references as research inputs for retry-versus-circuit-breaker-versus-fallback distinctions and graceful-degradation boundaries when reader-facing rendering is activated.

## Validation

- Fallback architectures are not reduced to a second model/API key or conflated with unbounded retry.
- Normal routing and failure/degradation-triggered fallback are distinguished even when they share implementation infrastructure.
- Fallback paths cannot relax mandatory authorization, privacy, residency, trust, or safety constraints merely to preserve availability.
- Safe refusal/fail-closed behavior is supported when no compliant alternative exists.
- Alternate paths are not assumed equivalent in modality, schema/tool support, context, quality, or safety behavior.
- Fallback chains are bounded/cycle-safe and side-effecting operations account for partial completion/idempotency.
- Concrete providers/models, thresholds, retry policies, incident values, and deployment settings remain outside the reusable fallback-architecture owner.
