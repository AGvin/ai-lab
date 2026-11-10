# Documentation Requirements

## Requirements

- Identify Qwen3-Nemotron-235B-A22B-GenRM-2603 as a separately released NVIDIA model with public weights and an official model card.
- Preserve the separate 2603 trained checkpoint and its Super RLHF role; do not infer a derivative relation to the earlier GenRM or backbone derivation of Super.
- Keep licensing, training stage, intended use and source-reported evaluations specific to this checkpoint; do not inherit terms from similarly named Nemotron releases.
- Keep runtime support, quantization variants and hardware capacity claims outside stable identity.

## Validation

- Membership resolves reciprocally to the canonical parent and NVIDIA producer provenance follows the existing Nemotron family relation.
- Preserve one trained model identity across serving formats; neither a hosted inference endpoint nor local execution has been validated by this catalog entry.
