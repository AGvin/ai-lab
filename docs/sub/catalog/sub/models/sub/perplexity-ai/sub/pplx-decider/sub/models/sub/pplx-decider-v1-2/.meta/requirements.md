# Documentation Requirements

## Requirements

- Identify the exact `perplexity-ai/pplx-decider-v1.2` checkpoint as a distinct released PPLX Decider model on the Qwen3.8-27B backbone.
- Preserve source-backed joint multi-question request semantics, text/image input, per-question marker readout, calibration and Apache-2.0 license boundary.
- Keep benchmark gains, CUDA memory figures, compilation paths and grouping recommendations contextual and checkpoint-specific rather than family-wide guarantees.
- Keep the hosted Decisions API, billing, aliases and authentication separate from trained-model identity; the current card's authenticated repository instruction remains freshness-sensitive.

## Validation

- V1.2 is not collapsed into V1.1 or PPLX 27B.
- Its Qwen3.8-27B `derived-from` relation has the reciprocal base-model edge.
- Joint request support is not interpreted as free-form generation or unlimited validated sequence length.
