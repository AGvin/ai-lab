# Documentation Requirements

## Requirements

- Present Retrieval-Augmented Generation (RAG) as a retrieval-to-generation system whose ingestion, retrieval, context assembly, generation, provenance, and evaluation stages must be designed and verified separately enough to diagnose failures.
- Materialize `graph-rag/` because it has an independent source-backed legacy topic. Keep the other selected RAG children logical but unmaterialized until deeper standalone content justifies them; the current root preserves their cross-cutting workflow guidance.
- Typical ingestion concerns include parsing/normalization, source identity/versioning, segmentation, metadata/scope capture, optional learned representations, index updates, and removal of stale derived state.
- Typical query-time concerns include query analysis, one or more retrieval routes, optional filtering/reranking, evidence/context assembly, generation, citation/grounding support, and explicit insufficient-evidence handling.
- Do not require a vector store, embedding model, fixed chunk size, reranker, or one retrieve-once prompt shape; select components from representative workload evidence.
- For repository/code retrieval, preserve useful path, symbol/signature, class/function, import/export, exact-string, dependency, language-structure, and version/Git signals; route exact identifiers through lexical/symbol-aware retrieval when stronger than semantic similarity.
- Evaluate retrieval and generation stages separately, including candidate evidence recall, ranking/filter behavior, freshness, support/faithfulness, citations, abstention, latency, and cost; preserve representative failure cases instead of masking them with a stronger generator.
- Compare RAG with simpler direct-context, structured-query/API, lexical search, fine-tuning, or deterministic designs according to the actual requirement.
- Keep generic retrieval methods with Search and Retrieval, generic grounding/citation integrity with Trustworthy AI, and concrete products with Catalog/Evidence owners.

## Validation

- Retrieval failures and generation failures remain distinguishable.
- RAG components are selected by evidence rather than assumed mandatory.
- Source/provenance and derived-state lifecycle remain reconstructable.
- Unmaterialized selected RAG children are not implied absent from the logical architecture.
