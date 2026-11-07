# Documentation Requirements

## Requirements

- Identify MLPerf Client v2.0 as the released MLCommons client-system benchmark suite for evaluating generative-AI and agentic workloads on personal computers.
- Preserve the v2.0 suite boundary, including current LLM tests, the added image-generation category, and agentic AI workloads such as software-engineering and data-analyst tasks, without promoting every version-scoped subtest to an independent catalog identity by default.
- Keep reference models, mandatory/experimental status, prompt lengths, task definitions, accuracy gates, platform/runtime requirements, submission rules, and results tied to the exact benchmark revision.
- Distinguish benchmark methodology from vendor system submissions and product-performance claims.
- Preserve MLCommons producer provenance through the canonical relation.

- Reconcile the reader with the source-backed identity, access and interpretation context in canonical `entity.identity_note`.
- Render the standard `entity-relations` block from the validated current-entity relation projection.

## Validation

- The node remains the MLPerf Client v2.0 benchmark-suite identity rather than a PC hardware product or individual workload page.
- Results are not generalized beyond the exact benchmark revision and system configuration.
- MLCommons provenance resolves bidirectionally.

## Scoped original-source qualification — 2026-11-08

- **MLPerf Client v2.0** is MLCommons' publicly released **2026-08-18** benchmark suite for local AI workloads on personal computers, not a hardware or trained-model product. Version 2.0 incorporates mandatory updated LLM tests, agentic software-engineer/data-analyst tasks and an **experimental** image-generation workload; the model roster and required/experimental flags apply only to v2.0.
- The suite distinguishes model inference, agent tool time, end-to-end response, hardware drivers and client runtime, and published per-system submissions; a single model score or PC result does not rank all hardware configurations. Image-generation and data/task rights require separate verification from the suite's open-source code license.
- First-party sources: https://mlcommons.org/2026/08/mlperf-client-v2-0/ ; https://mlcommons.org/benchmarks/client/
- Scoped gate verifies the existing suite's publisher identity, dated v2.0 edition and public workload/status boundaries only. No benchmark run, certified vendor performance, independent licensing/security/compliance audit, whole-repo schema/cache/CI/render, clean or final credit.
