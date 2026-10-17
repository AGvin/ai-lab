# Documentation Requirements

## Requirements

- Present `vector-search/` as the canonical service owner for producer-operated products whose primary identity is managed vector storage, indexing, similarity/hybrid search, or retrieval infrastructure for AI applications.
- Allow supporting full-text/sparse search, filtering, embeddings/reranking helpers, RAG integrations, and managed cluster/serverless operation without changing placement while managed search/retrieval remains primary.
- Exclude memory/context-first services even when they use vector stores, general databases/cloud products that merely expose vector search, hosted web search/extraction services, and self-managed vector/search software.
- Require an independently durable managed vector/search service identity rather than classifying by feature presence.
- Link every materialized direct child exactly once and keep mutable pricing/limits/availability/region claims with concrete product profiles.

## Validation

- Children are independently identifiable producer-operated vector/search services.
- General database products are not included solely because vector search is available.
- Navigation matches validated materialized direct children.
