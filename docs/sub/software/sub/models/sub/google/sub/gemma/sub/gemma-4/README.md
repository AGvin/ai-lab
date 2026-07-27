# Gemma 4 Model Generation

Gemma 4 is a Google DeepMind generation of open-weight multimodal models with dense and Mixture-of-Experts variants for edge, laptop, workstation, and server deployments.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Shared generation profile

- Provider: Google DeepMind
- License: Apache-2.0
- Variants: pre-trained and instruction-tuned
- Model types: general-purpose multimodal language models with reasoning, coding, function calling, and text generation
- Inputs: text and image for all documented sizes; audio for E2B, E4B, and 12B; video through frame sequences
- Output: generated text
- Languages: multilingual training across more than 140 languages
- Context: 128K tokens for E2B and E4B; 256K for 12B, 26B A4B, and 31B
- Architectures: dense E2B, E4B, 12B, and 31B models plus a sparse MoE 26B A4B model

## Documented models

- [Gemma 4 E2B Instruct](./sub/e2b-instruct/) — compact dense multimodal SLM with 2.3B effective parameters and official local QAT artifacts.
- [Gemma 4 E4B Instruct](./sub/e4b-instruct/) — stronger compact dense multimodal SLM with 4.5B effective parameters and official local QAT artifacts.

Other Gemma 4 sizes should receive canonical pages only when a comparison or practical note depends on their exact identity.

## Classification boundary

The `E` in E2B and E4B means effective parameters. Google documents larger totals when per-layer embedding tables are included. Record both figures rather than presenting one as the complete parameter identity.

For the MoE variant, record total and active parameters separately. Active parameters do not determine storage, memory residency, scale class, or local hardware fit.

Scale, architecture, modality, deployment, access, and task suitability remain independent dimensions.

## Local artifact boundary

Google publishes full-precision instruction-tuned repositories and official Quantization-Aware Training artifacts in several formats, including Q4_0 GGUF for llama.cpp-compatible local runtimes. A QAT or GGUF artifact remains a deployment representation of the underlying model and does not create a new scale class.

Record model and multimodal projection files together when both are required. File size is not peak RAM or VRAM; context, KV cache, runtime buffers, image or audio encoders, and concurrency remain material.

## Related pages

- [Gemma model family](../..)
- [Google models](../../../..)
- [Small and Large Language Models](../../../../../../../../../notes/sub/concepts/sub/model-classification/sub/language-model-scale/)
- [Dense and Sparse Architectures](../../../../../../../../../notes/sub/concepts/sub/model-architectures/sub/dense-and-sparse-architectures/)
- [Mixture of Experts](../../../../../../../../../notes/sub/concepts/sub/model-architectures/sub/mixture-of-experts/)

## Sources

- [Gemma 4 model card](https://ai.google.dev/gemma/docs/core/model_card_4)
- [Gemma 4 technical report](https://arxiv.org/abs/2607.02770)
- [Gemma 4 QAT guidance](https://ai.google.dev/gemma/docs/core)
