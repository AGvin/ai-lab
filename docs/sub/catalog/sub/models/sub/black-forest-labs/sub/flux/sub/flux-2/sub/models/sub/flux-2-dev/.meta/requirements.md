# Documentation Requirements

## Identity and provenance

- FLUX.2 [dev] is Black Forest Labs' downloadable 32-billion-parameter rectified-flow transformer for image generation and editing, with guidance distillation. Its model weights use the FLUX Non-Commercial license, separately from Apache-licensed components.
- The official checkpoint is black-forest-labs/FLUX.2-dev. Its 32B generator, text encoder, autoencoder, precision artifacts and hosted distributions are separate parts of the model and delivery workflow. [FLUX.2-dev model card](https://huggingface.co/black-forest-labs/FLUX.2-dev) [FLUX.2 inference repository](https://github.com/black-forest-labs/flux2).

## Operational decision boundaries

- The weight license permits specified noncommercial use; commercial weight operation requires separate permission. Commercial use of outputs under the license's conditions is not permission to run the weights commercially. Use the current license text, not the model card's stale link to a different model's license. [FLUX Non-Commercial License v2.1](https://github.com/black-forest-labs/flux2/blob/main/model_licenses/LICENSE-FLUX-NON-COMMERICAL) [FLUX.2-dev model card](https://huggingface.co/black-forest-labs/FLUX.2-dev).
- The official reference implementation targets large-memory GPUs. Its consumer 4-bit recipe can use a remote text encoder, so local image generation can still send prompts to another service; prompt upsampling can also introduce an external model. Record precision, encoder placement, offload and prompt route. [FLUX.2 inference repository](https://github.com/black-forest-labs/flux2).
- BFL's speed and quality claims do not establish local hardware performance or guaranteed text/identity preservation. Validate representative prompts and reference edits with the exact components and content review needed for the application. [FLUX.2-dev model card](https://huggingface.co/black-forest-labs/FLUX.2-dev) [FLUX.2 inference repository](https://github.com/black-forest-labs/flux2).

## Validation

- Preserve the canonical identity, model hierarchy and exact reciprocal relation targets; distinguish producer, family, series, model, artifact and serving identities.
- Render all visible current-node relations in deterministic order and resolve local reader links. Restore missing readers from canonical facts without granting dependency-domain credit.
- Keep source dates, availability, license conditions and service-specific limits attributable. Do not turn provider claims into local runtime, performance or benchmark verification.
