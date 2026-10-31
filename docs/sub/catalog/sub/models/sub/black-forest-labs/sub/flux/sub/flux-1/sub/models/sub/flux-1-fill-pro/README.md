# FLUX.1 Fill [pro]

FLUX.1 Fill [pro] is a distinct Black Forest Labs **hosted** image editing model introduced with FLUX.1 Tools in November 2024. It performs inpainting and outpainting using an input image, a mask and text instructions; it is not the separately published gated Fill [dev] checkpoint. [BFL Tools release](https://bfl.ai/blog/24-11-21-tools).

## Identity and scope

The official BFL API exposes POST /v1/flux-pro-1.0-fill for FLUX.1 Fill [pro]. A hosted endpoint does not provide the training parent, parameter count or rights to download and serve proprietary model weights. Fine-tuned API routes are not additional base-model nodes by default. [BFL API reference](https://api.bfl.ai/docs).

## Use and limitations

Use this model when an existing image must be edited or expanded under explicit **binary-mask control**. Kontext models instead support instruction-based reference-image editing; the two interfaces require different workflow and fidelity tests.

BFL deprecated the FLUX.1 Canny and Depth models, but its published notice explicitly says **Fill and Redux were not affected**. Fill [pro] remains listed among BFL's model tools; verify live endpoint availability and quotas for production use. [BFL deprecation notice](https://bfl.ai/blog/24-11-21-tools) [Provider overview](https://help.bfl.ai/articles/7655484417-what-flux-models-are-available).

Hosted API rights and image-data policies differ from the Fill [dev] open-weight non-commercial license. Confirm mask/input requirements, image retention, billing, output rights, policy screening and rate limits. No independent image benchmark or local serving test is claimed.

## Relations

| Relation | Target | Target type |
| --- | --- | --- |
| `member-of` | [FLUX.1](../../../../README.md) | `model-series` |

## Sources

- [FLUX.1 Tools launch and deprecation notice](https://bfl.ai/blog/24-11-21-tools)
- [BFL API model routes](https://api.bfl.ai/docs)
- [Current provider model overview](https://help.bfl.ai/articles/7655484417-what-flux-models-are-available)
