# Qwen3

Qwen3 is a large-language-model series in the Qwen family developed by Qwen Team at Alibaba Cloud. The series includes distinct dense and Mixture of Experts (MoE) model identities rather than one executable model.

## Family and producer

- [Qwen](../..)
- [Qwen Team](../../../../../../../producers/sub/q/sub/qwen-team/)

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

## Decision and Operational Boundaries

Qwen3 contains distinct dense and mixture-of-experts language models, with initial hybrid-thinking releases and separate later revisions.

- Thinking support and context belong to the exact release: the initial 30B-A3B checkpoint supports both modes, whereas Instruct-2507 is non-thinking only.
- Do not equate active parameters, quantized file size, total model size, and peak runtime memory.
- Keep model-generated text, code, and tool arguments separate from permission to execute them; the application owns command validation, tool access, network access, and sandboxing.

## Official resources

- [Official repository](https://github.com/QwenLM/Qwen3)
- [Qwen3 technical report](https://arxiv.org/abs/2505.09388)
- [Qwen3 model collection](https://huggingface.co/collections/Qwen/qwen3-67dd247413f0e2e4f653967f)

## Relationships

| Relationship | Catalog page |
| --- | --- |
| Member of | [Qwen](../../) |
| Produced by | [Qwen Team](../../../../../../../producers/sub/q/sub/qwen-team/) |
| Includes | [Qwen3 14B](./sub/models/sub/qwen3-14b/) |
| Includes | [Qwen3 30B-A3B](./sub/models/sub/qwen3-30b-a3b/) |
| Includes | [Qwen3 32B](./sub/models/sub/qwen3-32b/) |
| Includes | [Qwen3 8B](./sub/models/sub/qwen3-8b/) |

## Primary Sources

- [Official repository: QwenLM/Qwen3](https://github.com/QwenLM/Qwen3)
- [Official model card or license: Qwen/Qwen3-30B-A3B](https://huggingface.co/Qwen/Qwen3-30B-A3B)
- [Official model card or license: Qwen/Qwen3-30B-A3B-Instruct-2507](https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507)
