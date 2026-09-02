# Fallback Models

Legacy residual retained for model-substitution eligibility, compatibility, trust-boundary, and degraded-service guidance that is intentionally outside the reusable Reliability and Resilience concept and outside concrete model-selection recommendations.

> **Migration note:** Fallback/degraded-mode recovery as a general reliability mechanism is already preserved in `docs/sub/concepts/sub/ai-engineering/sub/reliability-and-resilience/`. The canonical model-selection owner explicitly keeps provider failover, infrastructure recovery, and service lifecycle outside model-selection ownership. The remaining material below therefore stays here until its exact system-design, deployment/reliability, governance, or decision owner is verified.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Substitution-eligibility residual

A fallback model is useful only when it can satisfy the minimum contract required by the specific workflow. Before substitution, verify the dimensions that matter to that route, such as:

- input and output modalities;
- usable context and output limits;
- structured-output or schema behavior;
- required tool/function interfaces;
- safety or policy behavior;
- latency, cost, and deployment constraints;
- privacy, data-location, licensing, and provider trust boundaries.

A second reachable model or API endpoint is not automatically an eligible fallback.

## Operational residual

Fallback activation can respond to provider/service outages, validation failure, capability gaps, policy/data-boundary constraints, or another explicitly defined failure condition. Avoid indefinite retries before fallback and avoid using fallback success to hide a persistent primary-path defect.

Test fallback paths with the same relevant contracts and failure cases used by the workflow, including prompt/schema/tool compatibility. When the alternate route materially reduces quality, modality support, context, or another user-visible capability, communicate the degraded mode where the product/workflow requires it.

Do not silently move sensitive data to a provider, region, or deployment environment that is less trusted or otherwise ineligible merely to preserve availability.

These model-substitution and degraded-service constraints remain migration source material until their exact system-design, deployment/reliability, governance, or decision owners are verified.
