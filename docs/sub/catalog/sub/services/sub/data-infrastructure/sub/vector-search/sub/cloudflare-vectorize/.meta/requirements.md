# Documentation Requirements

## Requirements

- Identify Cloudflare Vectorize as Cloudflare's generally available managed vector database for embedding storage, similarity search, recommendation, classification, anomaly detection, and retrieval workflows.
- Preserve its vector-search/data-infrastructure identity rather than collapsing it into Workers AI, AI Search, R2, D1, or AI Gateway.
- Keep embeddings/model generation separate from storage/query semantics even when Workers AI provides embeddings used by Vectorize.
- Treat dimensions, index/vector/namespace limits, metadata indexing, API versions, pricing, availability, and integration behavior as freshness-sensitive.
- Render the standard `entity-relations` block from validated current-entity relations.

## Validation

- The service remains a managed vector database, not a model API or full RAG application.
- Producer provenance resolves to Cloudflare.
