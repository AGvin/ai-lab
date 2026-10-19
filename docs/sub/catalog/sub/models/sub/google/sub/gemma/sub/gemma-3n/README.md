# Gemma 3n

Open Gemma series with E2B and E4B effective-parameter variants for text, image, video, and audio input with text output; effective size is smaller than total parameter count.

## Relations

- Member of: [Gemma](../../)

## Source-scoped operating boundaries

- The model card specifies a 32K combined input/output context. E2B/E4B are effective compute-size labels, not total-weight counts or runtime-memory requirements. [Gemma 3n model card](https://ai.google.dev/gemma/docs/gemma-3n/model_card).
- Multimodal input produces text, not generated speech or images. Runtime modality support and offline behavior depend on the selected artifact and integration; local-capable weights do not guarantee that an application sends no data elsewhere. [Model input/output boundary](https://ai.google.dev/gemma/docs/gemma-3n/model_card).

## Official resources

- <https://deepmind.google/models/gemma/gemma-3n/>
- <https://ai.google.dev/gemma/docs/releases>
- <https://ai.google.dev/gemma/docs/gemma-3n/model_card>
