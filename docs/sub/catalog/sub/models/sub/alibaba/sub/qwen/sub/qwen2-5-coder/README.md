# Qwen2.5-Coder

Qwen2.5-Coder is a coding-specialized model series in the Qwen family for code generation, code reasoning, code repair, and coding-assistant workflows.

## Family and producer

- [Qwen](../..)
- [Qwen Team](../../../../../../../producers/sub/q/sub/qwen-team/)

## Series profile

Official Qwen material describes Qwen2.5-Coder as a series of code-specific language models offered in multiple parameter sizes. The represented models use dense decoder-only Transformer architectures and include instruction-tuned releases.

Exact parameter counts, context length, training stage, and license belong to each concrete model rather than being generalized across the series.

## Models

- [Model index](./sub/models/)
- [Qwen2.5-Coder 3B Instruct](./sub/models/sub/qwen2-5-coder-3b-instruct/) — compact instruction-tuned coding model.
- [Qwen2.5-Coder 7B Instruct](./sub/models/sub/qwen2-5-coder-7b-instruct/) — larger instruction-tuned coding model.

## Scope boundary

This page owns Qwen2.5-Coder series identity, producer/family relations, and concrete-model navigation. Economical-local recommendations, runtime memory, throughput, retries, review effort, accepted-result quality, and artifact-specific deployment fit belong to selection, deployment/workflow, or evidence documentation.

## Decision and Operational Boundaries

Qwen2.5-Coder is a code-specialized language-model series with separately released model sizes.

- Keep the 3B Research License distinct from the 7B Apache-2.0 license; both license and context must be checked on the exact model.
- Do not transfer 7B long-context claims to the 3B model; preserve current 3B card limits even when historical cards differ.
- Keep model-generated text, code, and tool arguments separate from permission to execute them; the application owns command validation, tool access, network access, and sandboxing.

## Official resources

- [Qwen2.5-Coder family release](https://qwenlm.github.io/blog/qwen2.5-coder-family/)
- [Qwen2.5-Coder introduction](https://qwenlm.github.io/blog/qwen2.5-coder/)

## Relationships

| Relationship | Catalog page |
| --- | --- |
| Member of | [Qwen](../../) |
| Produced by | [Qwen Team](../../../../../../../producers/sub/q/sub/qwen-team/) |
| Includes | [Qwen2.5-Coder 3B Instruct](./sub/models/sub/qwen2-5-coder-3b-instruct/) |
| Includes | [Qwen2.5-Coder 7B Instruct](./sub/models/sub/qwen2-5-coder-7b-instruct/) |

## Primary Sources

- [qwenlm.github.io/blog/qwen2.5-coder-family/](https://qwenlm.github.io/blog/qwen2.5-coder-family/)
- [Official model card or license: Qwen/Qwen2.5-Coder-3B-Instruct](https://huggingface.co/Qwen/Qwen2.5-Coder-3B-Instruct)
- [Official model card or license: Qwen/Qwen2.5-Coder-7B-Instruct](https://huggingface.co/Qwen/Qwen2.5-Coder-7B-Instruct)
