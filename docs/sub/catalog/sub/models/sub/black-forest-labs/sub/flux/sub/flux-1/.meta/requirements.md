# Documentation Requirements

## Identity and provenance

- FLUX.1 is the first FLUX image-model series from Black Forest Labs. This catalog currently materializes FLUX.1-schnell within the series; the series is not synonymous with that checkpoint.
- The existing series and its Models index organize concrete FLUX.1 models. Do not infer that only the materialized schnell member exists upstream. [BFL official model registry](https://huggingface.co/black-forest-labs) [FLUX.1-schnell model card](https://huggingface.co/black-forest-labs/FLUX.1-schnell).

## Operational decision boundaries

- License, distillation method and inference-step facts belong to individual FLUX.1 models; do not apply schnell's Apache 2.0 license to the entire series. [FLUX.1-schnell model card](https://huggingface.co/black-forest-labs/FLUX.1-schnell).

## Validation

- Preserve the canonical identity, model hierarchy and exact reciprocal relation targets; distinguish producer, family, series, model, artifact and serving identities.
- Render all visible current-node relations in deterministic order and resolve local reader links. Restore missing readers from canonical facts without granting dependency-domain credit.
- Keep source dates, availability, license conditions and service-specific limits attributable. Do not turn provider claims into local runtime, performance or benchmark verification.
