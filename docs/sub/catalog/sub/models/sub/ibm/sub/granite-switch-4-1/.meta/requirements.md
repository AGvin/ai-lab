# Documentation Requirements

## Identity and decision boundaries

- Include the stable 8B and 30B checkpoints only; preview variants and standalone adapter libraries have separate lifecycle/ownership gates.
- Explain component selection through the documented chat template and control tokens; the composition is not evidence that every backend supports every mode.
- Keep the embedded speech component revision and language claims separate from later updates to standalone TurboCTC weights.
- The selected member weights use Apache-2.0; retain member-specific runtime and task boundaries.

## Validation

- Resolve identity, family membership and declared inverse relations to canonical entities.
- Keep downloaded-weight licensing separate from hosted terms and runtime-specific artifacts.
- Pin the selected checkpoint and runtime before deployment; measure memory, latency and task quality on representative inputs.
- Published benchmark results are producer claims; this documentation does not establish runtime or benchmark reproduction, cache freshness or final-render validation.
