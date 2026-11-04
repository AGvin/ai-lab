# Documentation Requirements

## Requirements

- Classify ComputeEval as a benchmark challenge/data family for generated CUDA code, not a hosted inference service, NVIDIA GPU SKU, or a claim that code execution passed.
- Official README describes handcrafted tasks covering CUDA runtime, kernels, GPU libraries and template/DSL variants. Each challenge has a problem specification, model-visible context, hidden reference solution, held-out tests and optional performance comparison.
- Dataset task inventory can change frequently. Record exact upstream revision, task groups, target GPU, CUDA toolkit, compiler, dependencies, hardware limits, reference baseline, accuracy and timing protocol in any reproducible result.
- Executing model-generated CUDA/C++ can crash the GPU process, misuse resources or access data. Use an isolated, quota-limited compute environment with no production credentials, resource boundaries, timeouts and secured artifacts.
- Apache-2.0 applies to code covered by the pinned root LICENSE; proprietary CUDA libraries, external hardware/toolchains and test/problem sources may have additional distribution and use conditions.
- Do not claim CUDA build, GPU execution, code quality, benchmark score, complete dependency audit or whole-catalog clean pass.

## Validation

- One frozen dataset identity, pinned publisher sources, distinct benchmark task/harness/model/service artifacts and canonical index link.
- No live vulnerability code, score, legal clearance, complete CI or whole-catalog clean pass is implied.
