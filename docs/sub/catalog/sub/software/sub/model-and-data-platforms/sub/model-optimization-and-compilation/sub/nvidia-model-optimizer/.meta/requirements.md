# Documentation Requirements

## Requirements

- Present NVIDIA Model Optimizer (ModelOpt) as NVIDIA's self-managed model-optimization library for quantization, pruning, distillation, neural architecture search, speculative decoding, sparsity, and related model transformation workflows.
- Preserve the current NVIDIA Model Optimizer identity after the December 2025 rebrand from NVIDIA TensorRT Model Optimizer; keep the former name as an alias rather than a separate current product.
- Keep downstream deployment targets such as TensorRT-LLM, TensorRT, vLLM, and SGLang as integrations/consumers rather than part of Model Optimizer's software identity.
- Keep generic model training, inference serving, and runtime execution outside this entity except where they are direct optimization/export integrations.
- Treat supported model families, optimization techniques, export formats, deployment integrations, package versions, and pre-1.0 deprecation behavior as freshness-sensitive.
- Render the standard `entity-relations` block from validated current-entity relations.

## Validation

- Model Optimizer remains optimizer/artifact-transformation-first rather than serving- or training-first.
- Current naming and stable installation remain traceable to NVIDIA first-party sources.
- Producer provenance resolves bidirectionally to NVIDIA.
