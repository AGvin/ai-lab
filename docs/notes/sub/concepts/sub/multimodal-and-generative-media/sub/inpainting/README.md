# Inpainting

Regenerating selected masked regions of an image.

## Translations

- English — current
- [Українська](./l10n/uk_UA/)

## Core idea

Regenerating selected masked regions of an image. In practical AI work, the term is useful because it names a specific part of the system rather than treating the model as a single opaque component. Understanding where it appears in the workflow makes configuration choices and failure analysis more precise.

## How it works

- Inpainting uses a mask to identify regions that may be regenerated.
- The model receives surrounding pixels and optional prompt context to fill the masked area.
- Mask feathering, crop strategy, and denoising strength affect boundary consistency.

The exact implementation varies by model family, provider, and runtime. The important distinction is the role the concept plays in the end-to-end system and which inputs, state, or resources it changes.

## Why it matters

Inpainting affects how an AI system should be selected, configured, tested, or operated. It can influence output quality, resource requirements, reliability, or the amount of control available to the surrounding application.

## Practical uses

- Remove objects, repair defects, or replace selected image regions.
- Correct hands, text areas, clothing, or background details without regenerating the entire image.

## Example

A duplicated limb is masked and regenerated while the rest of the character remains unchanged.

## Trade-offs and limitations

- Lighting, perspective, and texture can mismatch at mask boundaries.
- Large masked regions provide less surrounding context and may drift.

Do not evaluate this concept in isolation. Test it together with the actual model, data, runtime, tools, and workload that will be used in production or local experiments.

## Practical checklist

- What problem is Inpainting expected to solve in this workflow?
- Which inputs, settings, or resources does it depend on?
- How will success and failure be measured?
- What changes when the model, runtime, dataset, or context size changes?

## Related concepts

- [Multimodal and Generative Media](../../)
- [Image-to-Image](../image-to-image/)
- [ControlNet](../controlnet/)
