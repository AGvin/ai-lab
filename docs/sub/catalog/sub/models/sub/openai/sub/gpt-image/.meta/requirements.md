# Documentation Requirements

## Requirements

- Identify GPT Image as OpenAI's image-generation and image-editing model family.
- Preserve concrete model identity separately from ChatGPT Images product/workspace features, the Image API, Responses API image-generation tool, and mutable hosting controls.
- Keep text/image input to image output as the family-level modality boundary only where shared by current members.
- Keep pricing, rate limits, API endpoint support, quality/size controls, organization verification requirements, and ChatGPT product behavior freshness-sensitive and with the applicable serving/product surface.
- Render the standard `entity-relations` block from validated current-entity relations.

## Validation

- GPT Image remains a trained-model family rather than the Images API or ChatGPT Images product.
- Concrete members retain model-specific quality/speed positioning and snapshots.
- Producer provenance resolves bidirectionally to OpenAI.

## Source-scoped operating boundaries

- The Image API selects an image model directly. In Responses, a supported mainline model calls the image-generation tool, whose model setting selects the image model; the orchestration model and image model are separate identities [Image-generation guide](https://developers.openai.com/api/docs/guides/image-generation).
- Organization verification, output settings, and content filtering are service conditions. Precise text placement, composition, and cross-image consistency still require reviewing the generated result [Image-generation guide](https://developers.openai.com/api/docs/guides/image-generation).

## Source evidence

- [OpenAI model catalog](https://developers.openai.com/api/docs/models).
- [Image-generation guide](https://developers.openai.com/api/docs/guides/image-generation).
- [API changelog](https://developers.openai.com/api/docs/changelog).
