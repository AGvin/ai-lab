# Documentation Requirements

## Identity and decision boundaries

- Distinguish 149M/768-dimensional and 47M/384-dimensional retrievers from query-document relevance scoring by the reranker.
- Keep this English family separate from Multilingual R2. Embeddings and reranking scores are different output contracts.
- Preserve only the source-explicit English R2 retriever-to-reranker derivative pair; size similarity does not establish additional lineage.
- The selected member weights use Apache-2.0; retain member-specific runtime and task boundaries.

## Validation

- Resolve identity, family membership and declared inverse relations to canonical entities.
- Keep downloaded-weight licensing separate from hosted terms and runtime-specific artifacts.
- Pin the selected checkpoint and runtime before deployment; measure memory, latency and task quality on representative inputs.
- Published benchmark results are producer claims; this documentation does not establish runtime or benchmark reproduction, cache freshness or final-render validation.
