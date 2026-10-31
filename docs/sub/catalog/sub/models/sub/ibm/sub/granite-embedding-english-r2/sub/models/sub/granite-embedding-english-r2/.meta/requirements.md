# Documentation Requirements

## Identity and decision boundaries

- Identify the exact upstream checkpoint `https://huggingface.co/ibm-granite/granite-embedding-english-r2` and its Apache-2.0 weight license.
- Use as a retrieval encoder with its tokenizer, pooling and normalization contract; validate query/document matching on the target corpus.
- This model is the explicitly named parent of the English R2 reranker; preserve the reciprocal derivative edge.

## Validation

- Resolve identity, family membership and declared inverse relations to canonical entities.
- Keep downloaded-weight licensing separate from hosted terms and runtime-specific artifacts.
- Pin the selected checkpoint and runtime before deployment; measure memory, latency and task quality on representative inputs.
- Published benchmark results are producer claims; this documentation does not establish runtime or benchmark reproduction, cache freshness or final-render validation.
