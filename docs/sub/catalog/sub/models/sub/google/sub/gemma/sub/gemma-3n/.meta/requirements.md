# Documentation Requirements

## Requirements

- Identify Gemma 3n as Google's released mobile-first/open Gemma series for local multimodal use on phones, tablets, and laptops.
- Preserve current E2B/E4B series identity, text/audio/image/video understanding, transcription/translation capability, and reduced-memory/on-device positioning only while first-party sources support them.
- Keep Gemma 3n distinct from Gemma 3, Gemma 4, Gemini Nano, specialized Gemma variants, device applications, and runtime-specific optimized artifacts.
- Treat model variants, effective-vs-total parameter accounting, context limits, artifacts, licenses, runtime support, quantization, device/hardware fit, latency, memory, and benchmark results as freshness-sensitive.
- Do not infer guaranteed offline/privacy properties for every downstream application merely from local-capable model distribution.

## Validation

- Gemma 3n remains a model series rather than a generic on-device AI concept.
- Device-fit claims remain tied to the exact variant, runtime, precision, and hardware.

## Verified identity and provenance

Open Gemma series with E2B and E4B effective-parameter variants for text, image, video, and audio input with text output; effective size is smaller than total parameter count.

## Source-scoped operating boundaries

- The model card specifies a 32K combined input/output context. E2B/E4B are effective compute-size labels, not total-weight counts or runtime-memory requirements. [Gemma 3n model card](https://ai.google.dev/gemma/docs/gemma-3n/model_card).
- Multimodal input produces text, not generated speech or images. Runtime modality support and offline behavior depend on the selected artifact and integration; local-capable weights do not guarantee that an application sends no data elsewhere. [Model input/output boundary](https://ai.google.dev/gemma/docs/gemma-3n/model_card).

## Source evidence

- <https://ai.google.dev/gemma/docs/gemma-3n/model_card>
- <https://deepmind.google/models/gemma/gemma-3n/>
