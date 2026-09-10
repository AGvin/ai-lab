# Documentation Requirements

## Requirements

- Use the reader-facing title `Hybrid Retrieval` and introduce `hybrid search` as a common practical label rather than a separate canonical leaf.
- Define hybrid retrieval as combining two or more complementary retrieval signals, retrievers, candidate sets, or rankings to produce one retrieval result; lexical plus semantic/vector retrieval is the primary AI-search example but not the only possible hybrid composition.
- Distinguish candidate generation from fusion and reranking. Hybrid systems may merge scores, combine ranked lists, union candidate sets before a later reranker, route queries across retrievers, or use other explicit compositions.
- Explain that raw scores from different retrievers often have different scales and semantics. Direct weighted addition requires a defined normalization/calibration contract; rank-based fusion such as Reciprocal Rank Fusion combines positions instead of assuming raw-score comparability.
- Present fusion weights, RRF constants, candidate counts, deduplication, query routing, and retriever selection as implementation/evaluation choices rather than universal hybrid-search defaults.
- Explain that hybrid retrieval can preserve exact lexical evidence while adding meaning-oriented recall, but combining retrievers does not guarantee improvement for every query or corpus and can propagate weaknesses or access-control inconsistencies from either path.
- Distinguish hybrid retrieval from `reranking/`: fusion combines retrieval evidence or lists, whereas reranking applies a subsequent scoring/ordering stage to candidates; one system may use both.
- Require consistent document identity, versioning, permissions, filtering, and provenance semantics across combined retrieval paths when discussing system consequences, without moving those operational controls into the concept definition.
- Keep concrete score-normalization formulas, engine-specific fusion syntax, tuned weights, retrieval routes, benchmark gains, access-policy implementations, and RAG/model-selection decisions with their applicable engineering, evidence, catalog, or decision owners.
- Use the canonical entity references as research inputs for multi-retriever fusion and lexical/dense complementarity when reader-facing rendering is activated.

## Validation

- The page does not create a separate canonical `hybrid-search` child.
- Hybrid retrieval is not defined exclusively as one 50/50 lexical-vector score sum or one fusion algorithm.
- Raw scores from different retrievers are not assumed directly comparable without an explicit contract.
- Hybrid retrieval is distinguished from reranking and from a complete RAG pipeline.
- Combining retrievers is not presented as universally superior to the component systems.
- Legacy tuning/practical recommendations are preserved only as scoped evaluation boundaries rather than universal configuration.
