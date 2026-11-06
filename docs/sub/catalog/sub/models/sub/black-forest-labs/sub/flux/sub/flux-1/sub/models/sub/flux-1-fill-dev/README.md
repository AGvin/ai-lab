# FLUX.1 Fill [dev]

Released 12B guidance-distilled rectified-flow model for image inpainting and outpainting from an input image, text and a binary mask. The exact dev checkpoint is distinct from hosted Fill pro and from FLUX.1-dev generation weights. [Official checkpoint](https://huggingface.co/black-forest-labs/FLUX.1-Fill-dev).

## Identity and scope

Replaces selected image regions or extends an image using a mask and text. The reference implementation expects the mask and input image to have matching dimensions. [First-party implementation](https://github.com/black-forest-labs/flux/blob/main/docs/fill.md).

## Use and limitations

The model card warns of color shifts outside the filled area and seams at complex texture boundaries. Inspect preserved regions and mask edges; source ranking claims are not independent measurements.

Gated weights use the FLUX dev Non-Commercial License. Model-weight use, output permissions and hosted API contracts are separate; commercial model use requires appropriate rights. No local inference test or independent quality, memory or speed benchmark has been performed.

## Relations

| Relation | Target | Target type |
| --- | --- | --- |
| `member-of` | [FLUX.1](../../../../README.md) | `model-series` |

## Sources

- [Official model card and weights](https://huggingface.co/black-forest-labs/FLUX.1-Fill-dev)
- [Reference implementation](https://github.com/black-forest-labs/flux/blob/main/docs/fill.md)
- [BFL release and lifecycle information](https://bfl.ai/blog/24-11-21-tools)
