# Qwen3-VL-32B-Instruct

Qwen3-VL-32B-Instruct has official Apache-2.0 open weights for text/image/video understanding and text generation.

## Decision and Operational Boundaries

- Keep native 256K context separate from extension to 1M and from hosted-region budgets; image/video preprocessing also consumes model context.
- Keep this Instruct checkpoint distinct from a Thinking sibling and from image/video generation or embedding models.
- Keep checkpoint identity separate from quantization and runtime packaging; pin the chosen revision and validate processor, chat-template, reasoning-parser, and tool-parser support in the selected runtime.
- Visual agent capability does not authorize clicking, shell execution, or disclosure of image/document contents.

## Relationships

| Relationship | Catalog page |
| --- | --- |
| Member of | [Qwen3-VL](../../../../) |

## Primary Sources

- [Official model card or license: Qwen/Qwen3-VL-32B-Instruct](https://huggingface.co/Qwen/Qwen3-VL-32B-Instruct)
- [Official repository: QwenLM/Qwen3-VL](https://github.com/QwenLM/Qwen3-VL)
