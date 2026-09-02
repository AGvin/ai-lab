# Diffusion Models

Legacy residual retained for application examples and practical generation-workflow guidance that is intentionally outside the canonical Diffusion Models architecture owner.

> **Migration note:** Diffusion-model identity, forward/reverse process semantics, discrete and continuous formulations, latent-space boundary, conditioning families, sampler-versus-model distinction, step-count and seed caveats, and general limitations are already preserved in `docs/sub/concepts/sub/models/sub/architectures/sub/diffusion-models/`. The remaining material below stays here until its exact learning, generative-media workflow, runtime, evidence, or decision-support owner is verified.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Application residual

Diffusion-family models are commonly applied to workflows such as:

- text-to-image generation;
- image editing, inpainting, and outpainting;
- super-resolution and restoration;
- audio and video generation;
- controlled generation using edges, depth, pose, masks, or other conditioning signals.

These are application examples rather than part of the canonical diffusion-model definition.

## Workflow and settings residual

Concrete generation workflows can expose sampler or solver choice, step count, guidance strength, seed, resolution, conditioning weights, latent autoencoder selection, and related runtime controls. Their useful values depend on the specific model, scheduler/solver, conditioning pipeline, numerical/runtime environment, and target task.

More sampling steps do not inherently produce better output, and a seed alone is not a complete reproducibility contract. Workflow validation should also check component compatibility, including the concrete model, latent autoencoder or VAE where applicable, conditioning components, preprocessing, scheduler, and runtime.

These practical settings and workflow choices remain migration source material until their exact learning, runtime, evidence, generative-media workflow, or decision-support owners are verified.
