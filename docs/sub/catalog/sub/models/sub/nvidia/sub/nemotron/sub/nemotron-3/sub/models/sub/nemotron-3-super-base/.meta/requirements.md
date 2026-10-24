# Documentation Requirements

## Requirements

- Identify NVIDIA Nemotron 3 Super Base as a separately released NVIDIA model with public weights and an official model card.
- Preserve pretrained Super Base as distinct from post-trained Super and Super VL Base; NVFP4 pretraining does not make BF16 weights a separate trained identity.
- Keep licensing, training stage, intended use and source-reported evaluations specific to this checkpoint; do not inherit terms from similarly named Nemotron releases.
- Keep runtime support, quantization variants and hardware capacity claims outside stable identity.

## Validation

- Membership resolves reciprocally to the canonical parent and NVIDIA producer provenance follows the existing Nemotron family relation.
- Preserve one trained model identity across serving formats; neither a hosted inference endpoint nor local execution has been validated by this catalog entry.
