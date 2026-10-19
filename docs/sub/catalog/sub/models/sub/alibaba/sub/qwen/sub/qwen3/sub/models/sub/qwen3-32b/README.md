# Qwen3 32B

Qwen3 32B is a dense post-trained language model in the Qwen3 series.

## Model series

- [Qwen3](../../../..)

## Model profile

- Model repository: `Qwen/Qwen3-32B`
- Architecture: dense causal language model
- Parameters: 32.8B total; 31.2B excluding embeddings
- Layers: 64
- Attention heads (GQA): 64 query heads; 8 key/value heads
- Native context: 32,768 tokens
- Extended context: official guidance documents YaRN extension to 131,072 tokens
- License: Apache-2.0
- Training stage: pretraining and post-training

Official model material describes thinking/non-thinking interaction, multilingual support, reasoning, coding, instruction following, and tool-integrated agent capabilities. These are provider-described capabilities rather than independent AI Lab task evidence.

## Scope boundary

This canonical page owns Qwen3 32B identity and source-backed intrinsic model facts. Hardware fit, deployment configuration, artifact selection, runtime performance, and task-specific recommendation conclusions belong to their corresponding selection, deployment, artifact, or evidence owners.

## Decision and Operational Boundaries

Qwen3-32B is an Apache-2.0 dense text model with 32.8B total parameters and an initial hybrid-thinking interaction contract.

- Preserve the card's 32,768-token native context and separate 131,072-token YaRN extension; context scaling and memory requirements depend on the selected runtime.
- Keep checkpoint identity separate from quantization and runtime packaging; pin the chosen revision and validate processor, chat-template, reasoning-parser, and tool-parser support in the selected runtime.
- Keep model-generated text, code, and tool arguments separate from permission to execute them; the application owns command validation, tool access, network access, and sandboxing.

## Official resources

- [Qwen3 32B](https://huggingface.co/Qwen/Qwen3-32B)

## Relationships

| Relationship | Catalog page |
| --- | --- |
| Member of | [Qwen3](../../../../) |

## Primary Sources

- [Official model card or license: Qwen/Qwen3-32B](https://huggingface.co/Qwen/Qwen3-32B)
- [Official repository: QwenLM/Qwen3](https://github.com/QwenLM/Qwen3)
