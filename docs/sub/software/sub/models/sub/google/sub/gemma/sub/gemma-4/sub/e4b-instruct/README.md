# Gemma 4 E4B Instruct

Gemma 4 E4B Instruct is a compact Google instruction-tuned model for stronger multimodal, multilingual, reasoning, coding, function-calling, and on-device workflows than the E2B route.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Classification

- Model type: general-purpose multimodal instruction-tuned language model
- Scale class: [SLM](../../../../../../../../../../../notes/sub/concepts/sub/model-classification/sub/language-model-scale/) in the current AI Lab local and edge comparison context
- Architecture: [Dense](../../../../../../../../../../../notes/sub/concepts/sub/model-architectures/sub/dense-and-sparse-architectures/) decoder-only Transformer with per-layer embeddings and hybrid local/global attention
- Frontier status: not assessed for this exact model and workload scope
- Ecosystem status: emerging; this is a recent generation and the exact runtime ecosystem remains under review

The SLM label is contextual. It remains separate from full artifact size, practical hardware fit, multimodal encoder cost, quality, and total operating cost.

## Official profile

- Model repository: `google/gemma-4-E4B-it`
- Effective parameters: 4.5B
- Total parameters including embeddings: 8B
- Layers: 42
- Context length: 128K tokens
- Inputs: text, images, and audio; video can be processed as sampled frames
- Output: generated text
- Capabilities: configurable reasoning, multilingual generation, coding, function calling, OCR, document and UI understanding, and short audio processing
- License: Apache-2.0
- Full-precision model file: approximately 16 GB in the official Hugging Face repository at verification time

`E4B` records effective parameters rather than the complete stored parameter count. Keep the 4.5B effective and 8B total-with-embeddings figures separate.

## Official local QAT artifact

Google publishes `google/gemma-4-E4B-it-qat-q4_0-gguf` for llama.cpp-compatible local runtimes:

- Model file: `gemma-4-E4B_q4_0-it.gguf`, approximately 5.15 GB
- Multimodal projection: `gemma-4-E4B-it-mmproj.gguf`, approximately 992 MB
- Combined repository size: approximately 6.15 GB
- Quantization: official QAT Q4_0
- License: Apache-2.0

The multimodal projection is a separate required component for multimodal use. Published file sizes are not peak RAM or VRAM. Measure runtime buffers, context, KV cache, image and audio processing, batching, offload, and concurrent applications.

## Selection guidance

Consider this model for:

- a stronger compact local generalist when Gemma 4 E2B is below the acceptance threshold;
- private text, image, document, UI, and short-audio workflows;
- multilingual assistance, coding, extraction, and structured function-calling experiments;
- laptop or edge deployments where larger open models are impractical;
- comparison against Phi-4 Mini, Qwen3 8B, and hosted economical routes.

Prefer E2B when measured quality remains sufficient and lower resource demand matters more. Escalate beyond E4B when complex reasoning, long agent loops, repository-scale coding, high-detail OCR, or repeated correction exceeds the compact route's demonstrated capability.

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
- [Gemma 4 E4B Instruct on Hugging Face](https://huggingface.co/google/gemma-4-E4B-it)
- [Gemma 4 E4B QAT Q4_0 GGUF](https://huggingface.co/google/gemma-4-E4B-it-qat-q4_0-gguf)
- [Gemma 4 technical report](https://arxiv.org/abs/2607.02770)
