# Documentation Requirements

## Identity and decision boundaries

- Identify the exact upstream checkpoint `https://huggingface.co/ibm-granite/granite-switch-4.1-8b` and its Apache-2.0 weight license.
- Preserve the selected 8B/30B base identity and the bundled decision/guardian adapters and speech encoder.
- Use the supported runtime, processor and control-token contract for each mode; do not equate a modular checkpoint with arbitrary separately updated components.

## Validation

- Resolve identity, family membership and declared inverse relations to canonical entities.
- Keep downloaded-weight licensing separate from hosted terms and runtime-specific artifacts.
- Pin the selected checkpoint and runtime before deployment; measure memory, latency and task quality on representative inputs.
- Published benchmark results are producer claims; this documentation does not establish runtime or benchmark reproduction, cache freshness or final-render validation.
