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

## Scoped original-source qualification — 2026-11-06

- Cohere's direct managed API currently documents a v2-oriented Chat, Embed, Rerank and audio-transcription surface, with older v1 resources and explicit deprecated endpoints. Endpoint and model-level capability distinctions matter: text-only reranking is not a general multimodal guarantee.
- Preserve public managed SaaS versus Model Vault, private/cloud and on-prem deployment identities. Hosting, API version, customization support, latency, data treatment, pricing and model inventories must be verified for the actual deployment and release.
- Verified first-party source 1: https://docs.cohere.com/reference/about
- Verified first-party source 2: https://docs.cohere.com/docs/deployment-options-overview
- Verified first-party source 3: https://docs.cohere.com/docs/rerank
- This accepts only service-scoped source identity and documented capability boundaries; it is not an exhaustive freshness audit, authenticated endpoint test, independent compliance/ownership review, global schema/cache/CI/render verification, clean pass or final-delivery gate.
