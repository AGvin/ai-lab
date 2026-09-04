# Qwen3-Coder 30B-A3B Instruct

Qwen3-Coder 30B-A3B Instruct is a concrete Mixture of Experts coding model in the Qwen3-Coder series.

## Translations

- English
- [Українська](./l10n/uk_UA/)

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

## Official resources

- [Qwen3-Coder 30B-A3B Instruct](https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct)
