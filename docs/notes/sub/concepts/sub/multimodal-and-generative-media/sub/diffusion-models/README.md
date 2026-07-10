# Diffusion Models

<!--
ai_content:
  managed: true
  l10n: true
-->

Diffusion models are generative models trained to reverse a process that progressively adds noise to data.

## Core idea

During generation, the model starts from random noise or a noised input and predicts how to remove noise over several steps. Conditioning such as text embeddings, images, masks, or structural controls guides the denoising trajectory. Many image systems operate in a compressed latent space instead of directly on pixels.

## Practical use

- Text-to-image generation.
- Image editing, inpainting, and outpainting.
- Super-resolution and restoration.
- Audio and video generation.
- Controlled generation using edges, depth, or pose.

## Important settings

The sampler, number of steps, guidance strength, seed, resolution, and conditioning weights affect output. More steps do not always improve quality after the sampler reaches diminishing returns.

## Trade-offs and limitations

Diffusion generation is iterative and can be computationally expensive. High guidance may reduce diversity or create artifacts. Models can struggle with exact text, consistent characters, and complex spatial constraints.

## Common mistakes

- Treating seed alone as complete reproducibility.
- Increasing steps without measuring improvement.
- Using incompatible model, VAE, or conditioning components.
- Assuming latent-space edits preserve every original detail.

## Related concepts

- [Multimodal and Generative Media](../../)
- [Latent Space](../latent-space/)
- [ControlNet](../controlnet/)
- [Image Generation](../image-generation/)
