# Documentation Requirements

## Identity and provenance

- Identify the exact `black-forest-labs/FLUX.1-Fill-dev` checkpoint, independently published by BFL within FLUX.1. [Official registry](https://huggingface.co/black-forest-labs/FLUX.1-Fill-dev).
- Released 12B guidance-distilled rectified-flow model for image inpainting and outpainting from an input image, text and a binary mask. The exact dev checkpoint is distinct from hosted Fill pro and from FLUX.1-dev generation weights. [First-party documentation](https://github.com/black-forest-labs/flux/blob/main/docs/fill.md) [BFL release](https://bfl.ai/blog/24-11-21-tools).
- Render the standard current-entity relation block; preserve a single model identity rather than duplicating precision/runtime distributions.

## Operational decision boundaries

- Replaces selected image regions or extends an image using a mask and text. The reference implementation expects the mask and input image to have matching dimensions. [Reference documentation](https://github.com/black-forest-labs/flux/blob/main/docs/fill.md).
- The model card warns of color shifts outside the filled area and seams at complex texture boundaries. Inspect preserved regions and mask edges; source ranking claims are not independent measurements. [Model card](https://huggingface.co/black-forest-labs/FLUX.1-Fill-dev).
- Separate gated non-commercial model-weight permissions, outputs and hosted-service terms; do not inherit schnell's Apache 2.0 license.
- Do not assert VRAM fit, quality ranking or measured speed without workload-specific tests.

## Validation

- Resolve series membership with one exact inverse and resolving reader navigation.
- Preserve dev versus pro/other checkpoint distinctions; no inferred direct learned-parent edge from compatible code.
- No runtime, benchmark, full catalog validation or exhaustive upstream-coverage claim.
