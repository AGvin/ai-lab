# Qwen3 14B

Qwen3 14B is a dense post-trained language model in the Qwen3 series.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Model series

- [Qwen3](../../../..)

## Model profile

- Architecture: dense causal language model
- Parameters: 14.8B total; 13.2B excluding embeddings
- Layers: 40
- Native context: 32,768 tokens
- Extended context: official guidance documents YaRN extension to 131,072 tokens
- License: Apache-2.0
- Training stage: pretraining and post-training

Official model material describes thinking and non-thinking modes, multilingual instruction following, translation, reasoning, coding, and tool-integrated agent capabilities. These are provider-described capabilities and do not replace workload-specific evaluation.

## Official GGUF artifact

The official `Qwen/Qwen3-14B-GGUF` repository publishes multiple quantizations. The legacy AI Lab model page records a `Q4_K_M` artifact with a published size of approximately 9 GB.

Published artifact size is not peak VRAM or total runtime memory. Runtime buffers, key-value cache, context length, batching, GPU offload, and concurrent services remain separate deployment considerations.

## Scope boundary

This canonical page owns Qwen3 14B identity, intrinsic architecture and release facts, official references, and artifact identity useful for understanding the model. Hardware-fit recommendations, resident-model strategy, orchestration suitability, hybrid-routing advice, runtime performance, and accepted-result conclusions belong to selection, deployment/workflow, or evidence documentation.

## Official resources

- [Qwen3 14B](https://huggingface.co/Qwen/Qwen3-14B)
- [Qwen3 14B GGUF](https://huggingface.co/Qwen/Qwen3-14B-GGUF)
