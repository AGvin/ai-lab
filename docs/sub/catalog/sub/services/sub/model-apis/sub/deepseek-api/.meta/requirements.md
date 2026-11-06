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

## Scoped original-source qualification — 2026-11-06

- DeepSeek's original developer documentation describes OpenAI-compatible, Anthropic-compatible and Responses API forms. Its Responses guide distinguishes supported parameters and explicitly describes stateless responses requiring the caller to supply prior conversation history.
- Current DeepSeek service aliases can be rerouted after original model retirement: deepseek-flash is documented as serving a later DeepSeek V4.1 Flash release. An alias, compatibility route or agent-tool integration is not an additional immutable trained-model identity; unsupported tool and input capabilities must be checked endpoint by endpoint.
- Verified first-party source 1: https://api-docs.deepseek.com/guides/responses_api/
- Verified first-party source 2: https://api-docs.deepseek.com/api_samples/chat_python_v3.1_terminus/
- This accepts only service-scoped source identity and documented capability boundaries; it is not an exhaustive freshness audit, authenticated endpoint test, independent compliance/ownership review, global schema/cache/CI/render verification, clean pass or final-delivery gate.
