# Documentation Requirements

## Requirements

- Identify EmbeddingGemma 2 as Google DeepMind's released open multimodal embedding model in the Gemma family, released on 2026-10-06.
- Preserve the current unified text/code/image/video/audio embedding boundary, 768-dimensional native embedding space, Matryoshka truncation support, modular vision/audio encoders, and 8K context only while first-party documentation supports those facts.
- Keep total, text-backbone, embedder, vision-encoder, and audio-encoder parameter counts distinct; do not use one component count as a shortcut for total memory or deployment fit.
- Keep Hugging Face/Kaggle/Google AI Edge distribution, Sentence Transformers integration, fine-tuning recipes, precision/quantization, runtime support, and device-performance claims as freshness-sensitive deployment facts rather than permanent model identity.
- Preserve Apache-2.0/open-weight status only while current official distribution and licensing material supports it.
- Attribute benchmark, multilingual/code improvement, storage-efficiency, and on-device performance claims to Google DeepMind or the cited evaluator.

## Validation

- The node represents the concrete EmbeddingGemma 2 model rather than generic embedding methodology or the Gemma family as a whole.
- Multimodal encoder optionality is not misread as separate trained-model identities.
- Benchmark results remain scoped to the exact model artifact and evaluation configuration.
