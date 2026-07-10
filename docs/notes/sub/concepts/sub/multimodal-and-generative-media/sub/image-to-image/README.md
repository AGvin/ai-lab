# Image-to-Image

<!--
ai_content:
  managed: true
  l10n: true
-->

Image-to-image generation transforms an existing image while using it as conditioning for composition, content, or style.

## Core idea

The source image is encoded and partially noised, then regenerated under prompt or structural guidance. A denoising-strength parameter commonly controls how closely the output remains tied to the source: lower strength preserves more detail, while higher strength permits larger changes.

## Practical use

- Restyle a composition.
- Improve a sketch or rough render.
- Change lighting, materials, or environment.
- Produce variations while preserving layout.
- Prepare an image for focused inpainting.

## Trade-offs and limitations

Strong transformations can alter identity, geometry, text, or small details. Low-strength transformations may preserve unwanted artifacts. Repeated image-to-image passes can accumulate drift and reduce fidelity.

## Common mistakes

- Using high denoising strength when identity must remain stable.
- Expecting pixel-perfect preservation from generative editing.
- Ignoring aspect-ratio and preprocessing changes.
- Applying many successive transformations without returning to the best source.

## Related concepts

- [Multimodal and Generative Media](../../)
- [Inpainting](../inpainting/)
- [Outpainting](../outpainting/)
- [Diffusion Models](../diffusion-models/)
