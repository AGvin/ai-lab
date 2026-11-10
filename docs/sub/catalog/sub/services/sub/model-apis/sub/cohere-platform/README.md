# Cohere Platform

Cohere Platform is Cohere's managed public SaaS API for model inference and related language-AI services. Its API documentation covers chat, embeddings, reranking, and supported audio transcription and other model operations. [Cohere API reference](https://docs.cohere.com/reference/about).

## Model and deployment boundaries

Cohere Platform is the direct managed API service, not the underlying Command, North, Embed, Rerank, Parse or Transcribe trained models. [Cohere North](../../../assistant-workspaces/sub/cohere-north/) is a separate enterprise assistant/workspace. Cohere Model Vault and private-cloud/on-premises deployments have different infrastructure, data and operating boundaries; a common model API does not imply a shared deployment or security policy.

## API and operations

Documented v2 operations include Chat, Rerank, Embed and audio transcription, alongside older v1 and deprecated resources. Verify model-level text/multimodal capabilities rather than inferring them from a family name. API versions, credentials, model inventory, quotas, pricing, rate limits, SDKs, region and data-retention policies vary by chosen service/deployment. [Deployment options](https://docs.cohere.com/docs/deployment-options-overview).

## Relations

- Produced by [Cohere](../../../../../producers/sub/c/sub/cohere/).

## Official resources

- [Cohere API reference](https://docs.cohere.com/reference/about)
- [Deployment options](https://docs.cohere.com/docs/deployment-options-overview)
- [Cohere platform overview](https://docs.cohere.com/docs/welcome)
