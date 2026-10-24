# Documentation Requirements

## Requirements

- Identify PII-Tracer as Perplexity's released PII masking/token-classification model, distinct from the PII-TRACE dataset/benchmark.
- Preserve its exact PPLX Embed V1 0.6B backbone lineage, bidirectional encoder use, token-classification and sensitivity heads, and MIT license boundary.
- Treat MLX, vLLM and GGUF repositories as packaging/runtime variants rather than separate trained-model identities unless their weights diverge semantically.
- Keep label taxonomy, decoding implementation, benchmark scores and runtime deployment guidance source-scoped and freshness-sensitive.

## Validation

- PII-Tracer reciprocates Perplexity producer provenance and the PPLX Embed V1 0.6B derivative relation.
- Dataset identity and model identity remain separate.
