# Documentation Requirements

## Requirements

- Present Microsoft Olive as a self-managed model-optimization toolkit for transforming models through optimization, conversion, compression, quantization, packaging, and target-specific preparation.
- Keep runtime integrations and deployment helpers as downstream targets/capabilities rather than classifying Olive as an inference runtime.
- Keep generic fine-tuning/model-development facts outside this entity unless they directly serve Olive's optimization workflow.
- Treat supported passes, accelerators, runtimes, model formats, and version-specific features as freshness-sensitive.
- Render the standard `entity-relations` block from validated current-entity relations.

## Validation

- Olive remains optimizer/artifact-transformation-first rather than training- or serving-first.
- Producer provenance resolves to Microsoft.
