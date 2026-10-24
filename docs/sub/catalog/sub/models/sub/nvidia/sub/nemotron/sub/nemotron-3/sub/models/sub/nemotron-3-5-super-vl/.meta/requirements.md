# Documentation Requirements

## Requirements

- Identify NVIDIA Nemotron 3.5 Super VL as a distinct NVIDIA checkpoint released on 2026-10-15.
- Preserve the distinction from the separately released Super VL Base checkpoint and from text-focused Nemotron 3 Super.
- Preserve exact Super Base initialization and Ultra Base distillation provenance; add graph relations only after source-specific endpoint review and never substitute their post-trained counterparts.
- Keep deployment and benchmark claims source-scoped.

- Preserve the source-explicit Super Base initialization using reciprocal derived-from / has-derivative relations. Keep Ultra Base teacher distillation distinct from backbone initialization; do not substitute post-trained Ultra.

## Validation

- Family membership resolves reciprocally through Nemotron 3; producer provenance remains inherited through the existing family relation chain.
- Exact source and trained identity remain distinct from serving artifacts.
