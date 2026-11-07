# Documentation Requirements

## Requirements

- Identify MLPerf Mobile v6.0 as MLCommons' released on-device/mobile AI inference benchmark suite, including newly added on-device generative-LLM tasks; preserve the v6.0 snapshot rather than flattening it into desktop/PC MLPerf Client or datacenter MLPerf Inference.
- Preserve the official v6.0 LLM test model references: Llama 3.2 1B Instruct, Llama 3.2 3B Instruct, and Llama 3.1 8B Instruct evaluated on TinyMMLU and IFEval prompts. These are workloads inside the Mobile suite, not independently invented benchmark products.
- Distinguish portable CPU evaluation from selected NPU-accelerated model/SoC backends; support depends on tested Snapdragon, Dimensity, Exynos, iOS/Android platform versions and backend implementation.
- Keep the benchmark methodology, reference models/datasets, accuracy thresholds, device/SoC thermals, batching, latency percentiles, acceleration and backend drivers tied to exact suite version and app build.
- Do not infer universal phone-performance rankings from isolated vendor scores or measured CPU-only paths.
- Preserve producer provenance through the canonical MLCommons relation and its inverse `produces`.

- Reconcile the reader with the source-backed identity, access and interpretation context in canonical `entity.identity_note`.
- Render the standard `entity-relations` block from the validated current-entity relation projection.

## Validation

- The suite and published release/version are identifiable, independently useful and source-backed.
- Published results are scoped to exact workload, system and methodology, not universal hardware/model claims.
- The official MLCommons producer is resolved bidirectionally.

## Scoped original-source qualification — 2026-11-08

- **MLPerf Mobile v6.0** is MLCommons' released **2026-06-15** suite for on-device AI benchmarking. Version 6.0 adds LLM tests using **Llama 3.2 1B/3B Instruct and Llama 3.1 8B Instruct**, and selected **TinyMMLU/IFEval** prompts as benchmark workloads, not independently authored MLCommons datasets.
- The publisher distinguishes supported **CPU evaluation** from particular **NPU-backed mobile SoC** paths; a result does not establish that all Android/iOS models or backends run every test. Retain exact app/suite build, memory/temperature/driver constraints, model quantization, response-length, accuracy gate and hardware revision for each reported submission. This suite is distinct from MLPerf Client's PC benchmark.
- Verified publisher sources: https://mlcommons.org/2026/06/mlperf-mobile-v6/ ; https://github.com/mlcommons/mobile_app_open
- Scoped acceptance establishes existing benchmark release, original publisher, published workloads and platform restrictions only. No on-device test, universal SoC compatibility, ML model licensing clearance, vendor-score validation, root-wide schema/cache/CI/render, clean or final credit.
