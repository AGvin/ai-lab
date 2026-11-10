# Documentation Requirements

## Requirements

- Identify NVIDIA Nemotron 3 Nano Base as a separately released NVIDIA model with public weights and an official model card.
- Keep the separately released Base training stage distinct from post-trained Nano and Nano Omni; do not transfer their instruction-following, multimodal or benchmark claims.
- Keep licensing, training stage, intended use and source-reported evaluations specific to this checkpoint; do not inherit terms from similarly named Nemotron releases.
- Keep runtime support, quantization variants and hardware capacity claims outside stable identity.

## Validation

- Membership resolves reciprocally to the canonical parent and NVIDIA producer provenance follows the existing Nemotron family relation.
- Preserve one trained model identity across serving formats; neither a hosted inference endpoint nor local execution has been validated by this catalog entry.
