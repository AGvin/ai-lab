# Qwen3 30B-A3B

Qwen3 30B-A3B is a post-trained Mixture of Experts (MoE) language model in the Qwen3 series.

## Model series

- [Qwen3](../../../..)

## Model profile

- Architecture: mixture-of-experts causal language model
- Parameters: 30.5B total; 3.3B active per token
- Non-embedding parameters: 29.9B
- Experts: 128 total; 8 active per token
- Layers: 48
- Native context for the initial represented release: 32,768 tokens
- Extended context: official guidance documents YaRN extension to 131,072 tokens for the initial represented release
- License: Apache-2.0
- Training stage: pretraining and post-training

Official model material describes thinking and non-thinking modes, multilingual work, reasoning, coding, instruction following, and tool-integrated agent capabilities. These are provider-described capabilities and do not replace workload-specific evaluation.

The 3.3B active-parameter count does not make this model equivalent to a 3.3B dense model. Total weights, shared layers, expert routing, runtime implementation, context, and cache behavior remain material to storage, memory, and execution.

## Official GGUF artifact

The official `Qwen/Qwen3-30B-A3B-GGUF` repository publishes multiple quantizations. The legacy AI Lab model page records `Qwen3-30B-A3B-Q4_K_M.gguf` with a published size of approximately 18.6 GB.

Published artifact size is not peak VRAM or total runtime memory. Runtime buffers, key-value cache, context length, batching, GPU offload, and concurrent services remain separate deployment considerations.

## Versions

- [Initial release](./sub/versions/sub/initial/) — the original represented Qwen3 30B-A3B release with thinking and non-thinking interaction modes.
- [2507](./sub/versions/sub/2507/) — represented updated non-thinking instruction release.

Version-specific naming, behavior, and context differences belong on the corresponding version pages rather than being generalized across all releases.

## Scope boundary

This canonical page owns Qwen3 30B-A3B identity, intrinsic architecture facts, official references, artifact identity, and navigation to versions. Hardware-fit recommendations, loading strategy, comparisons against smaller or hosted models, runtime performance, and production-fit conclusions belong to selection, deployment/workflow, or evidence documentation.

## Decision and Operational Boundaries

Qwen3-30B-A3B is an Apache-2.0 MoE model with 30.5B total and 3.3B active parameters.

- Keep initial hybrid-thinking behavior and Instruct-2507 non-thinking behavior on their respective version owners; neither mode nor context is universal across the model's represented releases.
- Active parameters do not describe resident weights, KV cache, total RAM/VRAM, or equivalence to a dense 3B model.
- Keep model-generated text, code, and tool arguments separate from permission to execute them; the application owns command validation, tool access, network access, and sandboxing.

## Official resources

- [Qwen3 30B-A3B](https://huggingface.co/Qwen/Qwen3-30B-A3B)
- [Qwen3 30B-A3B GGUF](https://huggingface.co/Qwen/Qwen3-30B-A3B-GGUF)

## Relationships

| Relationship | Catalog page |
| --- | --- |
| Member of | [Qwen3](../../../../) |
| Has version | [Qwen3 30B-A3B Initial Release](./sub/versions/sub/initial/) |
| Has version | [Qwen3 30B-A3B Instruct 2507](./sub/versions/sub/2507/) |

## Primary Sources

- [Official model card or license: Qwen/Qwen3-30B-A3B](https://huggingface.co/Qwen/Qwen3-30B-A3B)
- [Official model card or license: Qwen/Qwen3-30B-A3B-Instruct-2507](https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507)
