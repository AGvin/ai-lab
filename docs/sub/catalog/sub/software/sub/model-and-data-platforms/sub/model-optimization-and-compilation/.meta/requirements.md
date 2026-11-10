# Documentation Requirements

## Requirements

- Present `model-optimization-and-compilation/` as the canonical software owner for self-managed toolchains whose primary identity is transforming model artifacts for efficiency, portability, compression, hardware targeting, or runtime compatibility through compilation, graph transformation, quantization, export/lowering, pruning, or related optimization pipelines.
- Keep training/fine-tuning/post-training frameworks whose primary role is changing model behavior through learning under model development.
- Keep execution/serving-first engines under inference runtimes even when they perform graph/runtime optimization.
- Classify compiler/runtime hybrids by durable product center rather than by presence of a runtime component.

## Validation

- Children are optimizer/compiler-first identities rather than model-training frameworks or inference-serving engines.
- Artifact-transformation claims are source-backed by current upstream documentation.
- Navigation matches validated materialized direct children.
