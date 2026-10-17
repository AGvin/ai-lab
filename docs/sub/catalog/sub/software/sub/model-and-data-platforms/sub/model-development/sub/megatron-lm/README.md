# Megatron-LM

NVIDIA's open-source framework/library for large-scale training of transformer models.

## Capabilities and software boundary

Supports combinations of tensor, pipeline, context, expert and data parallelism with distributed optimizers, mixed precision and training checkpoints. Megatron Core and ordinary modules are components, while NeMo products, Transformer Engine, models and downstream integrations can be separate entities.

## Compatibility, evidence and operations

Validate PyTorch, CUDA, communication libraries, model architecture, checkpoint format and cluster topology for the selected release. Throughput and scale depend on GPUs, interconnect, sequence/batch size and precision.

## Relations

- Produced by: [NVIDIA](../../../../../../../producers/sub/n/sub/nvidia/)

## Official resources

- [Primary source](https://github.com/NVIDIA/Megatron-LM)
