# Documentation Requirements

## Identity and decision boundaries

- Identify the exact upstream checkpoint `https://huggingface.co/ibm-granite/granite-guardian-hap-125m` and its Apache-2.0 weight license.
- Evaluate the accuracy/throughput tradeoff against the smaller HAP checkpoint using representative English inputs.
- Keep output labels and threshold calibration explicit; contextual toxicity errors and bias require domain evaluation.

## Validation

- Resolve identity, family membership and declared inverse relations to canonical entities.
- Keep downloaded-weight licensing separate from hosted terms and runtime-specific artifacts.
- Pin the selected checkpoint and runtime before deployment; measure memory, latency and task quality on representative inputs.
- Published benchmark results are producer claims; this documentation does not establish runtime or benchmark reproduction, cache freshness or final-render validation.
