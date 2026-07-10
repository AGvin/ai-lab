# Image Generation

<!--
ai_content:
  managed: true
  l10n: true
-->

Image generation creates new images from text, reference images, masks, layouts, depth maps, poses, or other conditioning signals.

## Core idea

Modern systems commonly use diffusion or related generative architectures that begin from noise or a latent representation and progressively construct an image. The prompt and conditioning guide composition, subject, style, lighting, and other attributes, but generation remains probabilistic.

## Practical use

- Concept art and visual ideation.
- Marketing and social media assets.
- Product mockups and storyboards.
- Controlled image editing and restoration.
- Synthetic visual datasets.

## Trade-offs and limitations

Models may produce anatomical errors, inconsistent text, duplicated objects, or details that do not match the prompt. Exact identity, logos, typography, and multi-image consistency often require reference conditioning or manual editing.

## Common mistakes

- Expecting a long prompt to control every detail independently.
- Using generated images as factual evidence.
- Ignoring model, dataset, and output licensing.
- Publishing without inspecting hands, text, reflections, and repeated objects.

## Related concepts

- [Multimodal and Generative Media](../../)
- [Diffusion Models](../diffusion-models/)
- [Text-to-Image](../text-to-image/)
- [Image-to-Image](../image-to-image/)
