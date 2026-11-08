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

## Scoped original-source qualification — 2026-11-08

- **Vertex AI API / Generative AI on Vertex AI** is an existing Google Cloud managed model-access service, now documented within the broader **Gemini Enterprise Agent Platform** product and API documentation. This is a current documentation/product-taxonomy evolution, not by itself proof that the existing Vertex model-API dataset must be duplicated or renamed during this scoped source acceptance.
- Google Cloud publishes managed APIs for its own **Gemini** and other generative models alongside eligible **third-party partner models** and open-weight deployments; partner-model MaaS calls are billed and mediated through Google Cloud infrastructure but the original model authorship remains with Anthropic, xAI, Mistral or another upstream publisher. Model Garden discovery, managed MaaS endpoints, self-deployed open models, Agent Engine, training and agents are separate deployment/ownership surfaces.
- Source-backed current API and lifecycle references: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/ ; https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/use-partner-models ; https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis .
- Scoped qualification accepts the existing Google Cloud model-access service's first-party operating and model-routing boundaries only. Reader and canonical link reconciliation to new Google documentation is separately required without extra credit; no credentials, inference, cloud resource deployment, external provider rights/region/legal/security assessment, global CI/render, clean or final gate.
