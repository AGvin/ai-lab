# Documentation Requirements

## Requirements

- Identify GPT-Image-2.5 Sunburst as the concrete `gpt-image-2.5-sunburst` image-generation/editing model released by OpenAI on 2026-09-08.
- Preserve text and image input, image output, direct Image API and Responses image-tool availability, and current support for `low`, `medium`, `high`, `xhigh`, `max`, and `auto` quality settings only while current first-party documentation supports them.
- Present OpenAI's precision/editing-capability positioning as provider guidance rather than an independent AI Lab ranking.
- Keep pricing, token consumption, rate limits, endpoint details, supported sizes/formats/backgrounds, organization verification, and dated snapshot IDs freshness-sensitive.

## Validation

- Sunburst remains distinct from GPT-Image-2.5 Flare and earlier GPT Image releases.
- ChatGPT Images product behavior is not treated as intrinsic model identity.

## Source-scoped operating boundaries

- Use the image-model identifier at the Image API or as the Responses image tool’s model. A Responses request still uses a supported mainline model to orchestrate that tool [Image-generation guide](https://developers.openai.com/api/docs/guides/image-generation).
- Service verification and filtering apply, and the output needs review for instruction fidelity and visual errors. Quality settings and pinned snapshots do not create peer model identities [Image-generation guide](https://developers.openai.com/api/docs/guides/image-generation).

## Source evidence

- [gpt-image-2.5-sunburst model reference](https://developers.openai.com/api/docs/models/gpt-image-2.5-sunburst).
- [Image-generation guide](https://developers.openai.com/api/docs/guides/image-generation).
- [API changelog](https://developers.openai.com/api/docs/changelog).
