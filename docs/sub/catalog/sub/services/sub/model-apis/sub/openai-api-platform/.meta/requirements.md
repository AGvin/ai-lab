# Documentation Requirements

## Requirements

- Present OpenAI API Platform as OpenAI's hosted developer/model-access service for programmatic use of OpenAI models and API-native generation/tool surfaces.
- Preserve the direct model-access/service boundary around current Responses, model invocation, streaming, batch, embeddings, image/audio/realtime, files/vector-store and related API capabilities only as supported by current OpenAI developer documentation.
- Keep concrete GPT, GPT Image, Realtime, Transcribe, TTS, embedding, moderation, and other trained-model identities with Model Reference; API availability does not make the service the model producer identity.
- Keep OpenAI Agents API as the separately canonical managed agent-infrastructure service, OpenAI Agents SDK as software, ChatGPT as assistant workspace, and Codex as agent product; shared authentication/billing does not collapse those identities.
- Treat endpoint inventory, API-version/migration guidance, supported models, tools, SDKs, pricing, quotas, rate limits, data controls, regions, service tiers, and deprecations as freshness-sensitive.
- Preserve current default/recommended API primitives as mutable service facts rather than permanent protocol standards.
- Track the **2026-10-06 beta Decisions API (`v1/decisions`, initially `gpt-6-luna`)** as an endpoint/product feature within OpenAI API Platform, distinct from the Responses API and from any independently trained model identity. Keep beta stability, schema, latency claims, supported models, and rollout lifecycle attributed to dated primary sources rather than assuming general availability.
- Record the **2026-10-08 GPT-6.1 Sol Ultrafast (`service_tier: "ultrafast"`)** rollout as a model-specific processing/service-tier option in the Responses API, not as a new hosted model or separately operated service. Current pricing, region/data-residency claims, entitlement and tier/model compatibility must be verified from current official docs.
- Treat the **2026-10-07 `chat-latest` alias refresh** as a mutable service routing/snapshot update, not a new concrete trained-model identity; resolve the active snapshot before making version-specific claims.
- Use the official API changelog at https://developers.openai.com/api/docs/changelog as dated primary evidence for these October 2026 changes.

## Validation

- OpenAI API Platform remains a hosted model/developer API service rather than a trained-model family or ChatGPT.
- Managed agent infrastructure and SDKs are not duplicated inside this service identity.
- Producer provenance resolves bidirectionally to OpenAI.
