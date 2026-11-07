# Documentation Requirements

## Requirements

- Identify MLPerf End-to-End RAG Inference as MLCommons' released multi-component benchmark for measuring a retrieval-augmented generation pipeline end to end, first included in MLPerf Inference v6.1.
- Preserve the two workload identities within the benchmark — database ingestion (`e2e-rag-db`) and question answering (`e2e-rag-qna`) — as benchmark workloads rather than separate canonical datasets unless upstream lifecycle later gives them independent identities.
- Preserve the current FRAMES-based query/corpus snapshot, pipeline components, reference models, hop limits, throughput/accuracy metrics, and compliance criteria only with exact release/version scope.
- Keep FRAMES, component models, vector databases, serving frameworks, and vendor submissions separate from the MLPerf benchmark identity.
- Treat result tables, system submissions, supported scenarios, accuracy thresholds, reference implementations, and component model selections as freshness-sensitive.
- Preserve MLCommons producer provenance through the canonical relation.

- Reconcile the reader with the source-backed identity, access and interpretation context in canonical `entity.identity_note`.
- Render the standard `entity-relations` block from the validated current-entity relation projection.

## Validation

- The node remains a concrete benchmark identity rather than a generic RAG concept or an implementation recipe.
- MLCommons provenance resolves bidirectionally.
- Component models/datasets are not misrepresented as produced or owned by MLCommons solely because the benchmark uses them.

## Scoped original-source qualification — 2026-11-08

- **MLPerf End-to-End RAG Inference** is MLCommons' **2026-08-26** published benchmark, introduced in the **Inference v6.1** cycle and included in its **2026-09-16** results. Unlike isolated text-embedding or language-model inference tests, it measures a multi-component document-ingestion/vector-database and retrieval-augmented question-answering pipeline.
- Benchmark workloads **`e2e-rag-db`** and **`e2e-rag-qna`** are parts of the same MLPerf benchmark, not independently authored standalone corpus entities. A frozen **FRAMES-based** question/corpus snapshot, database access, models, hop limits, retrieval/re-ranking, answer accuracy and workload configurations require exact release pinning. The FRAMES authors retain their separate dataset origin.
- Original publisher sources: https://mlcommons.org/2026/08/endtoend-inference/ ; https://mlcommons.org/2026/09/mlperf-inference-v6-1-results/ ; https://docs.mlcommons.org/inference/index_gh/
- Accepted the existing original benchmark identity, public v6.1 publication and pipeline-task separation only. No indexed database built, tested RAG system, vendor-score assurance, corpus copyright/legal/security audit, whole-repo CI/render, clean or final gate.
