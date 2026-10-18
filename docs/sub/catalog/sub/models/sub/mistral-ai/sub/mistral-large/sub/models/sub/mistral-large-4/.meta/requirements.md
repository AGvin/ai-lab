# Documentation Requirements

## Requirements

- Identify Mistral Large 4 as a distinct released trained-model identity from Mistral AI.
- Render the standard entity-relations block from validated canonical metadata.
- Keep model-specific specifications, artifact representations and hosted access context distinct.

## Validation

- The entity ID matches the canonical path and reciprocal relations resolve.
- Claims stay at the documented release scope, and generated output is not treated as a correctness or security guarantee.

## Source-backed profile

- Required reader orientation: Mistral Large 4 is Mistral AI’s multimodal Mixture-of-Experts model released through the API in public preview on October 6, 2026.
- Preserve this model-scoped fact: Mistral reports 1.05T total parameters, 52B active parameters, a 1.6B vision encoder and a 1M-token context. [Mistral Large 4 public-preview model card](https://docs.mistral.ai/models/mistral-large-4-0)
- Preserve this model-scoped fact: The documented API identifier is `mistral-large-4`. Its launch announcement says downloadable weights are still forthcoming. [Mistral model changelog](https://docs.mistral.ai/resources/changelogs)

## Operational and interpretation boundaries

- Explain this boundary: Public preview permits silent updates and does not guarantee a subsequent GA release. Treat this as released API access, without assuming an immutable downloadable checkpoint or an already available open-weight license. [Serverless model lifecycle policy](https://docs.mistral.ai/inference/model-lifecycle) [Mistral model changelog](https://docs.mistral.ai/resources/changelogs)
- Explain this boundary: Tool calling and structured output are supported interfaces; the application still validates outputs and authorizes execution. [Mistral Large 4 public-preview model card](https://docs.mistral.ai/models/mistral-large-4-0) [Function-calling contract](https://docs.mistral.ai/studio/conversations/function-calling)

- Keep source-reported capabilities distinct from application-level correctness, authorization and measured deployment performance.
