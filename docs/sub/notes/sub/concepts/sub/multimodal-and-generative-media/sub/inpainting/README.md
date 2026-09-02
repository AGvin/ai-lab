# Inpainting

Legacy residual retained for practical localized-edit workflows and mask/context handling guidance that is intentionally outside the canonical Image Inpainting concept owner.

> **Migration note:** Inpainting task identity, architecture-neutral localized completion semantics, mask-region boundary, distinctions from image-to-image/outpainting, preservation and factual-recovery caveats, boundary-consistency factors, and the separation of workflow heuristics from concept semantics are already preserved in `docs/sub/concepts/sub/modalities/sub/vision/sub/inpainting/`. The remaining material below stays here until its exact learning, editing-workflow, runtime, evidence, or decision-support owner is verified.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Editing-workflow residual

Inpainting workflows can be useful for:

- removing or replacing objects;
- correcting hands, faces, text, or localized artifacts;
- repairing damaged regions;
- changing clothing, background elements, or materials;
- applying a focused edit without regenerating the full image.

These are workflow examples rather than part of the canonical task definition.

## Mask and context residual

Concrete tools can expose mask blur, feathering, dilation, padding, crop/context size, compositing, prompt, strength, or repeated-pass controls. Useful values are runtime/model specific.

A mask that is too narrow can preserve unwanted structure around an artifact, while an unnecessarily broad edit region can modify surrounding content. Include enough relevant context for perspective, lighting, shadows, reflections, texture, and object relationships when those properties must remain coherent. Repeated editing of already compressed or repeatedly regenerated content can accumulate artifacts.

These practical mask/context choices remain migration source material until their exact learning, editing-workflow, runtime, evidence, or decision-support owners are verified.
