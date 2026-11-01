# Scaleway Generative APIs

**Scaleway Generative APIs** is [Scaleway SAS](../../../../../producers/sub/s/sub/scaleway-sas/)'s active, cloud-hosted model inference service. Its [serverless quickstart](https://www.scaleway.com/en/docs/generative-apis/quickstart/) documents OpenAI-compatible clients using `https://api.scaleway.ai/v1` with account IAM and an API key.

## Serverless, dedicated and model identity

The [official product description](https://www.scaleway.com/en/generative-apis/) distinguishes on-demand **Serverless** access to provider-hosted models from **Dedicated Deployment**, in which a customer provisions isolated inference capacity or deploys supported custom models. The [vendor FAQ](https://www.scaleway.com/en/docs/generative-apis/faq/) confirms that the earlier **Managed Inference** label was renamed **Generative APIs — Dedicated Deployment**; it is not a separate live legacy product.

The [current API reference](https://www.scaleway.com/en/developers/api/generative-apis) documents Chat Completions and additional endpoints for Responses, embeddings, audio transcription, reranking, batches and model discovery. **Compatibility is incomplete:** the Scaleway Responses interface does not support stateful conversations, built-in web/file search or all OpenAI parameters. Choose supported operations by actual model and endpoint; the catalog, rates, lifecycle and region availability may change. Models from Qwen, DeepSeek, GLM, Meta and other publishers keep their **original** training authorship, source rights and licensing.

## Privacy, security and practical operation

The [Scaleway Generative APIs privacy document](https://www.scaleway.com/en/docs/generative-apis/reference-content/data-privacy/) describes default zero data retention and states that prompts are not routinely used to train underlying models. **Important exception:** content of abnormal/problematic requests can be temporarily collected and accessed for troubleshooting or abuse investigations for **up to two weeks**; anonymized operational metadata may be retained for **up to six months**. Its ephemeral per-project caching and batch processing have different data-flow considerations. Do not interpret 'zero retention' as no logging or no exceptional human access.

The company currently describes its serverless infrastructure in Paris, France, but regions and data-processing terms are subject to revision. Verify current product-specific privacy, legal/DPA, processing region, TLS/IAM/security policies, upstream model rights and applicable ownership or sanctions restrictions for the actual account and use. Keep API keys out of source and logs. Pricing, quotas, model capability and SLA claims require current product-plan review; no authenticated inference, independent latency/cost test or complete corporate-ownership audit was performed.

## Provenance

- Produced by: [Scaleway SAS](../../../../../producers/sub/s/sub/scaleway-sas/).

## Official resources

- [Generative APIs product and deployment options](https://www.scaleway.com/en/generative-apis/)
- [Shared/serverless API quickstart](https://www.scaleway.com/en/docs/generative-apis/quickstart/)
- [API endpoints and interoperability boundaries](https://www.scaleway.com/en/developers/api/generative-apis)
- [Generative APIs privacy policy and exceptional-retention limits](https://www.scaleway.com/en/docs/generative-apis/reference-content/data-privacy/)
- [Serverless, Dedicated Deployment and legacy naming FAQ](https://www.scaleway.com/en/docs/generative-apis/faq/)
