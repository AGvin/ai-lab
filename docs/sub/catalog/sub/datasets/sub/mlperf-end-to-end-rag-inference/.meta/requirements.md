# Documentation Requirements

## Requirements

- Identify MLPerf End-to-End RAG Inference as MLCommons' released multi-component benchmark for measuring a retrieval-augmented generation pipeline end to end, first included in MLPerf Inference v6.1.
- Preserve the two workload identities within the benchmark — database ingestion (`e2e-rag-db`) and question answering (`e2e-rag-qna`) — as benchmark workloads rather than separate canonical datasets unless upstream lifecycle later gives them independent identities.
- Preserve the current FRAMES-based query/corpus snapshot, pipeline components, reference models, hop limits, throughput/accuracy metrics, and compliance criteria only with exact release/version scope.
- Keep FRAMES, component models, vector databases, serving frameworks, and vendor submissions separate from the MLPerf benchmark identity.
- Treat result tables, system submissions, supported scenarios, accuracy thresholds, reference implementations, and component model selections as freshness-sensitive.
- Preserve MLCommons producer provenance through the canonical relation.

## Validation

- The node remains a concrete benchmark identity rather than a generic RAG concept or an implementation recipe.
- MLCommons provenance resolves bidirectionally.
- Component models/datasets are not misrepresented as produced or owned by MLCommons solely because the benchmark uses them.
