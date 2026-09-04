# Qwen3 30B-A3B

Qwen3 30B-A3B is a post-trained Mixture of Experts (MoE) language model in the Qwen3 series.

## Translations

- English
- [Українська](./l10n/uk_UA/)

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

## Official resources

- [Qwen3 30B-A3B](https://huggingface.co/Qwen/Qwen3-30B-A3B)
- [Qwen3 30B-A3B GGUF](https://huggingface.co/Qwen/Qwen3-30B-A3B-GGUF)
