# Gemma 4 E2B Instruct

Gemma 4 E2B Instruct is Google's smallest instruction-tuned Gemma 4 model for multimodal, multilingual, reasoning, coding, function-calling, and on-device workflows.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Classification

- Model type: general-purpose multimodal instruction-tuned language model
- Scale class: [SLM](../../../../../../../../../../../notes/sub/concepts/sub/model-classification/sub/language-model-scale/) in the current AI Lab local and edge comparison context
- Architecture: [Dense](../../../../../../../../../../../notes/sub/concepts/sub/model-architectures/sub/dense-and-sparse-architectures/) decoder-only Transformer with per-layer embeddings and hybrid local/global attention
- Frontier status: not assessed for this exact model and workload scope
- Ecosystem status: emerging; this is a recent generation and the exact runtime ecosystem remains under review

The SLM label is contextual. It does not prove adequate quality, low accepted-result cost, or fit on a specific phone, laptop, CPU, GPU, or NPU.

## Official profile

- Model repository: `google/gemma-4-E2B-it`
- Effective parameters: 2.3B
- Total parameters including embeddings: 5.1B
- Layers: 35
- Context length: 128K tokens
- Inputs: text, images, and audio; video can be processed as sampled frames
- Output: generated text
- Capabilities: configurable reasoning, multilingual generation, coding, function calling, OCR, document and UI understanding, and short audio processing
- License: Apache-2.0
- Full-precision model file: approximately 10.2 GB in the official Hugging Face repository at verification time

`E2B` records effective parameters rather than the complete stored parameter count. Keep the 2.3B effective and 5.1B total-with-embeddings figures separate.

## Official local QAT artifact

Google publishes `google/gemma-4-E2B-it-qat-q4_0-gguf` for llama.cpp-compatible local runtimes:

- Model file: `gemma-4-E2B_q4_0-it.gguf`, approximately 3.35 GB
- Multimodal projection: `gemma-4-E2B-it-mmproj.gguf`, approximately 987 MB
- Combined repository size: approximately 4.34 GB
- Quantization: official QAT Q4_0
- License: Apache-2.0

The multimodal projection is a separate required component for multimodal use. Published file sizes are not peak RAM or VRAM. Measure runtime buffers, context, KV cache, image and audio processing, batching, offload, and concurrent applications.

## Selection guidance

Consider this model for:

- economical local text, image, and short-audio experiments;
- private preprocessing, classification, extraction, summarization, or draft work;
- constrained multilingual assistants and function-calling prototypes;
- edge or laptop workflows where a larger model is operationally unsuitable;
- comparison against Phi-4 Mini, Gemma 4 E4B, Qwen3 8B, and hosted low-cost routes.

Escalate when representative tests show repeated omissions, weak domain accuracy, unreliable tool arguments, insufficient visual detail, poor audio transcription, or excessive human correction. Do not infer autonomous-agent reliability from native function calling or provider benchmark claims.

## Evidence boundary

Identity, parameter figures, architecture, context, modalities, license, and published artifact sizes were verified from official Google and Hugging Face sources on 2026-07-27. The SLM and emerging labels are repository comparison judgments. Hardware fit, throughput, task quality, frontier status, and cost per accepted result require exact artifact and runtime measurement.

## Related pages

- [Gemma 4](../..)
- [Gemma model family](../../../..)
- [Google models](../../../../../..)
- [Small and Large Language Models](../../../../../../../../../../../notes/sub/concepts/sub/model-classification/sub/language-model-scale/)
- [Dense and Sparse Architectures](../../../../../../../../../../../notes/sub/concepts/sub/model-architectures/sub/dense-and-sparse-architectures/)
- [Local Model Selection by VRAM](../../../../../../../../../../../notes/sub/comparisons/sub/model-selection/sub/local-models-by-vram/)

## Sources

- [Gemma 4 model card](https://ai.google.dev/gemma/docs/core/model_card_4)
- [Gemma 4 E2B Instruct on Hugging Face](https://huggingface.co/google/gemma-4-E2B-it)
- [Gemma 4 E2B QAT Q4_0 GGUF](https://huggingface.co/google/gemma-4-E2B-it-qat-q4_0-gguf)
- [Gemma 4 technical report](https://arxiv.org/abs/2607.02770)
