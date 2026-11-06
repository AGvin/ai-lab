# Voyage AI Embeddings API

**Voyage AI Embeddings API** is a hosted model service that converts submitted text into vector representations for retrieval and related applications. It is distinct from individual Voyage model versions, SDK libraries, and customer-managed vector databases.

## Service interface

The [official embeddings reference](https://docs.voyageai.com/reference/embeddings-api) documents `POST https://api.voyageai.com/v1/embeddings`, a JSON input string or list, a selected embedding model and bearer-key authentication. For retrieval, the optional `input_type` distinguishes a search `query` from indexed `document` input; those modes can apply different prompts before vectorization.

The API returns embedding vectors and usage information. The caller must handle model-specific vector dimensionality, indexing, normalization, similarity search and access policies; this endpoint does **not** itself operate a persistent vector database.

## Data and commercial boundaries

Inputs may contain proprietary text or personal data. Protect API keys, review provider retention/processing terms, and evaluate model selection, quotas, rate limits and pricing against current published documentation. SDKs are access tools, not additional hosted-service identities. No embedding request, vector search, end-to-end RAG test or security/privacy audit was performed.

## Official sources

- [Embeddings API reference](https://docs.voyageai.com/reference/embeddings-api)
- [Embeddings documentation](https://docs.voyageai.com/docs/embeddings)
