# Documentation Requirements

## Requirements

- Identify Hugging Face Skills as Hugging Face's official Agent Skills collection for Hub operations and AI/ML workflows such as dataset creation, model training, evaluation, and related ecosystem tasks.
- Preserve the collection boundary rather than materializing every skill as an independent catalog identity; `hf-cli` is the recommended bootstrap skill but remains part of the collection unless later selected independently.
- Keep Hugging Face Hub, `huggingface_hub`, CLI software, Spaces, Inference Providers, and model/dataset assets separate from the skill collection even when skills operate those surfaces.
- Treat exact skill inventory, generated CLI guidance, installation/plugin mechanisms, client compatibility, and CLI/MCP integration as freshness-sensitive.
- Render the standard `entity-relations` block from validated current-entity relations.

## Validation

- Producer provenance resolves to Hugging Face, Inc.
- The collection is not conflated with the Hub service or CLI itself.
