# Documentation Requirements

## Identity and provenance

- FLUX is Black Forest Labs' model family, covering the FLUX.1 and FLUX.2 image lines and the FLUX 3 multimodal line. A family is a provenance and navigation grouping, not one concrete checkpoint.
- FLUX.1, FLUX.2 and FLUX 3 share Black Forest Labs provenance. Multimodal scope belongs to the family through its members; it does not make every member a video or action model. [BFL official model registry](https://huggingface.co/black-forest-labs) [FLUX.2 overview](https://docs.bfl.ai/flux_2/flux2_overview) [FLUX 3 initial announcement](https://bfl.ai/blog/flux-3).

## Operational decision boundaries

- Select a concrete member for its inputs, outputs, release state and weight terms. Hosted API contracts, downloaded checkpoints, code licenses and generated outputs have distinct boundaries. [FLUX.2 overview](https://docs.bfl.ai/flux_2/flux2_overview) [FLUX 3 initial announcement](https://bfl.ai/blog/flux-3) [FLUX Kommunity License v1.0](https://huggingface.co/black-forest-labs/flux-3-image-klein-base/blob/main/LICENSE.md).

## Validation

- Preserve the canonical identity, model hierarchy and exact reciprocal relation targets; distinguish producer, family, series, model, artifact and serving identities.
- Render all visible current-node relations in deterministic order and resolve local reader links. Restore missing readers from canonical facts without granting dependency-domain credit.
- Keep source dates, availability, license conditions and service-specific limits attributable. Do not turn provider claims into local runtime, performance or benchmark verification.
