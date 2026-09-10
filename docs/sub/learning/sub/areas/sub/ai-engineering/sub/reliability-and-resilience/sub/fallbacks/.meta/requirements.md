# Documentation Requirements

## Requirements

- Teach Fallbacks as alternate model/provider/mode routes that are activated only when a defined failure condition occurs and the alternate route still satisfies the minimum workflow contract.
- Verify substitution eligibility for the dimensions that matter to the workflow: input/output modalities, usable context/output limits, structured-output/schema behavior, required tool interfaces, latency/cost constraints, and applicable data-handling, licensing, and provider-boundary requirements.
- A reachable second model or endpoint is not automatically an eligible fallback.
- Test fallback routes using the same relevant acceptance contracts and failure cases as the primary route, including prompt/schema/tool compatibility where material.
- Keep concrete model portfolio and escalation choices with Model Selection and mutable provider/service availability with current evidence owners.
- Do not use fallback success to hide a persistent primary-path defect or silently change required application constraints.

## Validation

- Fallback eligibility is explicit and testable.
- Alternate routes are not assumed behaviorally interchangeable.
- A provider/deployment boundary change is visible in the eligibility decision rather than implicit.
