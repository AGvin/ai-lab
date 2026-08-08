# Qwen3

Qwen3 is a Qwen language-model generation developed by Qwen Team at Alibaba Cloud. The represented releases include dense and Mixture of Experts (MoE) models for reasoning, instruction following, multilingual work, coding, and tool-integrated agent workflows.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Canonical producer

- [Qwen Team](../../../../../../../../../producers/sub/q/sub/qwen-team/)

## Shared characteristics

Official Qwen3 material describes the represented post-trained models as supporting:

- thinking and non-thinking response modes;
- multilingual instruction following and translation across more than 100 languages and dialects;
- coding, mathematical, and general reasoning workloads;
- external-tool integration and agent-oriented tasks;
- Apache-2.0 licensed downloadable weights for the represented variants.

For the represented Qwen3 8B, 14B, and 30B-A3B models, the documented native context window is 32,768 tokens. Official guidance describes YaRN-based extension to 131,072 tokens. Extended context is a deployment option and does not by itself establish acceptable quality, latency, or memory use for a workload.

## Architecture variants

- **Dense** — Qwen3 8B and Qwen3 14B are represented as dense models.
- **Mixture of Experts (MoE)** — Qwen3 30B-A3B is represented as an MoE model with a smaller active-parameter set per token than its total parameter count.

Total parameters, active parameters, quantization, runtime, context length, cache size, batching, and implementation are separate operational dimensions. Active parameters must not be interpreted as the model's total storage or memory requirement.

## Models

- [Qwen3 8B](./sub/models/sub/qwen3-8b/) — dense 8.2B-parameter model.
- [Qwen3 14B](./sub/models/sub/qwen3-14b/) — dense 14.8B-parameter model.
- [Qwen3 30B-A3B](./sub/models/sub/qwen3-30b-a3b/) — MoE model with 30.5B total and 3.3B active parameters per token in the documented release.
- [Qwen3 32B](./sub/models/sub/qwen3-32b/) — represented in the RC catalog; its legacy source coverage still requires separate migration review.

## Scope boundary

This page owns Qwen3 generation-level identity and characteristics shared across represented concrete models. Model-selection guidance, VRAM planning, runtime-specific performance, local-versus-hosted recommendations, and workload suitability belong to decision-support, deployment/workflow, or evidence documentation rather than to the canonical model-family profile.

## Official resources

- [Official repository](https://github.com/QwenLM/Qwen3)
- [Qwen3 technical report](https://arxiv.org/abs/2505.09388)
- [Qwen3 model collection](https://huggingface.co/collections/Qwen/qwen3-67dd247413f0e2e4f653967f)
