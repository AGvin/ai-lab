# Documentation Requirements

## Requirements

- Describe **Scaleway Generative APIs** as a released Scaleway-operated cloud service for hosted AI model inference. The serverless/shared endpoint and separately provisioned dedicated deployments belong to one official Generative APIs product, not original trained models or an invented parallel Managed Inference product.
- Preserve the actual published shared model API base `https://api.scaleway.ai/v1` and OpenAI-compatible Chat Completions; also document current Responses, embeddings, audio transcription, rerank, batch and model endpoints only as supported by the official API description. Exact features depend on model, endpoint and date.
- State a key compatibility gap: Scaleway's current Responses API does **not** implement stateful conversations or the OpenAI built-in tools, including web/file search; only its supported function calls are described. Passing an OpenAI SDK call does not guarantee complete OpenAI service parity.
- Differentiate model/service publisher from upstream models (including DeepSeek, Qwen, GLM and Meta). A Scaleway-hosted model still has its own original producer, lifecycle and license; model rights and third-party indirect ownership/sanctions risk are not cleared by French server location or the operator's corporate identity.
- Present vendor current Paris-region hosted execution and European privacy claims as sourced and time-bound, not an eternal region, nationwide jurisdiction or legal guarantee. Published product account/key prerequisites, rate limits, per-model supported operations and credits/prices are mutable.
- **Critical privacy qualification:** Scaleway says default zero-data-retention and no routine prompt training, but documents exceptional temporary capture of complete request content to troubleshoot anomalous requests/abuse for up to two weeks. Anonymized usage metadata can be stored up to six months and ephemeral caching has separate properties; do not say universal 'never logs anything' or infer the same handling in batch and dedicated contexts.
- Use one company producer **Scaleway SAS**, confirmed on the current French legal notice with SIREN 433 115 904 and Paris registered office. Its official About page describes iliad Group subsidiary status. Do not infer a complete beneficial ownership, sanctions, indirect national control, or all corporate contract entities from public marketing alone.
- Link exactly one `produced-by` / `produces` pair and official product/API/privacy/company sources. No authenticated inference, independent cost/performance benchmarking, full schema/cache/CI or clean whole-catalog pass has been performed.

## Validation

- One product-level hosted Generative APIs identity, not duplicate dedicated/Managed Inference variant or upstream model authorship.
- Published endpoint, Responses limitations, data-retention exceptions and upstream model rights are accurately scoped.
- Canonical metadata, reciprocal links, reader and index checked separately from full rendering, live service or regulatory verification.
