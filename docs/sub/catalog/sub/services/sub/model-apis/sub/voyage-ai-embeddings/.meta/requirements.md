# Documentation Requirements

## Requirements

- Identify the provider-hosted Voyage embeddings service rather than a separately downloadable model, local Python/TypeScript SDK or vector database.
- Ground the main interface in `POST https://api.voyageai.com/v1/embeddings` with JSON `input`, `model` and optional `input_type`, authenticated by `Authorization: Bearer <VOYAGE_API_KEY>`.
- For text retrieval, document that `input_type=query` and `input_type=document` can alter embedding prompts to suit query/document roles. Inputs without a type are supported; never assert identical behavior or guarantee cross-model vector dimensions.
- Model IDs, context/tokens, quotas, batch sizes, billing, retention and support change. Read the current official API reference for the chosen model; avoid copying one snapshot's mutable numeric limits into timeless claims.
- Warn against disclosing API keys, sending copyrighted/private texts without authorization, confusing embedding representations with an automatic search index, or treating a commercial endpoint as an Apache-licensed tool.
- No authenticated request, embedding generation, accuracy evaluation, cross-region data audit or whole-catalog clean pass is claimed.

## Validation

- Verify the provider-owned API/product boundary and current documentation sources.
- Maintain a single catalog identity with the correct category link; never equate hosted terms with unrelated SDK or model licenses.
- Do not credit unperformed runtime, whole-site or clean-pass checks.
