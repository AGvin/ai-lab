# Image-to-Image

Legacy residual retained for practical editing workflows and runtime-specific transformation-strength guidance that is intentionally outside the canonical Image-to-Image Generation concept owner.

> **Migration note:** Image-to-image task identity, architecture-neutral transformation semantics, paired/unpaired training boundary, preservation-versus-transformation behavior, and distinctions from inpainting/outpainting are already preserved in `docs/sub/concepts/sub/modalities/sub/vision/sub/image-to-image/`. Diffusion-specific partial noising and `denoising strength` are explicitly treated there as implementation/UI details rather than universal concept semantics. The remaining material below stays here until its exact learning, workflow, runtime, evidence, or decision-support owner is verified.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Editing-workflow residual

Image-to-image workflows can be used to:

- restyle an existing composition;
- refine a sketch or rough render;
- change lighting, materials, or environment;
- produce variations while preserving selected layout/content;
- prepare an image for more localized editing such as inpainting.

These are workflow examples rather than part of the canonical task definition.

## Runtime-control residual

Some diffusion-based tools expose a denoising or transformation-strength control. Lower values commonly preserve more source detail while higher values permit larger changes, but the exact meaning and useful range depend on the concrete model, scheduler, preprocessing, runtime, and implementation.

When identity, geometry, typography, or fine detail matters, validate the actual result rather than assuming the source image guarantees preservation. Aspect-ratio changes, resize/crop preprocessing, repeated generative passes, and strong transformation settings can accumulate drift or preserve unwanted artifacts in model-specific ways.

These operational editing choices remain migration source material until their exact learning, runtime, workflow, evidence, or decision-support owners are verified.
