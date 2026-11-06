# Qwen3.6-35B-A3B

Qwen3.6-35B-A3B is a released Apache-2.0 35B total/3B active MoE vision-language checkpoint for text, image, and video understanding with text output.

## Decision and Operational Boundaries

- Preserve 262,144-token native context and the separately documented extension to 1,010,000; thinking is on by default and can be disabled through the appropriate API/template setting.
- History-preservation and runtime-specific reasoning controls are configuration options; do not copy hosted behavior into every local runtime.
- Keep checkpoint identity separate from quantization and runtime packaging; pin the chosen revision and validate processor, chat-template, reasoning-parser, and tool-parser support in the selected runtime.
- Keep model-generated text, code, and tool arguments separate from permission to execute them; the application owns command validation, tool access, network access, and sandboxing.

## Relationships

| Relationship | Catalog page |
| --- | --- |
| Member of | [Qwen3.6](../../../../) |

## Primary Sources

- [Official model card or license: Qwen/Qwen3.6-35B-A3B](https://huggingface.co/Qwen/Qwen3.6-35B-A3B)
- [Official model card or license: Qwen/Qwen3.6-35B-A3B/blob/main/LICENSE](https://huggingface.co/Qwen/Qwen3.6-35B-A3B/blob/main/LICENSE)
- [Official repository: QwenLM/Qwen3.8](https://github.com/QwenLM/Qwen3.8)
