# Outpainting

Outpainting extends an image beyond its original boundaries by generating new surrounding content.

## Core idea

The original image provides visual context while a larger canvas contains masked empty regions. The model continues textures, perspective, lighting, and scene content into the new area. Overlap between original and generated regions helps avoid visible seams.

## Practical use

- Change image aspect ratio.
- Expand backgrounds for banners or layouts.
- Reveal more environment around a subject.
- Reframe a composition without cropping.
- Create panoramic extensions.

## Trade-offs and limitations

The model may invent inconsistent geometry or repeat objects. Large extensions have less original context and are more likely to drift. Faces and central subjects near the boundary may be altered unless protected carefully.

## Common mistakes

- Extending too much in a single pass.
- Providing no prompt for the new scene area.
- Using a hard mask boundary without overlap.
- Expecting hidden parts of real objects to be reconstructed factually.

## Related concepts

- [Multimodal and Generative Media](../../)
- [Inpainting](../inpainting/)
- [Image-to-Image](../image-to-image/)
- [Image Generation](../image-generation/)
