# Documentation Requirements

## Identity and provenance

- FLUX.2 is a Black Forest Labs image-generation and image-editing model series. It groups the named max, pro, flex and dev models and the specialized Klein subseries without collapsing their distinct deployment or licensing boundaries.
- The series includes max, pro, flex and dev alongside the specialized Klein subseries. Klein contains separately published scale, base, distilled and KV model choices. [FLUX.2 overview](https://docs.bfl.ai/flux_2/flux2_overview) [FLUX.2 inference repository](https://github.com/black-forest-labs/flux2) [FLUX.2 Klein launch](https://bfl.ai/blog/flux2-klein-towards-interactive-visual-intelligence).

## Operational decision boundaries

- FLUX.2 includes hosted offerings and separately licensed downloadable weights. Do not give the whole series one license, parameter count, reference-image limit or hardware minimum. [FLUX.2 overview](https://docs.bfl.ai/flux_2/flux2_overview) [FLUX.2 inference repository](https://github.com/black-forest-labs/flux2).
- Provider reference limits, resolutions, sampling controls and preview endpoints vary by exact model and access route. Pin those choices for a workflow; a preview alias may change its underlying weights without creating a new canonical identity automatically. [FLUX.2 overview](https://docs.bfl.ai/flux_2/flux2_overview).

## Learned decoder component

- Include the separately distilled FLUX.2 Small Decoder as a learned VAE component in this series, with exact reciprocal membership and a resolving reader link. Do not count decoder-only/combined-encoder packaging as additional trained models or infer a complete image-generation pipeline from the component. Its Apache-2.0 license does not replace generator terms. [Official model card](https://huggingface.co/black-forest-labs/FLUX.2-small-decoder).

## Validation

- Preserve the canonical identity, model hierarchy and exact reciprocal relation targets; distinguish producer, family, series, model, artifact and serving identities.
- Render all visible current-node relations in deterministic order and resolve local reader links. Restore missing readers from canonical facts without granting dependency-domain credit.
- Keep source dates, availability, license conditions and service-specific limits attributable. Do not turn provider claims into local runtime, performance or benchmark verification.
