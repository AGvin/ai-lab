# Documentation Requirements

## Requirements

- Identify PPLX Embed V2 Late as Perplexity AI's released October 7, 2026 multimodal late-interaction embedding/retrieval family, with separately packaged 0.6B and 9B models.
- Preserve the distinct ColBERT/MaxSim retrieval design: per-token 128-dimensional vectors, not one pooled dense vector per text document.
- Keep text, image and visual document retrieval, cross-size embedding-space compatibility and bidirectional attention as model-family capabilities only to the extent verified by current upstream model cards.
- Distinguish released V2 Late models from existing PPLX Embed V1 and still-preview V2 Context model artifacts. A related preview appearing in a collection is not a stable released member.
- Keep Perplexity Embeddings API pricing, endpoint quotas and deployment/SDK integrations with their owning service/software, not as intrinsic model identities.
- Treat model card metrics, licensing, hardware memory, video support and exact indexing interoperability as freshness-sensitive and evaluated per checkpoint.

## Validation

- Only the two independently released V2 Late models are materialized under this family.
- Both model member relations and the family Perplexity producer inverse are reciprocal.
- A 128-dimensional *per-token* embedding is not misrepresented as a 128-dimensional single-vector retriever.
- V2 Late models are not conflated with V1 or preview V2 Context checkpoints.
