# Gemma 4 E2B Instruct

Gemma 4 E2B Instruct is a dense instruction-tuned multimodal model in the Gemma 4 generation with 2B effective parameters.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Generation

- [Gemma 4](../../../..)

## Model profile

- Architecture: dense
- Effective parameters: 2B
- Context length: 128K tokens
- Input: text, image, and audio
- Output: text
- License: Apache-2.0

`E2B` denotes effective parameters. A distinct total-parameter figure is not inferred in this migration pass and should be added only after independent source confirmation.

## Official QAT artifact

The represented official Quantization-Aware Training (QAT) distribution is `google/gemma-4-e2b-it-qat-q4_0-unquantized`. The legacy source records a published file size of approximately 2.17 GB.

That file includes model tensors plus multimodal components such as the vision encoder. Published artifact size is not a complete RAM or VRAM requirement; runtime buffers, key-value cache, context length, encoder residency, and concurrency remain deployment considerations.

## Scope boundary

This canonical page owns E2B identity, intrinsic model facts, official references, and represented artifact identity. Contextual scale labels, hardware fit, VRAM planning, runtime compatibility, quantization performance, throughput, latency, quality, and model-selection conclusions belong to classification/reference, artifact/deployment, decision-support, or evidence documentation.

## Official resources

- [Gemma 4 E2B Instruct](https://huggingface.co/google/gemma-4-e2b-it)
- [Gemma 4 E2B Instruct QAT Q4_0](https://huggingface.co/google/gemma-4-e2b-it-qat-q4_0-unquantized)
