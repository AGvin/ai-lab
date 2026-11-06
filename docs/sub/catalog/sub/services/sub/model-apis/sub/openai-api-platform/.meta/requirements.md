# Documentation Requirements

## Requirements

- Present OpenAI API Platform as OpenAI's hosted developer/model-access service for programmatic use of OpenAI models and API-native generation/tool surfaces.
- Preserve the direct model-access/service boundary around current Responses, model invocation, streaming, batch, embeddings, image/audio/realtime, files/vector-store and related API capabilities only as supported by current OpenAI developer documentation.
- Keep concrete GPT, GPT Image, Realtime, Transcribe, TTS, embedding, moderation, and other trained-model identities with Model Reference; API availability does not make the service the model producer identity.
- Keep OpenAI Agents API as the separately canonical managed agent-infrastructure service, OpenAI Agents SDK as software, ChatGPT as assistant workspace, and Codex as agent product; shared authentication/billing does not collapse those identities.
- Treat endpoint inventory, API-version/migration guidance, supported models, tools, SDKs, pricing, quotas, rate limits, data controls, regions, service tiers, and deprecations as freshness-sensitive.
- Preserve current default/recommended API primitives as mutable service facts rather than permanent protocol standards.
- Track the **2026-10-06 beta launch and 2026-10-22 general-availability release of the Decisions API (`v1/decisions`, `gpt-6-luna`)** as changes to an API endpoint within OpenAI API Platform, not a new trained-model identity. Attribute dated stability, schema, latency claims, supported models, quota and rollout conditions to each first-party release instead of carrying the original beta status forward.
- Record the **2026-10-08 GPT-6.1 Sol Ultrafast (`service_tier: "ultrafast"`)** rollout as a model-specific processing/service-tier option in the Responses API, not as a new hosted model or separately operated service. Current pricing, region/data-residency claims, entitlement and tier/model compatibility must be verified from current official docs.
- Treat the **2026-10-07 `chat-latest` alias refresh** as a mutable service routing/snapshot update, not a new concrete trained-model identity; resolve the active snapshot before making version-specific claims.
- Use the official API changelog at https://developers.openai.com/api/docs/changelog as dated primary evidence for these October 2026 changes.

## Reader projection

- Render the standard `entity-relations` block from all validated current-entity relations eligible for reader presentation.
- Render the `official-resources` block from canonical references supporting the identity, versioned facts, access context, and stated boundaries of this page.

## Validation

- OpenAI API Platform remains a hosted model/developer API service rather than a trained-model family or ChatGPT.
- Managed agent infrastructure and SDKs are not duplicated inside this service identity.
- Producer provenance resolves bidirectionally to OpenAI.

## Scoped original-source qualification — 2026-11-06

- OpenAI API Platform is OpenAI's hosted model-access API; Responses, the Decisions API, and model-specific service tiers are API capabilities, not new trained-model producer entities. The 2026-10-06 Decisions beta was replaced by general availability on 2026-10-22 for gpt-6-luna, so do not describe its current lifecycle as beta solely from the earlier announcement. The 2026-10-07 chat-latest snapshot is a moving alias, and GPT-6.1 Sol ultrafast is a Responses service tier rather than a separately trained model.
- Pin model, version/route, usage tier and processing/residency policy before integrating. Managed Agents API, SDK, ChatGPT and Codex remain separate from the general hosted API identity, and account access, quotas, prices, data controls and beta features remain mutable.
- Verified first-party source 1: https://developers.openai.com/api/docs
- Verified first-party source 2: https://developers.openai.com/api/docs/changelog
- This source qualification accepts only the existing hosted-service identity and bounded claims. It does not establish full freshness, legal/ownership/license clearance, independent security or performance, authenticated endpoints, complete schema/cache/CI/render, clean pass or final delivery.
