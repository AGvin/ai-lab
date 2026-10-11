# Documentation Requirements

## Requirements

- Identify Cloudflare AI Search as the independently released, fully managed search/RAG platform for indexing websites, R2 objects and uploaded content, with hybrid vector/keyword retrieval, metadata filters and optional answer generation.
- Keep it distinct from Cloudflare Vectorize, the underlying vector database. The official comparison explicitly says AI Search operates the complete ingestion/chunking/embedding/indexing/retrieval pipeline on top of Vectorize; Vectorize users directly manage embeddings and indexes.
- Preserve Cloudflare's October 1, 2026 **generally available** lifecycle boundary. Pricing, included Workers AI embeddings/reranking usage, storage quotas, OCR limits, region/account availability and November 1 billing commencement are mutable service facts.
- Do not duplicate indexes, namespaces, retrieval modes, reranking, AI Gateway providers, upload sources or individual generative models as independent AI Search service entities.
- Attribute inference, retrieval or answer quality to the exact embedding/reranking/generation models, source corpus, indexing modes, cache/settings and evaluation protocol; a managed search offering does not imply universal model-quality ranking.
- Preserve Cloudflare producer provenance with a reciprocal `produces` relation.

## Validation

- Managed content-to-search service is not conflated with low-level Vectorize or Workers AI inference.
- GA status and separate hosted service identity match official product documentation.
- Current features, model options and pricing carry first-party freshness boundaries.
- Reciprocal producer relation resolves correctly.
