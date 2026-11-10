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

## Scoped original-source qualification — 2026-11-06

- Fireworks AI offers managed serverless inference and dedicated GPU deployments. The provider describes serverless as per-token and dedicated autoscaling as workload/instance-oriented; capabilities, isolation, SLAs, and processing paths differ by mode.
- First-party retention documentation describes default Zero Data Retention for open models, with prompt caching held in volatile memory and metadata logged. Importantly, **Responses API requests using `store=true` (the documented default) retain conversation data for up to 30 days**; `store=false` is the documented opt-out. Do not imply unconditional zero retention for every endpoint.
- Original model authors retain model identity, licensing, and training provenance; deployment availability, latency and data processing terms need verification for each configuration.
- Verified first-party source 1: https://docs.fireworks.ai/getting-started/introduction
- Verified first-party source 2: https://docs.fireworks.ai/guides/security_compliance/data_handling
- This accepts bounded source facts only, not a full freshness/license/ownership audit, independent benchmarks, permission to process sensitive data, runtime tests, complete schema/cache/CI/render or final delivery.
