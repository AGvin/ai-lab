# NVIDIA Model Optimizer

NVIDIA Model Optimizer (ModelOpt) is a self-managed library for optimizing and transforming models for more efficient training and inference deployments.

## Scope and product boundaries

It supports release-dependent model compression and transformation workflows, including quantization, pruning, distillation, sparsity and related architecture or decoding optimizations. The current product name follows the former NVIDIA TensorRT Model Optimizer branding; that historic name remains an alias, not another catalog entity.

## Compatibility and operational considerations

TensorRT, TensorRT-LLM, vLLM and SGLang are potential consumers or integrations, not bundled duplicates of Model Optimizer. Check model architecture, export format, target runtime, GPU compatibility, package version and deprecations before selecting a method. Vendor speed or efficiency figures are not independent benchmark conclusions.

## Relations

- Produced by: [NVIDIA](../../../../../../../producers/sub/n/sub/nvidia/)

## Official resources

- [Source repository](https://github.com/NVIDIA/Model-Optimizer)
- [Documentation](https://nvidia.github.io/Model-Optimizer/)
