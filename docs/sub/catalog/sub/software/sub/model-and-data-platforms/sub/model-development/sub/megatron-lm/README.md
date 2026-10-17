# Megatron-LM

Megatron-LM is NVIDIA's open-source reference training framework for large transformer models, combining Megatron Core with preconfigured training scripts.

## Capabilities and software boundary

Supports combinations of tensor, pipeline, context, expert and data parallelism with distributed optimizers, mixed precision and training checkpoints. Megatron Core is the composable library of GPU-optimized building blocks used by the Megatron-LM reference implementation; both are developed in the same upstream repository. NeMo products, Transformer Engine, model checkpoints and downstream integrations have their own product or artifact boundaries.

## Compatibility, evidence and operations

Validate PyTorch, CUDA, communication libraries, model architecture, checkpoint format and cluster topology for the selected release. Throughput and scale depend on GPUs, interconnect, sequence/batch size and precision.

## Relations

- Produced by: [NVIDIA](../../../../../../../producers/sub/n/sub/nvidia/)

## Official resources

- [Primary source](https://github.com/NVIDIA/Megatron-LM)
