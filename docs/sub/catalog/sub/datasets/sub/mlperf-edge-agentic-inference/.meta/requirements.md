# Documentation Requirements

## Requirements

- Identify MLPerf Edge Agentic Inference as the released MLCommons benchmark introduced in MLPerf Inference v6.1 for measuring multi-turn agentic inference on a single edge accelerator.
- Preserve the benchmark's current two-part boundary: a BFCL-based deterministic accuracy gate and a recorded multi-turn agentic-coding replay for single-stream performance, only at the exact released revision supported by MLCommons.
- Keep BFCL as its own canonical benchmark/dataset identity; using BFCL data inside the MLPerf workload does not transfer ownership or collapse the two benchmarks.
- Keep the selected reference model/quantization, workload traces, accuracy thresholds, latency metrics, hardware constraints, submission rules, and result tables freshness-sensitive to the exact MLPerf release.
- Distinguish benchmark methodology from vendor submissions and performance claims.
- Preserve MLCommons producer provenance through the canonical relation.

- Reconcile the reader with the source-backed identity, access and interpretation context in canonical `entity.identity_note`.
- Render the standard `entity-relations` block from the validated current-entity relation projection.

## Validation

- The node remains the Edge Agentic benchmark identity, not a duplicate BFCL page or a generic agentic-inference concept.
- MLCommons provenance resolves bidirectionally.
- Results are never generalized beyond the exact MLPerf version, workload, system, and submission configuration.

## Scoped original-source qualification — 2026-11-08

- **MLPerf Edge Agentic Inference** was separately introduced by MLCommons in **Inference v6.1**, first publicly specified on **2026-07-09** and included in published **2026-09-16** results. It measures **single-stream, multi-turn** agentic inference on an edge accelerator, not general datacenter concurrency or a coding-agent's autonomous task success.
- The v6.1 design uses **BFCL v4-derived function-call accuracy gates** and recorded agentic-coding conversation replay as a latency/performance workload. BFCL's separate publisher/dataset identity is not transferred by its use here. Context budget, reference quantization/model, thresholds, token latency, hardware, tool traces and submitter results must be pinned to a v6.1 revision.
- Original publisher sources: https://mlcommons.org/2026/07/mlperf-inference-v61-edge-agentic/ ; https://mlcommons.org/2026/09/mlperf-inference-v6-1-results/
- Source credit covers the distinct existing edge-agentic benchmark identity and publisher release/measurement scope, not model safety, tool correctness outside supplied task protocol, executed reference cases, general device ranking, rights/legal/security review, full schema/cache/CI/render, clean or final acceptance.
