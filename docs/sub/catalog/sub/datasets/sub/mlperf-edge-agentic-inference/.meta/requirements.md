# Documentation Requirements

## Requirements

- Identify MLPerf Edge Agentic Inference as the released MLCommons benchmark introduced in MLPerf Inference v6.1 for measuring multi-turn agentic inference on a single edge accelerator.
- Preserve the benchmark's current two-part boundary: a BFCL-based deterministic accuracy gate and a recorded multi-turn agentic-coding replay for single-stream performance, only at the exact released revision supported by MLCommons.
- Keep BFCL as its own canonical benchmark/dataset identity; using BFCL data inside the MLPerf workload does not transfer ownership or collapse the two benchmarks.
- Keep the selected reference model/quantization, workload traces, accuracy thresholds, latency metrics, hardware constraints, submission rules, and result tables freshness-sensitive to the exact MLPerf release.
- Distinguish benchmark methodology from vendor submissions and performance claims.
- Preserve MLCommons producer provenance through the canonical relation.

## Validation

- The node remains the Edge Agentic benchmark identity, not a duplicate BFCL page or a generic agentic-inference concept.
- MLCommons provenance resolves bidirectionally.
- Results are never generalized beyond the exact MLPerf version, workload, system, and submission configuration.
