# Inpainting

<!--
ai_content:
  managed: true
  l10n: true
-->

Inpainting regenerates selected masked regions of an image while using the surrounding image as context.

## Core idea

A mask identifies which pixels may change. The model fills the masked region according to the prompt, neighboring content, and optional reference controls. Mask blur and padding help blend the generated region into its surroundings.

## Practical use

- Remove or replace objects.
- Correct hands, faces, text, or small artifacts.
- Repair damaged areas.
- Change clothing, background elements, or materials.
- Extend a local edit without regenerating the full image.

## Trade-offs and limitations

A mask that is too small may preserve the artifact's structure; a mask that is too large may unnecessarily alter surrounding content. Lighting, perspective, shadows, and texture must match the original image for a convincing result.

## Common mistakes

- Masking only the visible error and not its shadow or reflection.
- Using no context padding around the region.
- Expecting exact object placement from text alone.
- Repeatedly editing a compressed image and accumulating artifacts.

## Related concepts

- [Multimodal and Generative Media](../../)
- [Image-to-Image](../image-to-image/)
- [Outpainting](../outpainting/)
- [ControlNet](../controlnet/)
