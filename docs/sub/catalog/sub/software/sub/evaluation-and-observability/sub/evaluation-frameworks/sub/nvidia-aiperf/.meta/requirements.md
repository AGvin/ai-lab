# Documentation Requirements

## Requirements

- Present NVIDIA AIPerf as an Apache-2.0 package, CLI, and Python API for performance testing AI model/inference endpoints.
- Preserve its evaluation-tool identity around throughput, latency, time-to-first-token, concurrency/load, multimodal workloads, speculative-decoding analysis, result visualization, and optional hardware telemetry rather than treating it as a benchmark dataset or inference runtime.
- Keep concrete benchmark suites such as MLPerf, model-serving runtimes, target endpoints, and hardware under their own canonical identities; AIPerf may execute measurements against them without owning them.
- Treat package versions, endpoint plugins, supported workload types, telemetry backends, output formats, and metric semantics as freshness-sensitive.
- Render the standard `entity-relations` block from validated current-entity relations.

## Validation

- AIPerf remains evaluation/performance-testing software rather than a benchmark dataset or serving engine.
- Producer provenance resolves bidirectionally to NVIDIA.
