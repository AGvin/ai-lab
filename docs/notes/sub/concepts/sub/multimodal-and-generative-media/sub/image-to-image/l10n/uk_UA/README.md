<!--
l10n:
  locale: uk_UA
  source_locale: default
  source_path: ../../README.md
  source_hash: gitblob:1ca486607314826529fe39d69dd98892bd894f0b
  mode: copy-through
-->

# Image-to-Image

Generating a transformed image while conditioning on an existing image.

## Переклади

- [English](../../../../l10n/uk_UA/)
- Українська — поточна

## Core idea

Generating a transformed image while conditioning on an existing image. In practical AI work, the term is useful because it names a specific part of the system rather than treating the model as a single opaque component. Understanding where it appears in the workflow makes configuration choices and failure analysis more precise.

## How it works

- Image-to-image generation encodes an existing image and applies a controlled amount of transformation.
- Denoising strength or similar controls determine how strongly the result follows the source versus the new prompt.
- Additional masks, structure controls, or reference adapters can preserve selected features.

The exact implementation varies by model family, provider, and runtime. The important distinction is the role the concept plays in the end-to-end system and which inputs, state, or resources it changes.

## Why it matters

Image-to-Image affects how an AI system should be selected, configured, tested, or operated. It can influence output quality, resource requirements, reliability, or the amount of control available to the surrounding application.

## Practical uses

- Restyle, relight, clean up, or recompose an existing image.
- Use sketches or photos as structural starting points.

## Example

A reference photo preserves the pose while the workflow changes clothing and background style.

## Trade-offs and limitations

- High transformation strength can destroy identity or composition.
- Low strength can preserve unwanted artifacts and limit requested changes.

Do not evaluate this concept in isolation. Test it together with the actual model, data, runtime, tools, and workload that will be used in production or local experiments.

## Practical checklist

- What problem is Image-to-Image expected to solve in this workflow?
- Which inputs, settings, or resources does it depend on?
- How will success and failure be measured?
- What changes when the model, runtime, dataset, or context size changes?

## Related concepts

- [Multimodal and Generative Media](../../../../l10n/uk_UA/)
- [Diffusion Models](../../../diffusion-models/l10n/uk_UA/)
- [Inpainting](../../../inpainting/l10n/uk_UA/)
