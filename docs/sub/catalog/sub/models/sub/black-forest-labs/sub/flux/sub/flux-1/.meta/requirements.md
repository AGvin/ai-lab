# Documentation Requirements

## Identity and provenance

- FLUX.1 is the first FLUX image-model series from Black Forest Labs. This catalog materializes FLUX.1-schnell, FLUX.1-dev and FLUX.1 Krea [dev]; they are distinct checkpoints with different weight licenses and inference contracts.
- The existing series and its Models index organize concrete FLUX.1 models. Do not infer that only the materialized schnell member exists upstream. [BFL official model registry](https://huggingface.co/black-forest-labs) [FLUX.1-schnell model card](https://huggingface.co/black-forest-labs/FLUX.1-schnell).

## Operational decision boundaries

- License, distillation method and inference-step facts belong to individual FLUX.1 models; do not apply schnell's Apache 2.0 license to the entire series. [FLUX.1-schnell model card](https://huggingface.co/black-forest-labs/FLUX.1-schnell).
- FLUX.1-dev's gated weights use a non-commercial license and guidance-distilled generation; do not conflate its terms or behavior with schnell's Apache-2.0 weights and 1–4-step workflow. [FLUX.1-dev official model card](https://github.com/black-forest-labs/flux/blob/main/model_cards/FLUX.1-dev.md) [current terms](https://bfl.ai/legal/non-commercial-license-terms).

## Validation

- Preserve the canonical identity, model hierarchy and exact reciprocal relation targets; distinguish producer, family, series, model, artifact and serving identities.
- Render all visible current-node relations in deterministic order and resolve local reader links. Restore missing readers from canonical facts without granting dependency-domain credit.
- Keep source dates, availability, license conditions and service-specific limits attributable. Do not turn provider claims into local runtime, performance or benchmark verification.

- FLUX.1 Krea [dev] has joint BFL/Krea provenance; namespace placement is not exclusive authorship. Preserve source-specific raw-base provenance without an invented released-dev parent edge.
