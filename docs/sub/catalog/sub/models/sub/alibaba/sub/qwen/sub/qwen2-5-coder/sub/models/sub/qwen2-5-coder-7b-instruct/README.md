# Qwen2.5-Coder 7B Instruct

Qwen2.5-Coder 7B Instruct is a coding-specialized instruction-tuned language model in the Qwen2.5-Coder series.

## Model series

- [Qwen2.5-Coder](../../../..)

## Model profile

- Architecture: dense decoder-only Transformer
- Parameters: 7.61B total; 6.53B excluding embeddings
- Layers: 28
- Context length: 131,072 tokens
- Training stage: pretraining and post-training
- License: Apache-2.0
- Inputs and outputs: text input and generated text output

## Scope boundary

This canonical page owns Qwen2.5-Coder 7B Instruct identity and intrinsic model facts. The contextual AI Lab `SLM` label, stronger-compact-local positioning, local/self-hosted recommendations, hardware and runtime fit, autonomous repository-work suitability, validation guidance, throughput, ecosystem maturity, frontier status, and accepted-result cost belong to classification/reference, selection, deployment/workflow, or evidence documentation.

## Decision and Operational Boundaries

Qwen2.5-Coder-7B-Instruct is the 7.61B-parameter dense instruction-tuned text model under Apache-2.0.

- Distinguish the shipped 32,768-position configuration from the card's 131,072-token YaRN extension; extension requires runtime configuration and is not an automatic memory guarantee.
- Keep checkpoint identity separate from quantization and runtime packaging; pin the chosen revision and validate processor, chat-template, reasoning-parser, and tool-parser support in the selected runtime.
- Keep model-generated text, code, and tool arguments separate from permission to execute them; the application owns command validation, tool access, network access, and sandboxing.

## Official resources

- [Qwen2.5-Coder 7B Instruct](https://huggingface.co/Qwen/Qwen2.5-Coder-7B-Instruct)
- [Qwen2.5-Coder family release](https://qwenlm.github.io/blog/qwen2.5-coder-family/)

## Relationships

| Relationship | Catalog page |
| --- | --- |
| Member of | [Qwen2.5-Coder](../../../../) |

## Primary Sources

- [Official model card or license: Qwen/Qwen2.5-Coder-7B-Instruct](https://huggingface.co/Qwen/Qwen2.5-Coder-7B-Instruct)
- [Official model card or license: Qwen/Qwen2.5-Coder-7B-Instruct/blob/main/config.json](https://huggingface.co/Qwen/Qwen2.5-Coder-7B-Instruct/blob/main/config.json)
