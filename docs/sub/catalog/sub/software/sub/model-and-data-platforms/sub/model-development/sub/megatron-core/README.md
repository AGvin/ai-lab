# Megatron Core

NVIDIA's open-source, composable library for building large-scale model-training systems, distributed as `megatron-core` and imported through `megatron.core`.

## Capabilities and software boundary

Megatron Core provides model and transformer building blocks, distributed optimizers, parallelism strategies and mixed-precision training components. It is a reusable foundation for custom training frameworks.

The [Megatron-LM](../megatron-lm/) reference implementation combines Core with training scripts and examples in the same upstream repository. [Megatron Bridge](../megatron-bridge/) supplies a separate training and checkpoint-conversion layer. Internal Core modules do not become standalone software identities.

## Compatibility, evidence and operations

Choose the package or source release together with compatible PyTorch, CUDA, communication libraries, Transformer Engine and installation extras. Match the model architecture, parallelism layout, checkpoint format and precision to the cluster configuration.

The published package is classified Production/Stable; experimental development branches and newly added integrations still have their own constraints. Throughput and scale depend on the model, GPU generation/count, network, sequence/batch settings and software revision. Package metadata mixes BSD and Apache labels. The reviewed release license contains BSD-style redistribution conditions and component notices; use the actual selected-release license for distribution terms.

## Relations

- Produced by: [NVIDIA](../../../../../../../producers/sub/n/sub/nvidia/)

## Official resources

- [Megatron ecosystem overview](https://docs.nvidia.com/megatron-core/developer-guide/latest/get-started/overview.html)
- [Installation](https://docs.nvidia.com/megatron-core/developer-guide/latest/get-started/install.html)
- [Core source directory](https://github.com/NVIDIA/Megatron-LM/tree/main/megatron/core)
- [Package and lifecycle metadata](https://pypi.org/project/megatron-core/)
- [Repository license and component notices](https://github.com/NVIDIA/Megatron-LM/blob/core_v0.19.2/LICENSE)
