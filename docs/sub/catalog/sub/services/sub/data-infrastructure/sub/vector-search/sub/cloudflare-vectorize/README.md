# Cloudflare Vectorize

Cloudflare Vectorize is Cloudflare's managed vector database for embedding storage, similarity search, recommendation, classification, anomaly detection, and retrieval workflows.

## Service boundary

Vectorize remains a vector-search and data-infrastructure service rather than Workers AI, AI Search, R2, D1, AI Gateway, a model API, or a full RAG application. Embedding generation stays separate from Vectorize storage and query semantics even when Workers AI supplies embeddings.

Dimensions, index, vector and namespace limits, metadata indexing, API versions, pricing, availability, and integration behavior are freshness-sensitive.

## Relations

- Produced by [Cloudflare](../../../../../../../producers/sub/c/sub/cloudflare/).

## Official resources

- [Cloudflare Vectorize documentation](https://developers.cloudflare.com/vectorize/)
