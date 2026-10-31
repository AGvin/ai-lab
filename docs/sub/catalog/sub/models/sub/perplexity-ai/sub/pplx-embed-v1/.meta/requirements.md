# Documentation Requirements

## Requirements

- Identify PPLX Embed V1 as Perplexity AI's released first-generation embedding family.
- Preserve the distinction among standard dense embeddings, contextualized dense embeddings, and the independently published 0.6B late-interaction derivative.
- Keep concrete parameter class, dimensions, context length, quantization/output format, pooling or MaxSim behavior, model-card artifacts, and serving characteristics with the concrete member or current first-party service documentation.
- Keep Perplexity Embeddings API pricing, quotas, batching, endpoint behavior and client SDKs outside intrinsic model-family identity.
- Render the standard `entity-relations` block from validated current-entity relations.

## Validation

- The family remains distinct from the hosted Embeddings API service.
- Dense, contextualized and late-interaction representations are not silently conflated.
- PPLX Embed V1 Late 0.6B remains a derivative of the standard 0.6B model rather than an alias.
- Producer provenance resolves bidirectionally to Perplexity AI.

## Source-backed reader scope — 2026-10-23

- Identity and provenance: four dense/contextual members cover the 0.6B and 4B sizes; `pplx-embed-v1-late-0.6b` is a distinct MIT-licensed token-level MaxSim retriever continued from `pplx-embed-v1-0.6b`.
- Decision and deployment boundary: select standard dense, document-contextualized dense, or late-interaction retrieval intentionally; their index representations and scoring methods are not interchangeable.
- Render every visible current relation using canonical target names, explicit order first and alphabetical order within each relation group. Keep metadata paths out of reader navigation.
- Recheck account eligibility, exact artifact access, versions and terms before deployment. This source review does not certify runtime performance.
- Reviewed sources: <https://www.perplexity.ai/hub/blog/pplx-embed-state-of-the-art-embedding-models-for-web-scale-retrieval>, <https://huggingface.co/perplexity-ai/pplx-embed-v1-0.6b>, <https://huggingface.co/perplexity-ai/pplx-embed-context-v1-4b>, <https://huggingface.co/perplexity-ai/pplx-embed-v1-late-0.6b>.
