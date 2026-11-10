# Documentation Requirements

## Identity and decision boundaries

- Identify the exact upstream checkpoint `https://huggingface.co/ibm-granite/granite-embedding-reranker-english-r2` and its Apache-2.0 weight license.
- Use relevance scores from joint query/document encoding, not a bi-encoder vector-index interface; generic embedding wording in the card does not override its CrossEncoder usage.
- Preserve the explicit derived-from relation to the English R2 retriever; evaluate reranking quality and candidate-batch latency separately.

## Validation

- Resolve identity, family membership and declared inverse relations to canonical entities.
- Keep downloaded-weight licensing separate from hosted terms and runtime-specific artifacts.
- Pin the selected checkpoint and runtime before deployment; measure memory, latency and task quality on representative inputs.
- Published benchmark results are producer claims; this documentation does not establish runtime or benchmark reproduction, cache freshness or final-render validation.
