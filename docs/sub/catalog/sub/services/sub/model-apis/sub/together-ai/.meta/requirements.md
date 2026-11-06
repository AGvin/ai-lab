# Documentation Requirements

## Requirements

- Identify Together AI as Together Computer, Inc.'s hosted model and inference service, including managed API access and deployment options for AI models.
- Preserve the distinction between Together AI service identity and the independent authors, licenses, and intrinsic properties of models served through the platform.
- Preserve the current data-path boundary for third-party models at a stable level: Together documentation states that supported third-party models run on Together infrastructure rather than forwarding inference requests to the model author; re-verify this mutable service behavior before expanding it.
- Preserve the current default data-handling boundary at a stable level: inputs and outputs are not stored by default, with account/configuration and enterprise controls affecting behavior; do not turn this into an unconditional future guarantee.
- Keep exact model inventory, deployment modes, pricing, throughput, SLAs, regions, retention controls, and other mutable hosted state source-backed and time-scoped when expanded.
- Render the standard `entity-relations` block from validated current-entity relations.
- Include current official documentation, Privacy Policy, and Terms of Service references.

## Validation

- The profile remains a hosted model/inference service and does not duplicate model identities.
- Third-party model authors are not described as receiving Together-hosted inference traffic unless current first-party evidence says so.
- Data-handling claims preserve configuration and service-version boundaries rather than overstating zero retention.
- The `produces` / `produced-by` relation pair resolves consistently to Together Computer, Inc.

## Scoped original-source qualification — 2026-11-06

- Together AI documents both serverless inference and dedicated-model endpoints. Dedicated-model inference uses reserved hardware and capacity-bounded scaling/pricing; the public API may be shared between modes, but SLA, hardware tenancy, model support and throughput remain mode- and contract-specific.
- Do not infer default zero retention, universal third-party provider isolation, reserved capacity or performance results without checking the exact Together deployment and data-processing agreement.
- Verified first-party source 1: https://docs.together.ai/docs/dedicated-endpoints/overview
- Verified first-party source 2: https://docs.together.ai/docs/serverless/overview
- This accepts only the existing service identity and bounded source facts, not a full freshness/license/ownership audit, independent benchmarks, permission to process sensitive data, runtime tests, complete schema/cache/CI/render or final delivery.
