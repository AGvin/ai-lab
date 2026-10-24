# FLUX 3 Image

FLUX 3 Image is Black Forest Labs' named FLUX 3 image-generation and editing model, available through documented hosted interfaces. It is distinct from the separately published Image Klein Base and distilled models. [FLUX 3 Image product page](https://bfl.ai/models/flux-3-image) [FLUX 3 Image API overview](https://docs.bfl.ai/flux_3/flux3_image_overview) [FLUX 3 initial announcement](https://bfl.ai/blog/flux-3).

## Identity and scope

Use the current model page and API documentation for availability. The initial July 2026 promise of later Image access is a historical rollout statement, not the current access gate. [FLUX 3 Image product page](https://bfl.ai/models/flux-3-image) [FLUX 3 Image API overview](https://docs.bfl.ai/flux_3/flux3_image_overview) [FLUX 3 initial announcement](https://bfl.ai/blog/flux-3).

## Use and limitations

The documented API supports text with up to ten reference images and layout guidance through normalized bounding boxes. These are current serving controls, not a guarantee of pixel-perfect masks or one universal limit across all deployments. [FLUX 3 Image API overview](https://docs.bfl.ai/flux_3/flux3_image_overview).

Web grounding is on by default in the documented interface; grounding:false limits that request to its supplied prompt context. Confirm this setting and any external-search processing when selecting a workflow. Grounding does not certify factual correctness. [FLUX 3 Image API overview](https://docs.bfl.ai/flux_3/flux3_image_overview).

Public hosted access and commercial weight arrangements do not constitute an open-weight license. The reviewed sources do not establish a public parameter count for this named hosted model; do not borrow Image Klein's 5.6B count or license. [FLUX 3 Image product page](https://bfl.ai/models/flux-3-image) [FLUX 3 Image API overview](https://docs.bfl.ai/flux_3/flux3_image_overview) [FLUX 3 Image Klein release](https://bfl.ai/blog/flux-3-image-klein).

## Relations

| Relation | Target | Target type |
| --- | --- | --- |
| `member-of` | [FLUX 3](../../../../README.md) | `model-series` |

## Sources

- [FLUX 3 Image product page](https://bfl.ai/models/flux-3-image)
- [FLUX 3 Image API overview](https://docs.bfl.ai/flux_3/flux3_image_overview)
- [FLUX 3 initial announcement](https://bfl.ai/blog/flux-3)
- [FLUX 3 Image Klein release](https://bfl.ai/blog/flux-3-image-klein)
