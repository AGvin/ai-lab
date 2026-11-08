# Vertex AI API

Vertex AI API, also documented as Generative AI on Vertex AI and under the broader Gemini Enterprise Agent Platform, is Google's Google Cloud-managed model-access service for invoking Google and supported third-party foundation models through project-scoped APIs. [Google Cloud model access](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/).

## Model, hosting and agent boundaries

Model Garden, publisher endpoints, managed model APIs, supported partner models, tuning and grounding are part of a broader model-access/deployment experience, not a single trained-model identity. Original Gemini, Anthropic, Meta, Mistral and other model provenance remains with the upstream model producer even when the API, entitlement or billing is mediated by Google Cloud.

Google's direct Gemini API outside Vertex has different keys and billing; Vertex AI Agent Engine, Google Agent Registry, Google ADK and managed agent platforms also retain separate infrastructure and lifecycle boundaries. A documentation rename under Gemini Enterprise Agent Platform is not itself evidence of a newly independent API product. [Supported partner model hosting](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/use-partner-models).

## Operational boundaries

Check model-specific project and regional availability, IAM, authentication, quotas, pricing, safety and retention policies, managed API versus self-deployed models, inference regions, lifecycle and API compatibility. Availability through a common endpoint does not establish identical model parameters, portability or provider terms. [Google Cloud API documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis).

## Relations

- Produced by [Google Cloud](../../../../../producers/sub/g/sub/google-cloud/).

## Official resources

- [Models on Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/)
- [Partner model APIs](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/use-partner-models)
- [Platform APIs](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)
