# Documentation Requirements

## Requirements

- Present DeepSeek API as DeepSeek's direct hosted developer/model-access service for current DeepSeek model releases.
- Preserve current OpenAI-compatible, Anthropic-compatible, and Responses API surfaces only as current service interfaces; do not convert protocol compatibility into producer identity.
- Keep concrete DeepSeek V4/V4.1 and later trained-model identities with Model Reference and the DeepSeek web/app workspace separate.
- Treat active model aliases/routing, endpoint compatibility, multimodal support, pricing, context/output limits, caches, rate limits, availability, deprecation/retirement, and API feature support as freshness-sensitive.
- Preserve current lifecycle semantics where legacy aliases may temporarily route to replacement models; routing compatibility is not a new trained-model identity.

## Validation

- DeepSeek API remains a hosted service rather than the DeepSeek model family or web assistant.
- Deprecated/compatibility aliases are not frozen as durable model identities.
- Producer provenance resolves to DeepSeek.
