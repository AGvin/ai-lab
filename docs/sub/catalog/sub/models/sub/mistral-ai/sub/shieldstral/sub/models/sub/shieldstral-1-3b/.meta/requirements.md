# Documentation Requirements

## Requirements

- Render the standard entity-relations block from the validated current-entity projection.

- Identify Shieldstral 1.0 3B as the released policy-adaptive multimodal safety classifier introduced on 2026-08-04; keep the marketing name separate from the documented 3.8B total parameter count.
- Preserve its source-backed role as a safety classifier for conversational AI inputs and outputs, including supported moderation categories only where current first-party sources define them.
- Preserve model architecture/base-model lineage, license, context length, prompting/classification contract, and deployment guidance only from current official release/model-card evidence.
- Keep benchmark results and comparisons scoped to their evaluated datasets, versions, prompts, and baselines rather than treating them as timeless safety guarantees.
- Keep hosted aliases, quantized artifacts, and service-specific moderation routes outside the trained-model identity.

## Validation

- The model is not conflated with Mistral's hosted moderation service or with generic guardrail concepts.
- Safety-classification capability is not described as deterministic prevention of harmful model behavior.
- Mutable availability and performance claims remain freshness-sensitive.

## Source-backed profile

- Required reader orientation: Shieldstral 1.0 3B is Mistral AI’s policy-adaptive text-and-image safety classifier, released on August 4, 2026.
- Preserve this model-scoped fact: The released repository is `mistralai/Shieldstral-1.0-3B`, based on Ministral 3 3B Base with a vision encoder, under Apache 2.0. Its marketed 3B name is retained; the docs list 3.8B total parameters. [Shieldstral 1.0 3B weights and limitations](https://huggingface.co/mistralai/Shieldstral-1.0-3B) [Shieldstral 1.0 model card](https://docs.mistral.ai/models/shieldstral-1-0)
- Preserve this model-scoped fact: A natural-language policy question and the content to classify produce yes/no logits and a continuous score. The documented training range is 32K tokens. [Shieldstral 1.0 3B weights and limitations](https://huggingface.co/mistralai/Shieldstral-1.0-3B)

## Operational and interpretation boundaries

- Explain this boundary: Mistral documents self-hosting only, with no hosted Mistral API endpoint. Its model page labels the release public preview. [Self-hosted policy moderation with Shieldstral](https://docs.mistral.ai/resources/cookbooks/mistral-moderation-shieldstral_policy_moderation) [Shieldstral 1.0 model card](https://docs.mistral.ai/models/shieldstral-1-0)
- Explain this boundary: Thresholds are application policy. Mistral reports uneven language/domain coverage and reduced reliability on obfuscated inputs or long documents; classification cannot guarantee prevention of harmful behavior. [Shieldstral 1.0 3B weights and limitations](https://huggingface.co/mistralai/Shieldstral-1.0-3B)

- Keep source-reported capabilities distinct from application-level correctness, authorization and measured deployment performance.
