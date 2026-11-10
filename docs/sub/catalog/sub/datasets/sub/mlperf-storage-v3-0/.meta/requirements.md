# Documentation Requirements

## Requirements

- Identify MLPerf Storage v3.0 as the released MLCommons benchmark suite for measuring storage-system performance under representative AI/ML workloads.
- Preserve the v3.0 suite boundary, including the newly added KV Cache and Vector Database tests and support for S3 object-storage access alongside POSIX, without promoting each version-scoped subtest to a peer catalog identity by default.
- Keep workload definitions, access layers, datasets/models, scale factors, metrics, rules, submission classes, power measurements, and result tables freshness-sensitive to the exact benchmark revision.
- Keep the benchmark distinct from concrete storage products, vector databases, inference runtimes, and the general KV-cache concept.
- Distinguish benchmark methodology from vendor submissions and performance claims.
- Preserve MLCommons producer provenance through the canonical relation.

- Reconcile the reader with the source-backed identity, access and interpretation context in canonical `entity.identity_note`.
- Render the standard `entity-relations` block from the validated current-entity relation projection.

## Validation

- The node remains the MLPerf Storage v3.0 benchmark-suite identity rather than a storage product, vector-database product, or KV-cache mechanism.
- Results are not generalized beyond the exact benchmark revision and submitted system.
- MLCommons provenance resolves bidirectionally.

## Scoped original-source qualification — 2026-11-08

- **MLPerf Storage v3.0** is MLCommons' published **2026-09-01** benchmark revision for measuring storage throughput under real AI/ML training and inference I/O patterns. Version 3.0 adds distinct **KV Cache** and **Vector Database** workload tests and **S3 object-storage access** alongside POSIX. These are tests/access layers within one suite, not standalone vector-database, memory-cache or cloud storage products.
- Results are scoped to the exact reference workloads, benchmark scale factors, simulated accelerator behavior, dataset size and file/data access patterns, test-accuracy thresholds, power metrics and submitted hardware configuration. A reported storage result cannot predict every vector database's query quality or every model's end-to-end latency.
- Original publisher sources: https://mlcommons.org/2026/09/mlperf-storage-v3-0-results/ ; https://mlcommons.org/benchmarks/storage/
- Source acceptance covers the existing v3.0 identity and publisher-documented workload/version boundary, not benchmark execution, actual system storage durability, vendor performance certification, corpus/data licensing, independent security/CI/render, clean or final gate.
