# Documentation Requirements

## Requirements

- Identify Qwen3-Nemotron-235B-A22B-GenRM as a separately released NVIDIA model with public weights and an official model card.
- Keep the exact Qwen3-235B-A22B-Thinking-2507 foundation textual until its canonical endpoint exists; use as a reward evaluator in Nano training does not establish backbone derivation of Nano.
- Keep licensing, training stage, intended use and source-reported evaluations specific to this checkpoint; do not inherit terms from similarly named Nemotron releases.
- Keep runtime support, quantization variants and hardware capacity claims outside stable identity.

## Validation

- Membership resolves reciprocally to the canonical parent and NVIDIA producer provenance follows the existing Nemotron family relation.
- Preserve one trained model identity across serving formats; neither a hosted inference endpoint nor local execution has been validated by this catalog entry.
