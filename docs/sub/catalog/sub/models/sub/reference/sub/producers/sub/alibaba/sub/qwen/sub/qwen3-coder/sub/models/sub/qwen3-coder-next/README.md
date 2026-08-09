# Qwen3-Coder-Next

Qwen3-Coder-Next is a concrete open-weight coding-agent model in the Qwen3-Coder line.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Model line

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

This canonical page owns the model's identity, intrinsic architecture/parameter/context/reasoning/license facts, official references, and Qwen3-Coder membership. Direct-use and serving instructions, tensor-parallel deployment, context-reduction troubleshooting, consumer-hardware fit, quantized-artifact behavior, contextual LLM/frontier/ecosystem labels, and task-specific evaluation belong to future deployment/workflow, classification/reference, decision-support, or evidence documentation.

## Official resources

- [Qwen3-Coder-Next](https://huggingface.co/Qwen/Qwen3-Coder-Next)
- [Qwen3-Coder-Next technical report](https://github.com/QwenLM/Qwen3-Coder/blob/main/qwen3_coder_next_tech_report.pdf)
