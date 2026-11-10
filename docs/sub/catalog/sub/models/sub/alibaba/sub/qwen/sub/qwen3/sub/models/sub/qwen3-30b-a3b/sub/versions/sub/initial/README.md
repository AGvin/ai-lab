# Qwen3 30B-A3B — Initial Release

The initial Qwen3 30B-A3B release retains the base model identity while recording release-specific behavior.

## Parent model

- [Qwen3 30B-A3B](../../../..)
- [Version index](../..)

## Release behavior

This release supports the original Qwen3 thinking and non-thinking interaction modes.

Model-wide architecture, parameter counts, license, and artifact context remain on the parent Qwen3 30B-A3B page.

## Decision and Operational Boundaries

The initial Qwen3-30B-A3B checkpoint supports thinking and non-thinking text generation under Apache-2.0.

- Its native context is 32,768 tokens, with a separately configured 131,072-token YaRN extension; do not copy the 2507 native context into this release.
- Keep checkpoint identity separate from quantization and runtime packaging; pin the chosen revision and validate processor, chat-template, reasoning-parser, and tool-parser support in the selected runtime.
- Keep model-generated text, code, and tool arguments separate from permission to execute them; the application owns command validation, tool access, network access, and sandboxing.

## Official resources

- [Qwen3 30B-A3B](https://huggingface.co/Qwen/Qwen3-30B-A3B)

## Relationships

| Relationship | Catalog page |
| --- | --- |
| Version of | [Qwen3 30B-A3B](../../../../) |

## Primary Sources

- [Official model card or license: Qwen/Qwen3-30B-A3B](https://huggingface.co/Qwen/Qwen3-30B-A3B)
