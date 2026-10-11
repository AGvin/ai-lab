# Documentation Requirements

## Requirements

- Identify DeepSpeed as Microsoft's open-source deep-learning optimization software suite whose primary catalog identity is large-scale model training/development, while also providing inference and compression capabilities.
- Preserve the single-product boundary across DeepSpeed Training, ZeRO/ZeRO-Infinity, parallelism/MoE, DeepSpeed Inference, compression, profiling, DeepNVMe, DeepCompile, SuperOffload, ZenFlow, optimizer integrations, and related project components unless upstream later gives a component an independently useful lifecycle.
- Keep DeepSpeed distinct from PyTorch, Hugging Face Accelerate/Transformers, distributed schedulers, inference-serving engines, model checkpoints trained with DeepSpeed, Azure ML, and hardware accelerators.
- Treat supported PyTorch/CUDA/ROCm versions, accelerator support, build extensions, optimizer/kernel availability, ZeRO stages/options, precision support, offload behavior, inference paths, release versions, and integration compatibility as freshness-sensitive.
- Attribute performance/scale comparisons to Microsoft/DeepSpeed or the cited evaluator and preserve exact model, cluster, interconnect, precision, batch/sequence, and software configurations.
- Preserve Microsoft producer provenance even though current code is hosted under the `deepspeedai` GitHub organization.

## Validation

- DeepSpeed remains one software suite rather than duplicated into Training/Inference/Compression peer products.
- Integration references do not transfer ownership of PyTorch/Hugging Face or downstream models to DeepSpeed.
- Performance claims remain configuration-scoped.
- Producer provenance resolves bidirectionally to Microsoft.
