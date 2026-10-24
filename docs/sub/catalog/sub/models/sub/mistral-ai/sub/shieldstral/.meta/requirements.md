# Documentation Requirements

## Requirements

- Render the standard entity-relations block from the validated current-entity projection.

- Identify Shieldstral as Mistral AI's model family for safety classification and guardrailing of conversational AI inputs and outputs.
- Link the canonical Mistral AI producer and materialized concrete Shieldstral models.
- Keep moderation policy, supported categories, deployment/runtime guidance, and measured safety performance source-backed and scoped to the applicable concrete release.
- Keep Shieldstral model identity distinct from hosted moderation APIs, generic guardrail concepts, and third-party safety frameworks.

## Validation

- Shieldstral is not represented as a generic safety methodology or as a hosted service identity.
- Model-specific architecture, license, context, and classification behavior remain on concrete model pages.
- Safety benchmark results are not generalized beyond the evaluated release and protocol.

## Source-backed profile

- Required reader orientation: Shieldstral is Mistral AI’s family of policy-adaptive multimodal safety classifiers.
- Preserve this model-scoped fact: A supplied natural-language policy defines the question answered about text or images. The released 1.0 checkpoint uses a yes/no score instead of a fixed hosted moderation taxonomy. [Shieldstral release](https://mistral.ai/news/shieldstral/)

## Operational and interpretation boundaries

- Explain this boundary: The documented release is self-hosted; it is not an alias for Mistral Moderation. Policy wording, thresholds and deployment testing determine how classification is used. [Self-hosted policy moderation with Shieldstral](https://docs.mistral.ai/resources/cookbooks/mistral-moderation-shieldstral_policy_moderation)

- Keep source-reported capabilities distinct from application-level correctness, authorization and measured deployment performance.
