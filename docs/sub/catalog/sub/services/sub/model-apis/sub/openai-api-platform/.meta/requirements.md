# Documentation Requirements

## Requirements

- Present OpenAI API Platform as OpenAI's hosted developer/model-access service for programmatic use of OpenAI models and API-native generation/tool surfaces.
- Preserve the direct model-access/service boundary around current Responses, model invocation, streaming, batch, embeddings, image/audio/realtime, files/vector-store and related API capabilities only as supported by current OpenAI developer documentation.
- Keep concrete GPT, GPT Image, Realtime, Transcribe, TTS, embedding, moderation, and other trained-model identities with Model Reference; API availability does not make the service the model producer identity.
- Keep OpenAI Agents API as the separately canonical managed agent-infrastructure service, OpenAI Agents SDK as software, ChatGPT as assistant workspace, and Codex as agent product; shared authentication/billing does not collapse those identities.
- Treat endpoint inventory, API-version/migration guidance, supported models, tools, SDKs, pricing, quotas, rate limits, data controls, regions, service tiers, and deprecations as freshness-sensitive.
- Preserve current default/recommended API primitives as mutable service facts rather than permanent protocol standards.

## Validation

- OpenAI API Platform remains a hosted model/developer API service rather than a trained-model family or ChatGPT.
- Managed agent infrastructure and SDKs are not duplicated inside this service identity.
- Producer provenance resolves bidirectionally to OpenAI.
