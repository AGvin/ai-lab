# Documentation Requirements

## Identity and provenance

- FLUX.1 is the first FLUX image-model series from Black Forest Labs. This catalog materializes FLUX.1-schnell, FLUX.1-dev, FLUX.1 Krea [dev], FLUX.1 Kontext [dev], FLUX.1 Fill [dev] and FLUX.1 Redux [dev], plus hosted FLUX.1 Kontext [pro] and [max], Fill [pro], and FLUX1.1 [pro] (Ultra/Raw are modes). Redux is a learned adapter dependent on a compatible generator; hosted Kontext endpoints have distinct proprietary service contracts and no established downloadable checkpoint rights.
- The existing series and its Models index organize concrete FLUX.1 models. Do not infer that only the materialized schnell member exists upstream. [BFL official model registry](https://huggingface.co/black-forest-labs) [FLUX.1-schnell model card](https://huggingface.co/black-forest-labs/FLUX.1-schnell).

## Operational decision boundaries

- License, distillation method and inference-step facts belong to individual FLUX.1 models; do not apply schnell's Apache 2.0 license to the entire series. [FLUX.1-schnell model card](https://huggingface.co/black-forest-labs/FLUX.1-schnell).
- FLUX.1-dev's gated weights use a non-commercial license and guidance-distilled generation; do not conflate its terms or behavior with schnell's Apache-2.0 weights and 1–4-step workflow. [FLUX.1-dev official model card](https://github.com/black-forest-labs/flux/blob/main/model_cards/FLUX.1-dev.md) [current terms](https://bfl.ai/legal/non-commercial-license-terms).

## Validation

- Preserve the canonical identity, model hierarchy and exact reciprocal relation targets; distinguish producer, family, series, model, artifact and serving identities.
- Render all visible current-node relations in deterministic order and resolve local reader links. Restore missing readers from canonical facts without granting dependency-domain credit.
- Keep source dates, availability, license conditions and service-specific limits attributable. Do not turn provider claims into local runtime, performance or benchmark verification.

- FLUX.1 Krea [dev] has joint BFL/Krea provenance; namespace placement is not exclusive authorship. Preserve source-specific raw-base provenance without an invented released-dev parent edge.

- Distinguish instruction-based Kontext editing from binary-mask Fill inpainting/outpainting; hosted pro variants and optimized artifacts are not these dev checkpoints.

- Redux [dev] is a separate learned image-conditioning adapter usable with FLUX.1-dev or schnell; no unsupported `derived-from` edge from mere compatibility and no inheritance of schnell's Apache 2.0 terms. Preserve the actual non-commercial Redux license and standalone versus dependent role. [BFL reference](https://github.com/black-forest-labs/flux/blob/main/docs/image-variation.md) [Official model card](https://huggingface.co/black-forest-labs/FLUX.1-Redux-dev).

- Kontext [pro] and [max] are separate currently available BFL-hosted models introduced May 29, 2025. The official API exposes `/v1/flux-kontext-pro` and `/v1/flux-kontext-max`; keep their identities separate from open-weight Kontext [dev], with no inferred trained-parent relation or parameter count. BFL recommends FLUX.2 for new projects. [BFL release](https://bfl.ai/blog/flux-1-kontext) [Current guide](https://help.bfl.ai/articles/5186006235-what-is-flux-1-kontext) [API](https://api.bfl.ai/docs).

- FLUX1.1 [pro] was separately released by BFL in October 2024, with its own /v1/flux-pro-1.1 API route. Ultra/Raw are modes, not additional independently learned models. No local weight/parent claims. [Announcement](https://bfl.ai/blog/24-10-02-flux) [Modes](https://bfl.ai/blog/24-11-06-ultra).
- FLUX.1 Fill [pro] is a distinct hosted mask-based inpainting/outpainting model at /v1/flux-pro-1.0-fill, not the open-weight Fill [dev]. BFL's Canny/Depth deprecation explicitly excludes Fill. [Tools](https://bfl.ai/blog/24-11-21-tools) [API](https://api.bfl.ai/docs).
