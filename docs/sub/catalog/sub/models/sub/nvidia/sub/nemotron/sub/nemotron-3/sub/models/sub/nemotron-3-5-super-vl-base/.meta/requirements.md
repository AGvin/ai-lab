# Documentation Requirements

## Requirements

- Identify NVIDIA Nemotron 3.5 Super VL Base as a distinct NVIDIA checkpoint released on 2026-10-15.
- Preserve the released base checkpoint as a separate trained identity rather than a precision variant of post-trained Super VL.
- Keep Nemotron 3 Super Base initialization and Ultra Base distillation distinct from similarly named post-trained models.
- Do not transfer post-trained behavior or benchmark results to this base checkpoint.

## Validation

- Family membership resolves reciprocally through Nemotron 3; producer provenance remains inherited through the existing family relation chain.
- Exact source and trained identity remain distinct from serving artifacts.
