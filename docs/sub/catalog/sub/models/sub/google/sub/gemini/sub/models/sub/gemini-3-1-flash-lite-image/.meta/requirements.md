# Documentation Requirements

## Requirements

- Identify Gemini 3.1 Flash Lite Image (`gemini-3.1-flash-lite-image`, Nano Banana 2 Lite) as Google's generally available low-latency/cost-efficient image generation and editing model released on 2026-06-30.
- Preserve the model identity separately from product nicknames, image-generation API workflows, and later Gemini image models.
- Keep mutable limits, pricing, supported image operations, and serving availability source-scoped.

## Validation

- The GA model is not described as preview.
- Nano Banana 2 Lite is treated as an alias/product nickname rather than a separate trained-model identity.

## Verified identity and provenance

Stable Gemini image-generation and editing model served as gemini-3.1-flash-lite-image and also named Nano Banana 2 Lite; the nickname is not another trained model.

## Source-scoped operating boundaries

- The current API accepts text, image, video, and PDF input and returns image/text. It generates at 1K only; 2K and 4K are unsupported. Function calling, grounding, and Live API are not supported. [Model reference](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-image).
- SynthID is always enabled and the model supports C2PA provenance. These signals identify generated content; they do not establish factual accuracy or permission to use a depicted subject. Treat Google's latency target as provider guidance, not a deployment guarantee. [Output provenance and limits](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-image).

## Source evidence

- <https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-image>
