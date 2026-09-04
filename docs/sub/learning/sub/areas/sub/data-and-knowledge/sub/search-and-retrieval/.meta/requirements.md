# Documentation Requirements

## Requirements

- Present Search and Retrieval as practical teaching for finding and ranking relevant information before generation or another downstream decision.
- Materialize and link `lexical-retrieval/`, `semantic-retrieval/`, `vector-search/`, `hybrid-retrieval/`, `indexing-and-chunking/`, `reranking/`, and `filtering/` because each has source-backed material ready for migration.
- Evaluate retrieval stages independently enough to distinguish candidate-generation, filtering, fusion/ranking, reranking, and downstream failures.
- Use representative real query classes and explicit acceptance criteria; topically similar or mathematically nearest items are not automatically answer-bearing evidence.
- Preserve exact-match/lexical routes when identifiers, rare terms, codes, names, citations, negation, or other surface evidence matters; use semantic or hybrid signals when they measurably improve the workload.
- Apply required scope/tenant/access eligibility consistently across all retrieval paths; relevance ranking does not establish eligibility.
- Preserve stable source/chunk identity and provenance through indexing, deduplication, replacement, deletion, and downstream evidence use.
- Keep complete RAG workflow teaching with the selected Retrieval-Augmented Generation subtree and concrete search/database products with Catalog owners.

## Validation

- No retrieval method is presented as universally superior.
- Retrieval-stage quality is distinguishable from final generated-answer quality.
- Required eligibility constraints apply consistently across composed retrievers.
- Derived retrieval state remains traceable to current source identity/version.
