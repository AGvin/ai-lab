# Qwen3.8-27B

Qwen3.8-27B is the concrete 27B-parameter Qwen3.8 model released on 2026-08-14.

## Scope and boundaries

- Official model identity and source-backed capabilities without generalizing properties from the much larger Qwen3.8-2.4T-A95B sibling.
- Exact artifacts, quantizations, provider routes, benchmark state, and deployment recommendations remain outside intrinsic model identity unless separately materialized.

## Decision and Operational Boundaries

Qwen3.8-27B is the released 27B dense vision-language checkpoint, accepting image/video/text input and generating text under Apache-2.0.

- Its native context is 262,144 tokens; the card distinguishes extension to 1,000,000 tokens from native support and separately discusses hosted features.
- Thinking is on by default and can be disabled; reasoning-depth and history-preservation support must match the runtime.
- Keep checkpoint identity separate from quantization and runtime packaging; pin the chosen revision and validate processor, chat-template, reasoning-parser, and tool-parser support in the selected runtime.
- Keep model-generated text, code, and tool arguments separate from permission to execute them; the application owns command validation, tool access, network access, and sandboxing.

## Official resources

- <https://github.com/QwenLM/Qwen3.8>

## Relationships

| Relationship | Catalog page |
| --- | --- |
| Member of | [Qwen3.8](../../../../) |

## Primary Sources

- [Official model card or license: Qwen/Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B)
- [Official model card or license: Qwen/Qwen3.8-27B/blob/main/LICENSE](https://huggingface.co/Qwen/Qwen3.8-27B/blob/main/LICENSE)
