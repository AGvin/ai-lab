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
