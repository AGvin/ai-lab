# Documentation Requirements

## Requirements

- Identify Fireworks AI as Fireworks.ai, Inc.'s hosted inference/model-serving service with serverless and dedicated deployment surfaces.
- Preserve the distinction between Fireworks AI service identity and the independent authors, licenses, and intrinsic properties of models served through it.
- Preserve the current deployment boundary: serverless and dedicated deployments have different availability, isolation, model-customization, performance, and service-level characteristics; do not generalize one mode's guarantees to the other.
- Preserve data-handling claims only at their documented scope. Current first-party policy states that prompts/training data/API inputs are not used for training without explicit opt-in and documents zero-data-retention behavior for open models with exceptions; re-verify mutable policy details before expanding them.
- Keep exact model inventory, pricing, deployment hardware, SLA/availability, retention exceptions, throughput, and other mutable service state source-backed and time-scoped when added.
- Render the standard `entity-relations` block from validated current-entity relations.
- Include current official documentation, Privacy Notice, and Terms of Service references.

## Validation

- The profile remains a hosted model/inference service and does not duplicate third-party model identities.
- Serverless best-effort behavior is not described as having dedicated-deployment guarantees unless current evidence supports it.
- Data-handling claims preserve current opt-in and exception boundaries rather than becoming unconditional guarantees.
- The `produces` / `produced-by` relation pair resolves consistently to Fireworks.ai, Inc.
