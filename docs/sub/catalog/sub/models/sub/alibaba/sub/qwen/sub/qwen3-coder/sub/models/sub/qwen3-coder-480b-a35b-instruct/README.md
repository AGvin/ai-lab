# Qwen3-Coder 480B-A35B Instruct

Qwen3-Coder 480B-A35B Instruct is a Mixture of Experts (MoE) coding model in the Qwen3-Coder series.

## Model series

- [Qwen3-Coder](../../../..)

## Model profile

- Architecture: Mixture of Experts (MoE)
- Parameters: 480B total; 35B active
- Native context: 256K tokens
- Extended context: the launch material describes extrapolation methods supporting up to one million tokens
- License: Apache-2.0

The active-parameter count does not represent the model's total storage, memory requirement, or scale by itself.

Qwen Team positions this model for coding agents, tool use, and repository-scale coding workflows. Those use cases are provider positioning rather than independent AI Lab quality validation.

## Scope boundary

This canonical page owns the model's identity, architecture/parameter/context/license facts, official references, and Qwen3-Coder series membership. Hosted deployment details, infrastructure and hardware fit, runtime behavior, cost, and cross-model selection conclusions belong to service/deployment, selection, or evidence documentation.

## Decision and Operational Boundaries

Qwen3-Coder-480B-A35B-Instruct is an Apache-2.0, text-only, non-thinking coding model with 480B total and 35B active parameters.

- Keep the 262,144-token native context distinct from optional extensions and service quotas; preserve the exact checkpoint's non-thinking-only contract.
- Active parameter count does not establish model storage or peak serving memory.
- Keep checkpoint identity separate from quantization and runtime packaging; pin the chosen revision and validate processor, chat-template, reasoning-parser, and tool-parser support in the selected runtime.
- Keep model-generated text, code, and tool arguments separate from permission to execute them; the application owns command validation, tool access, network access, and sandboxing.

## Official resources

- [Qwen3-Coder 480B-A35B Instruct](https://huggingface.co/Qwen/Qwen3-Coder-480B-A35B-Instruct)
- [Qwen3-Coder launch](https://qwenlm.github.io/blog/qwen3-coder/)

## Relationships

| Relationship | Catalog page |
| --- | --- |
| Member of | [Qwen3-Coder](../../../../) |

## Primary Sources

- [Official model card or license: Qwen/Qwen3-Coder-480B-A35B-Instruct](https://huggingface.co/Qwen/Qwen3-Coder-480B-A35B-Instruct)
- [Official repository: QwenLM/Qwen3-Coder](https://github.com/QwenLM/Qwen3-Coder)
