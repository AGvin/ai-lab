# Documentation Requirements

## Identity and provenance

- Embed Multilingual v3 is a distinct prior-generation Cohere-hosted embedding model with the exact API identifier `embed-multilingual-v3.0`. The current Cohere table distinguishes the multilingual standard variant from other 3.x releases and all v4/v5 models; it is not an alias or a selectable output-dimension setting of another checkpoint. [Cohere Embed model table](https://docs.cohere.com/docs/cohere-embed) [Cohere models](https://docs.cohere.com/docs/models).
- Cohere documents **1024 fixed vector dimensions**, **512-token model context** and cosine similarity for this v3 model. The text language focus is multilingual (over 100 languages per Cohere's support table); do not infer equivalent text quality or cross-model vector-space alignment from the name. [Cohere Embed model table](https://docs.cohere.com/docs/cohere-embed).

## Operational decision boundaries

- Embeddings provide vectors for semantic search, classification and clustering; they are not chat, document search engines or reranking/answer-generation models. Set required v3+ `input_type` to `search_document` when indexing and `search_query` when querying; `classification`/`clustering` are separate processing intents, not new model IDs. [Embedding usage](https://docs.cohere.com/docs/embeddings) [Embed v2 API](https://docs.cohere.com/reference/embed).
- The documented v3 endpoint supports text and **separate** image embedding inputs. For v3 images the current API permits one 5 MB JPEG/PNG/WEBP/GIF image per request and `input_type=image`. **Fused mixed text-and-image in one vector is a version 4/5 capability**, not an assumed feature of this v3 checkpoint. [Embed v2 API](https://docs.cohere.com/reference/embed) [Embedding usage](https://docs.cohere.com/docs/embeddings).
- The fixed 1024-dimension vectors, 512-token truncation boundary and model-specific representation mean existing v4/v5 embeddings, other v3 tiers or changed input-type preprocessing cannot simply be mixed in one index. Re-embed/reindex and verify normalization, similarity metric and task-specific retrieval quality when migrating. Even dimensionally matching v3 models are not guaranteed to share embedding spaces. [Cohere model comparison](https://docs.cohere.com/docs/cohere-embed) [Embed API](https://docs.cohere.com/reference/embed).
- Model v3 remains listed as a prior-generation API identity in current Cohere documentation, and the 2026-04 retirement announcement applies to **v2**, not v3. Current account, region, billing and third-party platform availability are deployment-specific. Model-name presence does not prove publicly downloadable weights, unrestrictive commercial licensing, throughput, or independent benchmarks. [Models](https://docs.cohere.com/docs/models) [Retirement notice](https://docs.cohere.com/changelog/2026-04-04-embed-v2-aya-8b-retirement).
- This source review did not test request behavior, weight access, price, independent embedding quality, parameter counts, beneficial ownership or Russian-control claims. Do not promote unsupported safety/provenance classifications.

## Validation

- Keep this unique model ID, source-backed v3 service identity and one reciprocal Embed family membership pair; no invented training ancestry, provider, or image-mode-model duplicates.
- The reader must preserve 1024 dimensions, 512-token ceiling, image/input-type boundaries, rights and version-specific migrations; validate linked canonical pages.
- No current-HEAD full schema/cache/CI, local embedding inference, clean research pass or final publication gate credit from this bounded source intake.
