# Documentation Requirements

## Requirements

- Identify Nano Banana 2.1 as the stable Gemini model `gemini-nano-banana-2.1`, released on 2026-10-06 and described by Google DeepMind as a member of the Gemini 3 series based on Gemini 3.6 Flash.
- Preserve current text/image/video/PDF input to image/text output, image-generation/editing behavior, search grounding, and thinking support only while current first-party documentation supports them.
- Keep Nano Banana 2.1 distinct from Gemini 3.1 Flash Lite Image, Gemini 3.1 Flash Image, Gemini 3 Pro Image, earlier Nano Banana/2.5 image endpoints, and Gemini product UI names or routing behavior.
- Treat token limits, batch support, search-grounding behavior, API parameters, supported image sizes, pricing, quotas, safety controls, model-version aliases, and product integrations as freshness-sensitive serving facts.
- Keep provider claims about visual design, mask-based editing, subject consistency, realism, text rendering, and comparative quality explicitly attributed to Google/Google DeepMind.
- Do not infer that being based on Gemini 3.6 Flash makes Nano Banana 2.1 an alias or serving mode of that general-purpose model; it remains an independently published concrete image-generation model identity.

## Validation

- The node remains the stable concrete `gemini-nano-banana-2.1` model rather than the Gemini API or Gemini application.
- Preview/deprecated image endpoints are not represented as current aliases.
- Provider comparisons remain attributed and model/version scoped.

## Verified identity and provenance

Stable Gemini image-generation and editing model served as gemini-nano-banana-2.1 and named Nano Banana 2.1; product nicknames do not create additional model identities.

## Source-scoped operating boundaries

- The API accepts text, images, video, and PDFs and returns image/text. It supports 1K, 2K, and 4K generation with up to 14 reference images. Web/image grounding is supported; function calling, code execution, and Live API are not. [Model reference](https://ai.google.dev/gemini-api/docs/models/gemini-nano-banana-2.1).
- Grounding and visual consistency are model capabilities, not proof that a generated scene or rendered text is accurate. Keep safety controls and the rights to source/reference imagery scoped to the actual application. [Model limitations](https://deepmind.google/models/model-cards/nano-banana-2-1/).

## Source evidence

- <https://ai.google.dev/gemini-api/docs/models/gemini-nano-banana-2.1>
- <https://deepmind.google/models/model-cards/nano-banana-2-1/>
