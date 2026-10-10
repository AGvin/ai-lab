# Documentation Requirements

## Requirements

- Identify Megatron-LM as NVIDIA's released open-source framework/library for training large transformer models at scale.
- Preserve its primary large-scale model-development identity across tensor/pipeline/context/expert/data parallelism, distributed optimizer, checkpointing, mixed precision, and current transformer-training components.
- Keep Megatron Core, NeMo training products, DeepSpeed integrations, model checkpoints, Transformer Engine, NCCL, and downstream frameworks separate where independently materialized; ordinary modules of the same project are not peer products by default.
- Treat supported model architectures, PyTorch/CUDA/Transformer Engine versions, distributed strategies, precision, parallelism features, checkpoint formats, cluster topology requirements, and release versions as freshness-sensitive.
- Attribute scale/performance results to exact model size, GPU generation/count, network, precision, batch/sequence, and software revision.
- Preserve NVIDIA producer provenance.

## Validation

- Megatron-LM remains model-training software rather than a trained model or hosted service.
- Performance claims remain configuration-scoped.
- Producer provenance resolves to NVIDIA.
