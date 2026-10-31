# Documentation Requirements

## Requirements

- Render the standard entity-relations block from the validated current-entity projection.

- Identify this checkpoint as the 8B instruct member of the Ministral 3 generation.
- Keep exact context, multimodal, benchmark, quantization, license, and runtime facts source-backed.

## Validation

- Membership resolves to Ministral.

## Source-backed profile

- Required reader orientation: Ministral 3 8B Instruct 2512 is the instruction-tuned multimodal checkpoint in Mistral AI’s December 2025 Ministral 3 generation.
- Preserve this model-scoped fact: The architecture has a 8.4B language model and a 0.4B vision encoder. The released instruct representation is FP8 under Apache 2.0. [Ministral 3 8B Instruct weights](https://huggingface.co/mistralai/Ministral-3-8B-Instruct-2512)
- Preserve this model-scoped fact: The GA API release `ministral-8b-2512` has a 256K-token context. Text and image inputs produce text, including function-call and JSON output. [Ministral 3 8B model card](https://docs.mistral.ai/models/ministral-3-8b-25-12)

## Operational and interpretation boundaries

- Explain this boundary: This is the Instruct checkpoint; the separately trained Base and Reasoning releases are not aliases. Mistral recommends a small, clearly defined tool set and avoiding extreme image aspect ratios. [Ministral 3 8B Instruct weights](https://huggingface.co/mistralai/Ministral-3-8B-Instruct-2512)
- Explain this boundary: A parameter count is not a memory budget. The runtime, precision, images and context determine deployment requirements; the calling application controls tool execution.

- Keep source-reported capabilities distinct from application-level correctness, authorization and measured deployment performance.
