# Documentation Requirements

## Requirements

- Identify DeepSeek-V4.1 as a model series within the DeepSeek family and keep it distinct from the earlier DeepSeek-V4 series.
- Preserve only source-backed characteristics genuinely shared at V4.1 series scope.
- Link materialized concrete V4.1 models without treating the series as a provider alias or API route.
- Keep provider pricing, mutable serving aliases, quotas, and other hosted-service state outside intrinsic series facts.

## Validation

- DeepSeek-V4.1 is represented as a series, not as a second DeepSeek family.
- V4.1 facts are not silently generalized back to DeepSeek-V4.
- Concrete V4.1 models remain distinct member identities.
