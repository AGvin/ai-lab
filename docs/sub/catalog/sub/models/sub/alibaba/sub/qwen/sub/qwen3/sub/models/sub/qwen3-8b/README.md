# Qwen3 8B

Qwen3 8B is a dense post-trained language model in the Qwen3 series.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Model series

- [Qwen3](../../../..)

## Model profile

- Architecture: dense causal language model
- Parameters: 8.2B total; 6.95B excluding embeddings
- Layers: 36
- Native context: 32,768 tokens
- Extended context: official guidance documents YaRN extension to 131,072 tokens
- License: Apache-2.0
- Training stage: pretraining and post-training

Official model material describes thinking and non-thinking modes, multilingual support, reasoning, coding, instruction following, and tool-integrated agent capabilities. These are provider-described capabilities and do not replace workload-specific evaluation.

## Official GGUF artifact

The official `Qwen/Qwen3-8B-GGUF` repository publishes multiple quantizations. The legacy AI Lab model page records `Qwen3-8B-Q4_K_M.gguf` with a published file size of 5.03 GB.

Published artifact size is not peak VRAM or total runtime memory. Runtime buffers, key-value cache, context length, batching, GPU offload, and concurrent services remain separate deployment considerations.

## Scope boundary

This canonical page owns Qwen3 8B identity, intrinsic architecture and release facts, official references, and artifact identity that is useful for understanding the model. Hardware-fit recommendations, model-selection guidance, agent-role suitability, runtime performance, and accepted-result conclusions belong to selection, deployment/workflow, or evidence documentation.

## Official resources

- [Qwen3 8B](https://huggingface.co/Qwen/Qwen3-8B)
- [Qwen3 8B GGUF](https://huggingface.co/Qwen/Qwen3-8B-GGUF)
