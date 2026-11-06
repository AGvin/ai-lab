# Documentation Requirements

## Requirements

- Identify GPT-Image-2 as OpenAI's released `gpt-image-2` image-generation and editing model, introduced on 2026-04-21.
- Preserve text/image input to image output, high-fidelity image-input behavior, flexible-size support, and current Image API/Responses integration only while supported by current first-party documentation.
- Keep the dated `gpt-image-2-2026-04-21` snapshot as a versioned serving artifact of the same trained-model identity.
- Keep pricing, quality settings, image-size constraints, endpoint details, rate limits, organization verification, and deprecation/replacement guidance freshness-sensitive.
- Keep GPT-Image-2 distinct from GPT-Image-2.5 Sunburst/Flare and deprecated GPT Image 1.x models.

## Validation

- GPT-Image-2 is a concrete member of the GPT Image family.
- Serving and API behavior is not generalized into permanent architecture.

## Source-scoped operating boundaries

- Use the image-model identifier at the Image API or as the Responses image tool’s model. A Responses request still uses a supported mainline model to orchestrate that tool [Image-generation guide](https://developers.openai.com/api/docs/guides/image-generation).
- Service verification and filtering apply, and the output needs review for instruction fidelity and visual errors. Quality settings and pinned snapshots do not create peer model identities [Image-generation guide](https://developers.openai.com/api/docs/guides/image-generation).

## Source evidence

- [gpt-image-2 model reference](https://developers.openai.com/api/docs/models/gpt-image-2).
- [Image-generation guide](https://developers.openai.com/api/docs/guides/image-generation).
- [API changelog](https://developers.openai.com/api/docs/changelog).
