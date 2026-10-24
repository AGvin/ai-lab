# Documentation Requirements

## Requirements

- Identify T5Gemma 2 as Google's released open encoder-decoder Gemma series based on Gemma 3, with current 270M, 1B, and 4B scale families.
- Preserve the encoder-decoder architecture boundary, multimodal/multilingual/long-context positioning, pre-trained distribution, and model-size inventory only while current first-party documentation supports them.
- Keep T5Gemma 2 distinct from earlier T5Gemma, decoder-only Gemma 3/4, generic T5, and downstream fine-tuned encoder-decoder derivatives.
- Keep encoder/decoder parameter accounting separate from total memory footprint and optional vision-encoder costs.
- Treat artifacts, licenses, runtime support, context limits, fine-tuning behavior, hardware fit, and provider benchmark comparisons as freshness-sensitive.
- Attribute reasoning, factuality, STEM/code, multilingual, multimodal, and long-context comparisons to Google DeepMind or the cited evaluator.

## Validation

- T5Gemma 2 remains a model series rather than one universal checkpoint.
- Size and memory claims preserve encoder/decoder accounting and evaluated configuration.

## Verified identity and provenance

Open pretrained encoder-decoder Gemma series based on Gemma 3, with 270M-270M, 1B-1B, and 4B-4B encoder/decoder size pairs; it is separate from earlier T5Gemma releases.

## Source-scoped operating boundaries

- T5Gemma 2 is distributed pretrained and supports a 128K context. Google's displayed post-training comparisons include supervised fine-tuning, so those results do not establish out-of-the-box instruction-following performance for the released pretrained checkpoint. [T5Gemma 2 release and evaluation scope](https://deepmind.google/models/gemma/t5gemma/).
- The encoder/decoder labels are size pairs, not a complete artifact or runtime-memory estimate. Shared embeddings, attention changes, and the optional vision encoder require separate accounting. [Architecture and size accounting](https://deepmind.google/models/gemma/t5gemma/).
- Fine-tuning and downstream safety or task validation remain deployment work; the model series is not itself a translation service, dialogue product, or application security boundary.

## Source evidence

- <https://deepmind.google/models/gemma/t5gemma/>
- <https://ai.google.dev/gemma/docs/releases>
