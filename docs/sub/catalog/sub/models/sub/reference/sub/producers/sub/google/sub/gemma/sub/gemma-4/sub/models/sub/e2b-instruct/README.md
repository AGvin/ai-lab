# Gemma 4 E2B Instruct

Gemma 4 E2B Instruct is a dense instruction-tuned multimodal model in the Gemma 4 series.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Model series

- [Gemma 4](../../../..)

## Model profile

- Architecture: dense hybrid-attention model
- Effective parameters: 2.3B
- Parameters including embeddings: 5.1B
- Layers: 35
- Sliding window: 512 tokens
- Context length: 128K tokens
- Input: text, image, and audio
- Output: text
- Vision encoder: approximately 150M parameters
- Audio encoder: approximately 300M parameters
- License: Apache-2.0

`E2B` denotes effective parameters. The larger parameter figure includes per-layer embeddings; neither value should be silently substituted for artifact size or runtime memory requirements.

## Official QAT artifact

The represented official Quantization-Aware Training (QAT) distribution is `google/gemma-4-e2b-it-qat-q4_0-unquantized`. The legacy source records a published file size of approximately 2.17 GB.

Published artifact size is not a complete RAM or VRAM requirement; runtime buffers, key-value cache, context length, multimodal encoders, and concurrency remain deployment considerations.

## Scope boundary

This canonical page owns E2B identity, source-backed intrinsic model facts, official references, and represented artifact identity. Hardware fit, VRAM planning, runtime compatibility, quantization performance, throughput, latency, quality, and selection conclusions belong to artifact/deployment, selection, or evidence documentation.

## Official resources

- [Gemma 4 model card](https://ai.google.dev/gemma/docs/core/model_card_4)
- [Gemma 4 E2B Instruct](https://huggingface.co/google/gemma-4-e2b-it)
- [Gemma 4 E2B Instruct QAT Q4_0](https://huggingface.co/google/gemma-4-e2b-it-qat-q4_0-unquantized)
