# Documentation Requirements

## Identity and provenance

- Identify FLUX.1 Fill [pro] as a separately released **BFL-hosted inpainting/outpainting model** within the FLUX.1 Tools suite, distinct from the open-weight gated Fill [dev] checkpoint and from the FLUX1.1 [pro] text-to-image model. [FLUX.1 Tools release](https://bfl.ai/blog/24-11-21-tools).
- The official API labels POST /v1/flux-pro-1.0-fill as the route to inpaint with FLUX.1 Fill [pro], with input image and mask. Additional finetuned endpoints do not automatically create new base-model identities. [BFL API reference](https://api.bfl.ai/docs).
- The provider's deprecation notice concerns FLUX.1 Canny and Depth variants; it explicitly states that **Fill and Redux are not affected**. Do not falsely mark Fill [pro] deprecated. [Updated BFL Tools page](https://bfl.ai/blog/24-11-21-tools).

## Decision and operational boundaries

- Fill [pro] edits or extends source images from a text prompt and mask. It is a masked editing route, not a substitute for Kontext's instruction-based editing with preserved image context. [Original release](https://bfl.ai/blog/24-11-21-tools).
- Follow the hosted endpoint's accepted image/mask formats, mask semantics, quotas, output policies and provider authentication. Do not transplant the exact open-weight [dev] implementation limitations into an unverified hosted service contract. [BFL API](https://api.bfl.ai/docs).
- BFL lists FLUX.1 Fill [pro] among current Tools. Treat catalog availability and prices as mutable; verify them at integration time. [Provider model overview](https://help.bfl.ai/articles/7655484417-what-flux-models-are-available).
- No claim of downloadable [pro] weights, parameter count, known training ancestry, weight license, GPU fit or independent quality benchmark. API terms, image-data handling, content restrictions and output rights remain provider-specific.

## Validation

- Exactly one member-of edge to FLUX.1 and reciprocal series membership; index and reader links resolve.
- Distinguish Fill [pro], Fill [dev], deprecated Canny/Depth, and Kontext models; preserve model/mode/service boundaries.
- No complete current-HEAD schema/cache/CI, end-to-end inference or benchmark credit.
