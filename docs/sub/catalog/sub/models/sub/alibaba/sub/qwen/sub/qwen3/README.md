# Qwen3

Qwen3 is a large-language-model series in the Qwen family developed by Qwen Team at Alibaba Cloud. The series includes distinct dense and Mixture of Experts (MoE) model identities rather than one executable model.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Family and producer

- [Qwen](../..)
- [Qwen Team](../../../../../../../../../producers/sub/q/sub/qwen-team/)

## Series scope

The initial Qwen3 release (also identified upstream as Qwen3-2504) introduced multiple dense and MoE sizes with hybrid thinking/non-thinking interaction, multilingual support, and Apache-2.0 open-weight releases. Later Qwen3-2507 updates are revisioned releases and must not be flattened into the initial model facts.

The currently materialized models are:

- [Qwen3 8B](./sub/models/sub/qwen3-8b/) — dense 8.2B-parameter model.
- [Qwen3 14B](./sub/models/sub/qwen3-14b/) — dense 14.8B-parameter model.
- [Qwen3 30B-A3B](./sub/models/sub/qwen3-30b-a3b/) — MoE model with 30.5B total and 3.3B activated parameters in the initial release; revision-specific behavior lives under its version nodes.
- [Qwen3 32B](./sub/models/sub/qwen3-32b/) — dense 32.8B-parameter model.

For the represented initial 8B, 14B, 30B-A3B, and 32B model cards, upstream documents 32,768-token native context and YaRN-based extension to 131,072 tokens. Do not generalize that context profile to later Qwen3 revisions whose official cards publish different limits.

Active parameters for MoE models are not total storage or memory requirements. Artifact quantization, runtime, cache, context, batching, and deployment configuration remain separate operational dimensions.

## Scope boundary

This page owns Qwen3 series identity and genuinely shared series context. Exact architecture, parameter counts, version-specific context or reasoning behavior, artifacts, and limitations belong to the corresponding model/version pages. Model rankings, hardware-fit conclusions, local-versus-hosted recommendations, and workload suitability belong to selection or evidence documentation.

## Official resources

- [Official repository](https://github.com/QwenLM/Qwen3)
- [Qwen3 technical report](https://arxiv.org/abs/2505.09388)
- [Qwen3 model collection](https://huggingface.co/collections/Qwen/qwen3-67dd247413f0e2e4f653967f)
