# Outpainting

Legacy residual retained for practical canvas-extension workflows and staged-edit guidance that is intentionally outside the canonical Image Outpainting concept owner.

> **Migration note:** Outpainting task identity, architecture-neutral boundary-extension semantics, distinctions from inpainting/image-to-image, factual-reconstruction caveats, source-preservation boundary, scene-consistency challenges, and the separation of workflow heuristics from concept semantics are already preserved in `docs/sub/concepts/sub/modalities/sub/vision/sub/outpainting/`. The remaining material below stays here until its exact learning, editing-workflow, runtime, evidence, or decision-support owner is verified.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Editing-workflow residual

Outpainting workflows can be useful to:

- change an image aspect ratio without cropping the existing source;
- expand backgrounds for banners or layouts;
- reveal or invent more environment around a subject;
- reframe a composition;
- create panorama-like extensions.

These are workflow examples rather than part of the canonical task definition.

## Extension-strategy residual

Concrete tools can expose canvas direction/size, overlap, feathering, masks, prompt/conditioning, generation order, and repeated-pass controls. Extending a very large area in one pass can provide less source context and increase drift, repeated objects, geometry inconsistency, or unwanted changes near the source boundary.

For workflows where continuity matters, staged smaller extensions and overlapping/blended context can be useful implementation strategies, but their exact values and effectiveness are model/runtime specific. Validate perspective, horizon, lighting, texture, object continuation, reflections, and protected source regions rather than assuming a seamless local edge implies globally coherent continuation.

Generated content outside the observed frame is synthetic completion, not factual recovery of what existed beyond the original image boundary.

These practical extension choices remain migration source material until their exact learning, editing-workflow, runtime, evidence, or decision-support owners are verified.
