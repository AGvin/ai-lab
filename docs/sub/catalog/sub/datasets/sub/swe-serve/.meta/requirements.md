# Documentation Requirements

## Requirements

- Identify SWE-Serve as NVIDIA's released inference-engineering benchmark/evaluation set for testing whether AI coding-agent patches work through a real live model-serving path, not only repository-local tests.
- Preserve the published scope of 53 SGLang inference-engineering tasks derived from merged pull requests, including the subset that starts a live server and validates behavior through public serving interfaces.
- Keep SGLang as the target software/runtime context rather than producer ownership; current NVIDIA material states the benchmark was developed with input from the SGLang team.
- Treat task inventory, source pull requests, harness/model set, pass rates, evaluation methodology, and reported comparative results as revision-specific and freshness-sensitive.
- Distinguish benchmark methodology from claims about general coding-agent quality outside the tested environment.

## Validation

- SWE-Serve remains a benchmark/dataset identity rather than an SGLang feature or general software-engineering concept.
- Producer provenance remains source-backed and collaboration language is preserved.
