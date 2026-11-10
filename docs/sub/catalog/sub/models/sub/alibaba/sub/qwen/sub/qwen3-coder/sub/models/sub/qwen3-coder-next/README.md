# Qwen3-Coder-Next

Qwen3-Coder-Next is a concrete open-weight coding-agent model in the Qwen3-Coder series.

## Model series

- [Qwen3-Coder](../../../..)

## Model profile

- Type: causal language model
- Architecture: hybrid Gated DeltaNet, gated attention, and Mixture of Experts (MoE)
- Parameters: 80B total; 3B active
- Native context: 262,144 tokens
- Reasoning mode: non-thinking only
- License: Apache-2.0

The 3B active-parameter count does not make this model equivalent to a 3B dense model and must not be interpreted as its total storage, RAM, or VRAM requirement.

Qwen Team positions Qwen3-Coder-Next for coding agents, long-horizon coding tasks, complex tool use, and recovery from execution failures. These are provider-described use cases rather than independently validated AI Lab quality conclusions.

## Scope boundary

This canonical page owns the model's identity, intrinsic architecture/parameter/context/reasoning/license facts, official references, and Qwen3-Coder series membership. Serving instructions, tensor-parallel deployment, hardware fit, quantized-artifact behavior, and task-specific evaluation belong to deployment/workflow, artifact, selection, or evidence documentation.

## Decision and Operational Boundaries

Qwen3-Coder-Next is an Apache-2.0, text-only, non-thinking coding model with 80B total and 3B active parameters.

- Keep the 262,144-token native context distinct from optional extensions and service quotas; preserve the exact checkpoint's non-thinking-only contract.
- Active parameter count does not establish model storage or peak serving memory.
- Keep checkpoint identity separate from quantization and runtime packaging; pin the chosen revision and validate processor, chat-template, reasoning-parser, and tool-parser support in the selected runtime.
- Keep model-generated text, code, and tool arguments separate from permission to execute them; the application owns command validation, tool access, network access, and sandboxing.

## Official resources

- [Qwen3-Coder-Next](https://huggingface.co/Qwen/Qwen3-Coder-Next)
- [Qwen3-Coder-Next technical report](https://github.com/QwenLM/Qwen3-Coder/blob/main/qwen3_coder_next_tech_report.pdf)

## Relationships

| Relationship | Catalog page |
| --- | --- |
| Member of | [Qwen3-Coder](../../../../) |

## Primary Sources

- [Official model card or license: Qwen/Qwen3-Coder-Next](https://huggingface.co/Qwen/Qwen3-Coder-Next)
- [Official repository: QwenLM/Qwen3-Coder](https://github.com/QwenLM/Qwen3-Coder)
