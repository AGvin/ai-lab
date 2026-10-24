# Documentation Requirements

## Identity and decision boundaries

- Identify the exact upstream checkpoint `https://huggingface.co/ibm-granite/granite-embedding-small-english-r2` and its Apache-2.0 weight license.
- The card documents an 8192-token context. Use the checkpoint-specific embedding contract and benchmark the size/quality tradeoff.
- Do not infer a derived-from edge to the larger retriever solely from the smaller architecture.

## Validation

- Resolve identity, family membership and declared inverse relations to canonical entities.
- Keep downloaded-weight licensing separate from hosted terms and runtime-specific artifacts.
- Pin the selected checkpoint and runtime before deployment; measure memory, latency and task quality on representative inputs.
- Published benchmark results are producer claims; this documentation does not establish runtime or benchmark reproduction, cache freshness or final-render validation.
