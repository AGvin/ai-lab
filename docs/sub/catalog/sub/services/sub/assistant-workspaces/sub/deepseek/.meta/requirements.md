# Documentation Requirements

## Requirements

- Present DeepSeek as DeepSeek's hosted end-user assistant service spanning official web and mobile applications with chat, reasoning, web search, file/document input and current model access.
- Keep DeepSeek trained-model identities, DeepSeek API Platform, DeepSeek Harness, open-source kernel/runtime libraries and third-party model-hosting surfaces separate from the end-user assistant.
- Treat web/app model selection, Expert/Thinking modes, search/file capabilities, account/sync behavior, plan/pricing state, regional availability, data handling and current model rollout as freshness-sensitive.
- Preserve the official web/app product continuity even when the default model changes; do not rename the service after the currently routed model.
- Render the standard `entity-relations` block from validated current-entity relations.

## Validation

- DeepSeek remains a hosted assistant service rather than the DeepSeek model family or API.
- Current model rollout in web/app is not generalized into permanent service identity.
- Producer provenance resolves bidirectionally to DeepSeek.

## Scoped original-source qualification — 2026-11-07

- DeepSeek's hosted assistant on web/mobile is separate from DeepSeek's trained models and API Platform; a default-model update does not create a new hosted assistant identity.
- First-party product surface: https://chat.deepseek.com/
- Credits only the existing service identity and source boundary; no independent runtime, privacy, security, legal, clean-pass or final-gate verification.
