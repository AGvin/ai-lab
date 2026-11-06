# Documentation Requirements

## Requirements

- Present Mistral API as Mistral AI's direct hosted API service for invoking Mistral models and supported API-native capabilities.
- Keep concrete Mistral model families, OCR/embedding/moderation models, Mistral Studio, Vibe, agent/workspace products, SDKs, and self-hosted/open-weight artifacts with their canonical owners.
- Treat endpoint inventory, model availability, SDKs, authentication, pricing, rate limits, batch/file/fine-tuning behavior, API versions, deprecations, regions, and beta/GA state as freshness-sensitive.
- Do not treat Mistral Studio's broader developer-console/asset surface as identical to the API service merely because Studio manages API keys and model access.

- Reconcile the reader with the source-backed identity, access and interpretation context in canonical `entity.identity_note`.
- Render the standard `entity-relations` block from the validated current-entity relation projection.

## Validation

- Mistral API remains the direct hosted model-access service rather than Mistral Studio or a model family.
- Mutable API capability/lifecycle claims remain source-scoped.
- Producer provenance resolves to Mistral AI.

## Scoped original-source qualification — 2026-11-06

- Mistral API is Mistral AI's direct hosted model API with separately documented chat, embeddings, OCR, audio, files and batch endpoints; developer Studio, Vibe and downloadable/self-hosted models are separate product or deployment identities. The API reference labels preview/beta capability groups, so endpoint availability and stability are version-scoped.
- Do not assume a Mistral model's open weights, Studio console privileges or beta agent endpoints are automatically available under any direct API key or region.
- Verified first-party source 1: https://docs.mistral.ai/api/
- Verified first-party source 2: https://docs.mistral.ai/api/endpoint/models
- This bounded source qualification does not establish a full freshness audit, independently validated runtime, legal/model-license clearance, current pricing or entitlements, global schema/cache/CI/render or final publication.
