# Documentation Requirements

## Identity and decision boundaries

- Distinguish the 4-layer 38M and 12-layer 125M classifiers and their throughput/quality tradeoff.
- HAP detects hateful, abusive, profane and other toxic English text; it is not the broader generative Guardian risk evaluator.
- Calibrate thresholds and evaluate false positives and false negatives on the target domain; classifier output is not a universal safety guarantee.
- The selected member weights use Apache-2.0; retain member-specific runtime and task boundaries.

## Validation

- Resolve identity, family membership and declared inverse relations to canonical entities.
- Keep downloaded-weight licensing separate from hosted terms and runtime-specific artifacts.
- Pin the selected checkpoint and runtime before deployment; measure memory, latency and task quality on representative inputs.
- Published benchmark results are producer claims; this documentation does not establish runtime or benchmark reproduction, cache freshness or final-render validation.
