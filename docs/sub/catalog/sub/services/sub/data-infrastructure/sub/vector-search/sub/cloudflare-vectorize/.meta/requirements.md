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

## Scoped original-source qualification — 2026-11-07

- Cloudflare Vectorize is the managed vector index/database, not the AI Search ingestion/RAG service. Embedding generation may use Workers AI but is separate from vector storage and query operations.
- Publisher documentation: https://developers.cloudflare.com/vectorize/
- Qualification covers the existing service identity/source boundary only. No authenticated runtime testing, independent security/licensing assessment, full-repository checks, clean pass or final gate is claimed.
