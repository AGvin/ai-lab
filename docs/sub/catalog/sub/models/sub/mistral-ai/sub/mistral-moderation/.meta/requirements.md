# Documentation Requirements

## Requirements

- Render the standard entity-relations block from the validated current-entity projection.

- Identify Mistral Moderation as Mistral AI's hosted moderation model line and materialize Mistral Moderation 2 as the current GA Premier release.
- Keep Shieldstral as a separate open multimodal safety-classifier family: shared moderation purpose does not make the hosted Mistral Moderation line an alias of Shieldstral.
- Keep the deprecated 24.11 Mistral Moderation predecessor historical unless lifecycle context requires it.
- Treat moderation categories, jailbreak detection, multilingual behavior, context, pricing, lifecycle, and API surface as freshness-sensitive.

## Validation

- Producer provenance resolves to Mistral AI.
- Mistral Moderation 2 and Shieldstral retain distinct model identities and deployment/licensing boundaries.

## Source-backed profile

- Required reader orientation: Mistral Moderation is Mistral AI’s hosted text-moderation model line.
- Preserve this model-scoped fact: The represented Moderation 2 release scores text against versioned moderation categories, including jailbreak-related content. [Mistral Moderation 2 model card](https://docs.mistral.ai/models/mistral-moderation-26-03) [Moderation scores and guardrail thresholds](https://docs.mistral.ai/studio/conversations/moderation)

## Operational and interpretation boundaries

- Explain this boundary: Shieldstral is a separate open-weight text-and-image classifier driven by a supplied policy. Category scores and thresholds are fallible inputs to an application’s policy decisions. [Shieldstral 1.0 3B weights and limitations](https://huggingface.co/mistralai/Shieldstral-1.0-3B) [Moderation scores and guardrail thresholds](https://docs.mistral.ai/studio/conversations/moderation)

- Keep source-reported capabilities distinct from application-level correctness, authorization and measured deployment performance.
