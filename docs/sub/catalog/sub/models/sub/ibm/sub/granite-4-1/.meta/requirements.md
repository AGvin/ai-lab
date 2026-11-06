# Documentation Requirements

## Identity and decision boundaries

- Keep all six trained checkpoints separate; base weights serve adaptation/pretraining workflows while instruct weights target assistant and tool-use workflows.
- This established generation remains relevant to the Granite ecosystem; do not present it as the newest Granite language generation.
- Use each checkpoint card for context, language and runtime constraints; do not infer them from parameter labels.
- The selected member weights use Apache-2.0; retain member-specific runtime and task boundaries.

## Validation

- Resolve identity, family membership and declared inverse relations to canonical entities.
- Keep downloaded-weight licensing separate from hosted terms and runtime-specific artifacts.
- Pin the selected checkpoint and runtime before deployment; measure memory, latency and task quality on representative inputs.
- Published benchmark results are producer claims; this documentation does not establish runtime or benchmark reproduction, cache freshness or final-render validation.
