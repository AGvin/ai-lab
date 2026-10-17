# Documentation Requirements

## Requirements

- Present Axolotl as an open-source model-development/post-training framework for LLM/VLM fine-tuning and related training workflows.
- Keep SFT, LoRA/QLoRA, preference optimization, reinforcement-learning methods, reward modeling, and distributed training as capabilities of the same model-development identity.
- Treat supported models, trainers, accelerators, optimization libraries, configuration schema, hardware requirements, and package versions as freshness-sensitive.
- Render the standard `entity-relations` block from validated current-entity relations.

- State that telemetry is enabled by default and sends system/hardware information, selected model/configuration categories, runtime metrics and sanitized error information through PostHog; document the `AXOLOTL_DO_NOT_TRACK=1` or `DO_NOT_TRACK=1` opt-out controls from the current upstream telemetry guide.

## Validation

- Axolotl remains model-development software rather than model-optimization/compilation or inference-runtime ownership.
- Producer provenance resolves to Axolotl AI Cloud.
