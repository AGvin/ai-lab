# Documentation Requirements

## Identity and decision boundaries

- Identify the exact upstream checkpoint `https://huggingface.co/ibm-granite/granite-guardian-hap-38m` and its Apache-2.0 weight license.
- Use for English HAP screening and bulk annotation with measured false-positive/false-negative tradeoffs.
- Keep output labels and threshold calibration explicit; do not claim broad multilingual or general Guardian coverage.

## Validation

- Resolve identity, family membership and declared inverse relations to canonical entities.
- Keep downloaded-weight licensing separate from hosted terms and runtime-specific artifacts.
- Pin the selected checkpoint and runtime before deployment; measure memory, latency and task quality on representative inputs.
- Published benchmark results are producer claims; this documentation does not establish runtime or benchmark reproduction, cache freshness or final-render validation.
