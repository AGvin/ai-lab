# Documentation Requirements

## Requirements

- Teach Degraded Modes as explicit reduced-capability operation used when the full route is unavailable or ineligible but a smaller contract can still be satisfied safely and usefully.
- Define which capabilities may be reduced, disabled, delayed, or rerouted and which acceptance, policy, data-handling, or safety constraints remain non-negotiable.
- Communicate materially reduced quality, modality support, context, latency, freshness, or other user-visible capability when the product/workflow requires that distinction.
- Do not silently move data or execution to an alternate provider, region, or deployment environment when that route violates the workflow's eligibility constraints.
- Test degraded-mode transitions and recovery back to normal operation rather than treating alternate-route success as sufficient evidence.
- Keep concrete product messaging and current provider availability with their respective product/evidence owners.

## Validation

- Degraded operation has an explicit reduced contract rather than an undefined weaker state.
- Non-negotiable constraints remain enforced during degradation.
- User-visible material capability reduction is not silently presented as normal operation when disclosure is required.
