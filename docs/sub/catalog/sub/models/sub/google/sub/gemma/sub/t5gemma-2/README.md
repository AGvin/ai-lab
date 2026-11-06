# T5Gemma 2

Open pretrained encoder-decoder Gemma series based on Gemma 3, with 270M-270M, 1B-1B, and 4B-4B encoder/decoder size pairs; it is separate from earlier T5Gemma releases.

## Relations

- Member of: [Gemma](../../)

## Source-scoped operating boundaries

- T5Gemma 2 is distributed pretrained and supports a 128K context. Google's displayed post-training comparisons include supervised fine-tuning, so those results do not establish out-of-the-box instruction-following performance for the released pretrained checkpoint. [T5Gemma 2 release and evaluation scope](https://deepmind.google/models/gemma/t5gemma/).
- The encoder/decoder labels are size pairs, not a complete artifact or runtime-memory estimate. Shared embeddings, attention changes, and the optional vision encoder require separate accounting. [Architecture and size accounting](https://deepmind.google/models/gemma/t5gemma/).
- Fine-tuning and downstream safety or task validation remain deployment work; the model series is not itself a translation service, dialogue product, or application security boundary.

## Official resources

- <https://deepmind.google/models/gemma/t5gemma/>
- <https://ai.google.dev/gemma/docs/releases>
