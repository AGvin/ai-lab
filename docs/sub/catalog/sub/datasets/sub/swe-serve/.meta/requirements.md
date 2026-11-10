# Documentation Requirements

## Requirements

- Identify SWE-Serve as NVIDIA's released inference-engineering benchmark/evaluation set for testing whether AI coding-agent patches work through a real live model-serving path, not only repository-local tests.
- Preserve the published scope of 53 SGLang inference-engineering tasks derived from merged pull requests, including the subset that starts a live server and validates behavior through public serving interfaces.
- Keep SGLang as the target software/runtime context rather than producer ownership; current NVIDIA material states the benchmark was developed with input from the SGLang team.
- Treat task inventory, source pull requests, harness/model set, pass rates, evaluation methodology, and reported comparative results as revision-specific and freshness-sensitive.
- Distinguish benchmark methodology from claims about general coding-agent quality outside the tested environment.

- Preserve the first-release scope of 53 executable tasks derived from 83 merged SGLang pull requests, including 19 with live-serving checks; the task count is not a one-to-one pull-request count.
- Explain containerized pre-change checkouts, complete hidden-verifier success on declared hardware, and the release-specific CPU/single-H100 boundary. Preserve closed-book evaluation conditions and distinguish SGLang team input from NVIDIA ownership of SGLang.
- Render the complete visible current-node relation set through the standard `entity-relations` component as a provenance block; preserve relation semantics and canonical target identities.
- Render an `official-resources` block with this explicit selection from canonical references: [SWE-Serve release, live-serving protocol, and collaboration](https://developer.nvidia.com/blog/how-swe-serve-exposes-the-gap-between-local-tests-and-live-serving/).

## Validation

- SWE-Serve remains a benchmark/dataset identity rather than an SGLang feature or general software-engineering concept.
- Producer provenance remains source-backed and collaboration language is preserved.

## Scoped original-source qualification — 2026-11-08

- **SWE-Serve** is NVIDIA's original **2026-09-23** inference-engineering coding-agent benchmark assembled with input from the SGLang maintainers. Its first public release contains **53 executable tasks selected from 83 merged SGLang pull requests**, spread over model/backend enablement, decoding, kernels/performance, serving API/runtime correctness, caching and distributed scheduling. Tasks and merged pull requests are not one-to-one identities.
- **Nineteen tasks require real live-serving verification** beyond local tests; the source describes **12 CPU-only tasks and 41 tasks on one NVIDIA H100**, with a containerized pre-change checkout and hidden task-specific behavioral verifier. A reported agent pass, server start or benchmark score depends on benchmark release, model/harness, hardware, timeout and isolation, and cannot establish correct implementation across other inference frameworks, GPUs or cluster sizes.
- First-party publisher source: https://developer.nvidia.com/blog/how-swe-serve-exposes-the-gap-between-local-tests-and-live-serving/ .
- One scoped source gate verifies the existing NVIDIA-produced benchmark identity and its published 53/83/19 hardware/verification scope. No agent patches developed or run, executable containers/model checkpoints downloaded, independent score or rights/security/legal audit, global schema/cache/CI/render, clean or final gate.
