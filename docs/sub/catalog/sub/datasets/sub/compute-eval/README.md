# ComputeEval

**ComputeEval** is NVIDIA's CUDA code-generation benchmark for evaluating both **correctness** and, when configured, **performance** of code produced by language models.

## Task and measurement boundary

The [pinned source README](https://github.com/NVIDIA/compute-eval/blob/00fbad91b63957a002b501f33a06510cd25beaae/README.md) describes challenge directories with a task specification, model-visible CUDA headers and helpers, hidden reference solutions and tests. Tasks cover CUDA runtime operations, kernels, GPU libraries and template-based programming. A performance benchmark may compare execution to a reference baseline, but not every task has an identical performance setup.

Reproduce reported outcomes with the exact task set, compiler/CUDA version, GPU model, memory constraints, allowed tools, timeout and scoring implementation. Source tasks and test harnesses are parts of one benchmark; historical results and generated executables are separate.

## Safety and rights

Generated GPU code is **untrusted executable code**. It belongs in an isolated test environment, not production or a workstation with secrets. Constrain resources and data access and treat generated logs as potentially sensitive.

The [source LICENSE](https://github.com/NVIDIA/compute-eval/blob/00fbad91b63957a002b501f33a06510cd25beaae/LICENSE) is Apache-2.0 for covered material; toolchain and third-party library terms remain separate. No GPU compilation, device testing, model request, legal audit or whole-catalog clean pass was performed.

## Official source snapshot

- [Upstream repository](https://github.com/NVIDIA/compute-eval)
- [Pinned README](https://github.com/NVIDIA/compute-eval/blob/00fbad91b63957a002b501f33a06510cd25beaae/README.md)
- [Pinned root LICENSE](https://github.com/NVIDIA/compute-eval/blob/00fbad91b63957a002b501f33a06510cd25beaae/LICENSE)
