# Documentation Requirements

## Requirements

- Present Cohere Platform as Cohere's fully managed public SaaS/API service for direct access to Cohere models and platform endpoints.
- Preserve the model-access boundary across Chat, Embed, Rerank, Parse, Transcribe, model customization, and related API resources only while current Cohere documentation supports them.
- Keep concrete Cohere model identities with Model Reference, Cohere North as a separate assistant/workspace service, and Cohere Model Vault/private deployment surfaces with their own owners.
- Treat API versions, endpoints, model inventory, SDKs, pricing, quotas, priority behavior, data controls, customization options, deprecations, and deployment-region/access state as freshness-sensitive.
- Preserve the distinction between Cohere-managed public SaaS, cloud-provider hosting, private cloud, and on-prem deployment paths.

## Validation

- Cohere Platform remains a hosted model/API service rather than a model family or North workspace.
- Deployment options do not transfer model producer provenance to hosting providers.
- Producer provenance resolves to Cohere.
