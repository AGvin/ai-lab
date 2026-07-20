# Text-to-Image

Text-to-image generation creates an image conditioned primarily on a natural-language description.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Core idea

The prompt is encoded into a representation that guides a generative model. Different parts of the prompt influence subject, composition, environment, style, color, camera, and lighting, but the model does not interpret text as a deterministic scene specification.

## Practical prompting

- State the main subject and action first.
- Describe composition and viewpoint explicitly.
- Add environment, lighting, and medium after the core scene.
- Use negative constraints only when supported and necessary.
- Generate several candidates and refine the strongest one.

## Trade-offs and limitations

Text prompts provide flexible high-level control but weak exact control over geometry, identity, typography, and object count. Prompt interpretation varies between model families and versions.

## Common mistakes

- Listing conflicting styles and camera directions.
- Expecting exact spelling in generated text.
- Changing many prompt elements at once during refinement.
- Assuming prompt wording transfers unchanged across models.

## Related concepts

- [Multimodal and Generative Media](../../)
- [Image Generation](../image-generation/)
- [ControlNet](../controlnet/)
- [Prompting](../../../model-usage-and-generation/sub/prompting/)
