# Qwen3-Coder 30B-A3B Instruct

Qwen3-Coder 30B-A3B Instruct is a concrete Mixture of Experts coding model in the Qwen3-Coder series.

## Model series

- [Qwen3-Coder](../../../..)

## Canonical profile

- Model repository: `Qwen/Qwen3-Coder-30B-A3B-Instruct`
- Type: causal language model
- Architecture: Mixture of Experts (MoE)
- Parameters: 30.5B total; 3.3B active
- Layers: 48
- Attention heads (GQA): 32 query heads; 4 key/value heads
- Experts: 128 total; 8 active
- Native context: 262,144 tokens
- Extended context: provider guidance describes extension up to 1M tokens with YaRN
- Reasoning mode: non-thinking only
- Training stage: pretraining and post-training
- License: Apache-2.0

The 3.3B active-parameter count is not the model's total storage or memory requirement and does not make this model equivalent to a 3.3B dense model.

Qwen positions the model for agentic coding, browser use, repository-scale context, and tool calling. Those are provider-described capabilities rather than independent AI Lab task evidence.

## Lineage role

This model is the documented base model for community derivatives such as `huihui-ai/Huihui-Qwen3-Coder-30B-A3B-Instruct-abliterated`. Derivative modification, refusal/alignment changes, and artifact packaging belong to those derivative entities rather than this base profile.

## Scope boundary

This page owns exact base-model identity and source-backed architecture, scale, context, reasoning, training-stage, and license facts. Runtime choice, quantization, memory fit, hosted availability, workload ranking, and accepted-result conclusions belong to artifact/deployment, selection, or evidence owners.

## Decision and Operational Boundaries

Qwen3-Coder-30B-A3B-Instruct is an Apache-2.0, text-only, non-thinking coding model with 30.5B total and 3.3B active parameters.

- Keep the 262,144-token native context distinct from optional extensions and service quotas; preserve the exact checkpoint's non-thinking-only contract.
- Active parameter count does not establish model storage or peak serving memory.
- Keep checkpoint identity separate from quantization and runtime packaging; pin the chosen revision and validate processor, chat-template, reasoning-parser, and tool-parser support in the selected runtime.
- Keep model-generated text, code, and tool arguments separate from permission to execute them; the application owns command validation, tool access, network access, and sandboxing.
- Retain derivative lineage separately; a downstream abliterated model's modifications or safety behavior are not properties of this original checkpoint.

## Official resources

- [Qwen3-Coder 30B-A3B Instruct](https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct)

## Relationships

| Relationship | Catalog page |
| --- | --- |
| Has derivative | [Huihui Qwen3 Coder 30B A3B Instruct Abliterated](../../../../../../../../../huihui-ai/sub/qwen3-coder-derived/sub/models/sub/huihui-qwen3-coder-30b-a3b-instruct-abliterated/) |
| Member of | [Qwen3-Coder](../../../../) |

## Primary Sources

- [Official model card or license: Qwen/Qwen3-Coder-30B-A3B-Instruct](https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct)
- [Official repository: QwenLM/Qwen3-Coder](https://github.com/QwenLM/Qwen3-Coder)
