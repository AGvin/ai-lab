# Documentation Requirements

## Requirements

- Identify TorchAO as an independently released PyTorch-native model-optimization/quantization library for inference and training efficiency.
- Place TorchAO under `software/model-and-data-platforms/model-optimization-and-compilation` for its primary quantization and model-transformation role, not under the trained-model or execution-first runtime owners.
- Distinguish post-training quantization, quantization-aware training, low-bit kernels, mixed-precision workflows, model packing and sparsity, without duplicating PyTorch, ExecuTorch, vLLM, or downstream library integrations as TorchAO peers.
- Preserve version-specific stable/prototype feature boundaries and dependency compatibility for PyTorch, CUDA/other accelerators, model types, numerical precisions and kernels.
- Attribute model quality, memory-saving and performance claims to exact model, task, hardware, quantization scheme, runtime/backend, and source evidence. Upstream benchmark figures are not platform-independent guarantees.
- Retain official TorchAO source, packaging and documentation references, with PyTorch Project producer provenance.

## Validation

- Primary identity is model optimization, while training and serving are downstream applications.
- Current stable and experimental features are distinguished rather than merged.
- `produced-by` and `produces` relations resolve bidirectionally.
