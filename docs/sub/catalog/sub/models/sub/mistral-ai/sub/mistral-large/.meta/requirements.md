# Documentation Requirements

## Requirements

- Identify Mistral Large as Mistral AI's large general-purpose model family.
- Render the standard entity-relations block and preserve the distinct GA/open-weight and public-preview/API boundaries of represented releases.
- Preserve multimodal, MoE, reasoning/agentic, context, benchmark, deployment, license, and provider claims only at the concrete-model scope.

## Validation

- Producer provenance resolves to Mistral AI.
- Family identity is not conflated with Mistral Medium, Small, or Ministral.

## Source-backed profile

- Required reader orientation: Mistral Large is Mistral AI’s large general-purpose multimodal model family.
- Preserve this model-scoped fact: Large 3 is a GA release with published Apache 2.0 weights. Large 4 is a released public-preview API model whose launch notice still describes weights as forthcoming. [Mistral Large 3 model card](https://docs.mistral.ai/models/mistral-large-3-25-12) [Mistral Large 4 public-preview model card](https://docs.mistral.ai/models/mistral-large-4-0) [Mistral model changelog](https://docs.mistral.ai/resources/changelogs)

## Operational and interpretation boundaries

- Explain this boundary: Model generation, parameter counts, context and weight availability remain member-specific. A public-preview listing does not supply GA stability or an immutable weight artifact. [Serverless model lifecycle policy](https://docs.mistral.ai/inference/model-lifecycle)

- Keep source-reported capabilities distinct from application-level correctness, authorization and measured deployment performance.
