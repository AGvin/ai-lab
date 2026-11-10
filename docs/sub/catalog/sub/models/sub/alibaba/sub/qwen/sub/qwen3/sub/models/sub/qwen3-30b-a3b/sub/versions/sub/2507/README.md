# Qwen3 30B-A3B Instruct 2507

Qwen3 30B-A3B Instruct 2507 is an updated instruction-tuned release of Qwen3 30B-A3B.

## Parent model

- [Qwen3 30B-A3B](../../../..)
- [Version index](../..)

## Release behavior

This release supports non-thinking mode only and has a native context length of 262,144 tokens.

Model-wide architecture and parameter counts remain on the parent Qwen3 30B-A3B page.

## Decision and Operational Boundaries

Qwen3-30B-A3B-Instruct-2507 is the separately named non-thinking-only release with 262,144-token native context and Apache-2.0 weights.

- The model does not produce the original thinking blocks; a client-side thinking switch cannot turn it into the initial hybrid checkpoint.
- Keep advertised extended contexts and serving limits separate from native context and from available output budget.
- Keep checkpoint identity separate from quantization and runtime packaging; pin the chosen revision and validate processor, chat-template, reasoning-parser, and tool-parser support in the selected runtime.
- Keep model-generated text, code, and tool arguments separate from permission to execute them; the application owns command validation, tool access, network access, and sandboxing.

## Official resources

- [Qwen3 30B-A3B Instruct 2507](https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507)

## Relationships

| Relationship | Catalog page |
| --- | --- |
| Version of | [Qwen3 30B-A3B](../../../../) |

## Primary Sources

- [Official model card or license: Qwen/Qwen3-30B-A3B-Instruct-2507](https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507)
