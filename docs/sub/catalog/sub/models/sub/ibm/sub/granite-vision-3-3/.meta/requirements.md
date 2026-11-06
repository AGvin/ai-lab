# Documentation Requirements

## Identity and decision boundaries

- The 2B generator has a newer Vision generation; retain it here as the explicit parent of the independently useful embedding model.
- Separate image-to-text generation from ColBERT-style page multi-vector retrieval; the latter is not a text-generation endpoint.
- Preserve the source-explicit 2B-to-embedding derivative pair and do not transfer experimental generator features to the embedding checkpoint.
- The selected member weights use Apache-2.0; retain member-specific runtime and task boundaries.

## Validation

- Resolve identity, family membership and declared inverse relations to canonical entities.
- Keep downloaded-weight licensing separate from hosted terms and runtime-specific artifacts.
- Pin the selected checkpoint and runtime before deployment; measure memory, latency and task quality on representative inputs.
- Published benchmark results are producer claims; this documentation does not establish runtime or benchmark reproduction, cache freshness or final-render validation.
