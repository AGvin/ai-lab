# Documentation Requirements

## Requirements

- Identify llm-d as an open-source, Kubernetes-native distributed LLM inference serving stack that orchestrates and optimizes model servers such as vLLM and SGLang for production cluster workloads.
- Preserve its primary placement under `inference-runtimes/distributed-serving`; llm-d operates above single-node/model-server engines rather than replacing their inference kernels.
- Preserve its CNCF-project and Kubernetes-oriented operating boundary without treating benchmark claims or accelerator coverage as stable catalog facts.
- Keep release versions, supported engines/accelerators, routing strategies, benchmark results, and deployment recipes source-backed when expanded.
- Include current official llm-d site and repository references.

## Validation

- The page distinguishes distributed orchestration from the underlying inference engines.
- Vendor/project benchmark claims are not presented as independent AI Lab evaluation.
- Official resource links match canonical entity metadata.
- The page contains no temporary-placeholder wording.
