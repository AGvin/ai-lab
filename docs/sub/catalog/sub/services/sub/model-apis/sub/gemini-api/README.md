# Gemini API

Gemini API is Google's direct developer model-access service for calling supported Gemini and generative-media models through Google AI developer tools and APIs. It is distinct from the Google Cloud Vertex AI API and the end-user Gemini assistant. [Gemini API documentation](https://ai.google.dev/gemini-api/docs).

## Interface and model boundaries

Google's **Interactions API** has been documented as generally available and recommended for new applications since June 2026; `generateContent` remains supported as a legacy interface. This recommendation and the exact tool, model, agent and multimodal feature matrix are version-dependent rather than permanent. [Interactions API guidance](https://ai.google.dev/gemini-api/docs/interactions-overview).

The API exposes invocation, streaming/Live, batch, embeddings, supported media and tool workflows; the models' original identity and model-lineage facts remain with Model Reference. Google AI Studio is an adjacent development/key-management interface, while Vertex AI has its own Google Cloud project, regional, access and billing boundaries.

## State and operational boundaries

Interactions can keep server-side state by default, with documented stateless options. Check the active data-retention configuration, API key security, free/paid usage, quotas, regions, model rollout, tool support, prices, safety configuration and deprecations for the real environment. [Interactions state and retention](https://ai.google.dev/gemini-api/docs/interactions-overview).

## Relations

- Produced by [Google](../../../../../producers/sub/g/sub/google/).

## Official resources

- [Gemini API documentation](https://ai.google.dev/gemini-api/docs)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview)
- [Gemini API reference](https://ai.google.dev/api)
