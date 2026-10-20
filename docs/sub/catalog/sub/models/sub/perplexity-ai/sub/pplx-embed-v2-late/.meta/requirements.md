# Documentation Requirements

## Requirements

- Identify PPLX Embed V2 Late as Perplexity AI's released October 7, 2026 multimodal late-interaction embedding/retrieval family, with separately packaged 0.6B and 9B models.
- Preserve the distinct ColBERT/MaxSim retrieval design: per-token 128-dimensional vectors, not one pooled dense vector per text document.
- Keep text, image and visual document retrieval, cross-size embedding-space compatibility and bidirectional attention as model-family capabilities only to the extent verified by current upstream model cards.
- Distinguish released V2 Late models from existing PPLX Embed V1 and V2 Context model artifacts outside this represented family. Appearing in a related collection does not establish family membership or release status.
- Keep Perplexity Embeddings API pricing, endpoint quotas and deployment/SDK integrations with their owning service/software, not as intrinsic model identities.
- Treat model card metrics, licensing, hardware memory, video support and exact indexing interoperability as freshness-sensitive and evaluated per checkpoint.

## Validation

- Only the two independently released V2 Late models are materialized under this family.
- Both model member relations and the family Perplexity producer inverse are reciprocal.
- A 128-dimensional *per-token* embedding is not misrepresented as a 128-dimensional single-vector retriever.
- V2 Late models are not conflated with V1 or preview V2 Context checkpoints.

## Source-backed reader scope — 2026-10-20

- Identity and provenance: PPLX Embed V2 Late is Perplexity's multimodal late-interaction retrieval family, with distinct 0.6B and 9B artifacts built on Qwen3.5. It scores per-token vectors with MaxSim.
- Decision and deployment boundary: Use a multivector index and the model-card inference path. Shared embedding space allows the documented smaller-query/larger-index combination, but does not make the two sizes equal in quality or resource use. The represented family contains only its two canonical Late members.
- Render every visible current relation using canonical target names, explicit order first and alphabetical order within each relation group. Keep metadata paths out of reader navigation.
- Recheck account eligibility, exact artifact access, versions and terms before deployment. This source review does not certify runtime performance.
- Reviewed sources: <https://huggingface.co/perplexity-ai/pplx-embed-v2-late-0.6b>, <https://huggingface.co/perplexity-ai/pplx-embed-v2-late-9b>.
