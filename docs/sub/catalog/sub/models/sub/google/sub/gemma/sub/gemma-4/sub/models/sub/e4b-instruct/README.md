# Gemma 4 E4B Instruct

Gemma 4 E4B Instruct is a dense instruction-tuned multimodal model in the Gemma 4 series.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Model series

- [Gemma 4](../../../..)

## Model profile

- Architecture: dense hybrid-attention model
- Effective parameters: 4.5B
- Parameters including embeddings: 8B
- Layers: 42
- Sliding window: 512 tokens
- Context length: 128K tokens
- Input: text, image, and audio
- Output: text
- Vision encoder: approximately 150M parameters
- Audio encoder: approximately 300M parameters
- License: Apache-2.0

`E4B` denotes effective parameters. The larger parameter figure includes per-layer embeddings; neither value should be silently substituted for artifact size or runtime memory requirements.

## Official QAT distributions

Google publishes multiple distinct QAT-related distributions for this model. Keep them separate rather than treating one file-size figure as the size of every QAT artifact.

### QAT-trained unquantized Safetensors

- Repository: `google/gemma-4-E4B-it-qat-q4_0-unquantized`
- Primary weights file: `model.safetensors`
- Hub-reported weights size verified 2026-08-11: 15.9 GB

The repository name records the QAT training lineage, but this distribution is stored as the unquantized Safetensors checkpoint. Its file size is not the size of the separate GGUF package below.

### QAT Q4_0 GGUF

- Repository: `google/gemma-4-E4B-it-qat-q4_0-gguf`
- Q4_0 model file: `gemma-4-E4B_q4_0-it.gguf`
- Hub-reported model-file size verified 2026-08-11: 5.15 GB
- Multimodal projector: `gemma-4-E4B-it-mmproj.gguf`
- Hub-reported projector size verified 2026-08-11: 992 MB

The projector is a separate required component for the GGUF multimodal path represented by this repository. Do not omit it when estimating downloadable files for multimodal use.

Published repository or file size is not a complete RAM or VRAM requirement. Runtime buffers, key-value cache, context length, batching, GPU offload, multimodal processing, and concurrency remain deployment considerations.

## Scope boundary

This canonical page owns E4B identity, source-backed intrinsic model facts, official references, and represented artifact identities. Hardware fit, VRAM planning, runtime compatibility, quantization performance, throughput, latency, quality, and selection conclusions belong to artifact/deployment, selection, or evidence documentation.

## Official resources

- [Gemma 4 model card](https://ai.google.dev/gemma/docs/core/model_card_4)
- [Gemma 4 E4B Instruct](https://huggingface.co/google/gemma-4-E4B-it)
- [Gemma 4 E4B QAT-trained unquantized checkpoint](https://huggingface.co/google/gemma-4-E4B-it-qat-q4_0-unquantized)
- [Gemma 4 E4B QAT Q4_0 GGUF](https://huggingface.co/google/gemma-4-E4B-it-qat-q4_0-gguf)
