# Documentation Requirements

## Requirements

- Identify MLPerf Mobile v6.0 as MLCommons' released on-device/mobile AI inference benchmark suite, including newly added on-device generative-LLM tasks; preserve the v6.0 snapshot rather than flattening it into desktop/PC MLPerf Client or datacenter MLPerf Inference.
- Preserve the official v6.0 LLM test model references: Llama 3.2 1B Instruct, Llama 3.2 3B Instruct, and Llama 3.1 8B Instruct evaluated on TinyMMLU and IFEval prompts. These are workloads inside the Mobile suite, not independently invented benchmark products.
- Distinguish portable CPU evaluation from selected NPU-accelerated model/SoC backends; support depends on tested Snapdragon, Dimensity, Exynos, iOS/Android platform versions and backend implementation.
- Keep the benchmark methodology, reference models/datasets, accuracy thresholds, device/SoC thermals, batching, latency percentiles, acceleration and backend drivers tied to exact suite version and app build.
- Do not infer universal phone-performance rankings from isolated vendor scores or measured CPU-only paths.
- Preserve producer provenance through the canonical MLCommons relation and its inverse `produces`.

## Validation

- The suite and published release/version are identifiable, independently useful and source-backed.
- Published results are scoped to exact workload, system and methodology, not universal hardware/model claims.
- The official MLCommons producer is resolved bidirectionally.
