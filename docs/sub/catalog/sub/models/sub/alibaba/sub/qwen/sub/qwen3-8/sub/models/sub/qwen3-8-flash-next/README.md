# Qwen3.8-Flash-Next

Qwen3.8-Flash-Next is a separately released Qwen3.8 foundation-model identity published on 2026-08-26 with its own first-party repository and weights.

## Scope and boundaries

- Its own source-backed model facts rather than inheriting parameter or deployment claims from other Qwen3.8 siblings.
- Quantizations, provider routes, runtime packaging, benchmark state, and deployment recommendations remains outside intrinsic model identity unless separately materialized.

## Relations

- Member of: [`catalog/models/alibaba/qwen/qwen3-8`](../../../..//)

## Decision and Operational Boundaries

Qwen3.8-Flash-Next has released multimodal weights, but Qwen explicitly describes it as an experimental preview of an architecture intended for Qwen4.

- Use the Qwen Community License 1.0 attached to these weights. Commercial MaaS or AI Work Assistant businesses require a separate license without the 2.4T checkpoint's USD 50 million revenue threshold; observe the limited internal-use exception and attribution conditions.
- Keep 262,144-token native context distinct from extension to 1,000,000 and from hosted Qwen3.8-Flash features.
- Retain this pre-existing preview node for accurate reference; do not treat released preview weights as a stable Qwen4 model release.
- Keep checkpoint identity separate from quantization and runtime packaging; pin the chosen revision and validate processor, chat-template, reasoning-parser, and tool-parser support in the selected runtime.
- Keep model-generated text, code, and tool arguments separate from permission to execute them; the application owns command validation, tool access, network access, and sandboxing.

## Official resources

- <https://github.com/QwenLM/Qwen3.8-Flash-Next>

## Relationships

| Relationship | Catalog page |
| --- | --- |
| Member of | [Qwen3.8](../../../../) |

## Primary Sources

- [Official model card or license: Qwen/Qwen3.8-Flash-Next](https://huggingface.co/Qwen/Qwen3.8-Flash-Next)
- [Official model card or license: Qwen/Qwen3.8-Flash-Next/blob/main/LICENSE](https://huggingface.co/Qwen/Qwen3.8-Flash-Next/blob/main/LICENSE)
- [Official repository: QwenLM/Qwen3.8-Flash-Next](https://github.com/QwenLM/Qwen3.8-Flash-Next)
