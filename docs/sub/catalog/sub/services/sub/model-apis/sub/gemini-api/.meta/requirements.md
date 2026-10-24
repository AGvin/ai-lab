# Documentation Requirements

## Requirements

- Present Gemini API as Google's direct developer/model-access API service for invoking Gemini and supported Google generative-media models outside the Google Cloud Vertex AI service boundary.
- Preserve the current API boundary across Interactions, legacy generateContent/streaming, Live, Batch, embeddings, media-generation and platform utility APIs only while supported by current Google AI developer documentation.
- Keep concrete Gemini, Nano Banana, Veo, embedding, and other trained-model identities with Model Reference; the API is an access service, not the model family.
- Keep Google AI Studio as a development/playground/key-management surface, Vertex AI API as a separate Google Cloud service, Gemini Apps as assistant workspace, and Google agent infrastructure/frameworks with their own owners.
- Treat recommended/default API primitives, endpoint inventory, SDKs, model availability, free/paid tiers, pricing, quotas, rate limits, data-use terms, regions, tools/grounding, batch/live behavior, and deprecations as freshness-sensitive.
- Preserve the current migration boundary in which Interactions is recommended while generateContent remains supported/legacy; do not turn that mutable service guidance into a permanent standard.

## Validation

- Gemini API remains a direct hosted model-access service rather than the Gemini model family or Vertex AI API.
- Google AI Studio is not treated as a model alias.
- Producer provenance resolves bidirectionally to Google.
