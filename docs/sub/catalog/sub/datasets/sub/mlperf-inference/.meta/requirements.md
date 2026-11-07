# Documentation Requirements

## Requirements

- Identify MLPerf Inference as MLCommons' open, versioned benchmark suite for architecture-neutral and reproducible measurement of trained-model inference-system performance across representative deployment scenarios.
- Preserve MLPerf Inference v6.1 as the current released suite revision only while supported by current MLCommons material; treat benchmark inventory, datasets, reference models, quality targets, scenarios, accuracy requirements, harnesses, metrics, power rules, submission classes, and results as version-sensitive.
- Link the separately materialized MLPerf Edge Agentic Inference and MLPerf End-to-End RAG Inference identities as current suite members without implying that those two nodes exhaust the suite's workload inventory.
- Keep MLPerf Endpoints as a distinct next-generation benchmark direction rather than silently renaming the current MLPerf Inference identity before MLCommons completes that transition.
- Keep vendor submissions, hardware products, inference runtimes, reference models, and individual datasets separate from the benchmark-suite identity.
- Preserve MLCommons producer provenance through the canonical relation.
- Attribute performance records to the exact submitted system, benchmark revision, scenario, quality target, and configuration rather than generalizing them into universal hardware or model rankings.

- Reconcile the reader with the source-backed identity, access and interpretation context in canonical `entity.identity_note`.
- Render the standard `entity-relations` block from the validated current-entity relation projection.

## Validation

- The node remains the durable MLPerf Inference benchmark-suite identity rather than one particular release, workload, hardware product, or results table.
- Independently materialized suite-member relations are not presented as an exhaustive workload list.
- MLCommons provenance resolves bidirectionally.
- Results remain scoped to the exact benchmark version and submitted system.

## Scoped original-source qualification — 2026-11-08

- **MLPerf Inference** is MLCommons' ongoing versioned benchmark suite for reproducible, architecture-neutral **trained-model inference-system** tests. The first-party **2026-09-16 v6.1** release expanded the suite with **Edge Agentic Inference** and **End-to-End RAG Inference**; these are recognized suite-member workload identities rather than the suite's entire benchmark inventory.
- Reference models, underlying datasets, load-generation scenarios, accuracy targets, latency/throughput/power metrics, submission classes and published vendor systems are all version-specific. **MLPerf Endpoints** is a separately released serving-endpoint methodology; the publisher's future transition roadmap is not a renaming of historic Inference v6.1 results.
- First-party sources: https://mlcommons.org/2026/09/mlperf-inference-v6-1-results/ ; https://mlcommons.org/benchmarks/inference-datacenter/ ; https://docs.mlcommons.org/inference/index_gh/
- Source credit limited to existing suite identity, public v6.1 edition/relations and general reproducibility contract. No actual model/system benchmark run, independent leaderboard audit, unrestricted third-party model/data rights, full legal/security/CI/render, clean or final gate.
