# Documentation Requirements

## Requirements

- Render the standard entity-relations block from the validated current-entity projection.

- Identify Mistral Moderation 2 as the GA v26.03 hosted moderation model with 128K context and first-party jailbreaking-detection support.
- Preserve multilingual/long-conversation moderation claims and supported categories only at exact first-party model scope.
- Treat pricing, categories, API behavior, context, lifecycle, and replacement guidance as freshness-sensitive.

## Validation

- Membership resolves to Mistral Moderation.

## Source-backed profile

- Required reader orientation: Mistral Moderation 2 is Mistral AI’s hosted text-moderation release identified as `mistral-moderation-2603`.
- Preserve this model-scoped fact: The model card lists GA Premier access, a 128K-token context and jailbreak classification for multilingual and multi-turn text. [Mistral Moderation 2 model card](https://docs.mistral.ai/models/mistral-moderation-26-03)

## Operational and interpretation boundaries

- Explain this boundary: The moderation API returns policy-category scores. Guardrail thresholds and the decision to block, review or allow content are application configuration, not a guarantee of safety. [Moderation scores and guardrail thresholds](https://docs.mistral.ai/studio/conversations/moderation)
- Explain this boundary: Keep its versioned policy categories separate from older 2411 categories and from Shieldstral’s supplied-policy text-and-image classification contract. [Moderation scores and guardrail thresholds](https://docs.mistral.ai/studio/conversations/moderation)

- Keep source-reported capabilities distinct from application-level correctness, authorization and measured deployment performance.
