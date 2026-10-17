# Documentation Requirements

## Requirements

- Present Vertex AI API / Generative AI on Vertex AI as Google Cloud's hosted model-access service for invoking Google and selected partner foundation models through project-scoped managed APIs.
- Preserve the model-access/deployment boundary across publisher endpoints, Gemini and supported partner-model APIs, Model Garden access/deployment options, tuning/evaluation/grounding integrations, and OpenAI-compatible access where currently supported.
- Keep concrete Gemini, Gemma, Anthropic, Mistral, AI21, Meta, and other trained-model identities with their upstream model owners; Vertex availability does not transfer producer provenance to Google Cloud.
- Keep Vertex AI Agent Engine, Gemini Enterprise Agent Platform, Google Agent Registry, Google ADK, and broader Vertex AI training/data services separate from this model-access identity.
- Treat model inventory, endpoint types, regions/global endpoint, managed API versus self-hosted deployment options, lifecycle/deprecations, pricing, quotas, safety controls, and partner-model availability as freshness-sensitive.
- Render the standard `entity-relations` block from validated current-entity relations.

## Validation

- Vertex AI API remains a hosted model-access service rather than a trained-model family or Agent Engine.
- Partner-model provenance remains with upstream producers.
- Model Garden is treated as a discovery/deployment surface of the broader Vertex model-access platform unless a separate reader-use case requires another canonical owner.
- Producer provenance resolves bidirectionally to Google Cloud.
