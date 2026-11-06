# TorchAO

TorchAO is a separately released PyTorch-native library for model-optimization workflows that target efficient training or inference.

## Scope and product boundaries

It provides quantization and low-bit-weight transformation workflows, with release-dependent sparsity and optimized kernel support. Quantization-aware training and post-training quantization are applications of this optimization library, not additional PyTorch or inference-server identities.

## Compatibility and operational considerations

PyTorch versions, accelerators, model families, numerical schemes and kernels have specific compatibility boundaries. Different APIs may be stable, prototype or experimental. Pin the exact TorchAO release and backend, and measure memory, quality and latency using the actual model, task, hardware, precision and runtime.

## Relations

- Produced by: [PyTorch Project](../../../../../../../producers/sub/p/sub/pytorch-project/)

## Official resources

- [Official documentation](https://docs.pytorch.org/ao/stable/)
- [Source repository](https://github.com/pytorch/ao)
