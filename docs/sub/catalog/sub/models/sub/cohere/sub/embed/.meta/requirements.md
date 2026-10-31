# Documentation Requirements

## Identity and provenance

- Embed is Cohere’s embedding-model family for semantic search, multilingual retrieval, classification and clustering.
- The materialized Embed family now contains four separately named Embed v3 (English/Multilingual; standard/Light) checkpoints plus Embed 4, Embed 5 Pro and Embed 5 Fast. Each concrete model produces vectors; the family is not a vector database, search service or text-answering model. [Cohere Embed model comparison](https://docs.cohere.com/docs/cohere-embed) [Embed 5 release](https://docs.cohere.com/changelog/embed-v5).

## Operational decision boundaries

- Embed 4 and the two Embed 5 members accept text, images and mixed content, but supported vector dimensions and defaults differ. Version 5 Pro and Fast explicitly share an embedding space, allowing Pro indexing with Fast querying when dimensions, encodings and preprocessing are compatible with the retrieval system. [Cohere Embed model comparison](https://docs.cohere.com/docs/cohere-embed) [Embed 4 release](https://docs.cohere.com/changelog/embed-multimodal-v4) [Embed 5 release](https://docs.cohere.com/changelog/embed-v5).
- Choose output dimension, numeric representation, input type and truncation with the exact endpoint contract. Do not infer compatibility between Embed 4 and Embed 5 merely because Pro/Fast interoperability is documented within version 5. [Cohere Embed model comparison](https://docs.cohere.com/docs/cohere-embed) [Embeddings usage guide](https://docs.cohere.com/docs/embeddings) [Embed API reference](https://docs.cohere.com/reference/embed).
- Current public sources describe hosted and managed deployment routes; this audit establishes no downloadable weights, parameter total or open-weight license for these members. Provider search-quality comparisons require task-specific validation. [Embed 4 release](https://docs.cohere.com/changelog/embed-multimodal-v4) [Embed 5 release](https://docs.cohere.com/changelog/embed-v5).

- The four legacy Embed v3 API identities are each distinct: `embed-english-v3.0` (1,024 dimensions), `embed-english-light-v3.0` (384), `embed-multilingual-v3.0` (1,024), and `embed-multilingual-light-v3.0` (384), each with a **512-token context**. These are previous-generation endpoints, not trained aliases or interchangeable vector-index dimensions. Cohere lists them in current Embed model and platform tables, including restricted deployment differences. [Cohere Embed model table](https://docs.cohere.com/docs/cohere-embed) [Cohere model inventory](https://docs.cohere.com/docs/models).
- Version 3 embeds text or single images through separate input branches; `input_type` is mandatory. Current v2 API allows at most **one 5MB image per v3 request** and does not provide the v4/v5 fused text-and-image input behavior. `search_document` and `search_query` preprocessing must match indexing use, and changing model/vector size/embedding space needs re-embedding and matching vector index rather than assuming v5 Pro/Fast compatibility applies to v3. [Embed API](https://docs.cohere.com/reference/embed) [Embedding usage guide](https://docs.cohere.com/docs/embeddings).
- The April 2026 retirement notice concerns **Embed v2**, not v3. This historical v3 catalog materialization is not a recommendation to prefer v3 for new projects; verify current account/model availability, output size and price. Public hosted listings do not establish open weights or a public weight license. [2026 Embed v2 retirement](https://docs.cohere.com/changelog/2026-04-04-embed-v2-aya-8b-retirement) [Cohere Embed model table](https://docs.cohere.com/docs/cohere-embed).

## Validation

- Preserve this canonical ID, type, aliases and prior relation membership; apply only the exact source-backed additive provenance and derivative repairs assessed for this node.
- Render every visible current-entity relation through the standard entity-relations contract, respecting explicit order and deterministic target-name ordering; resolve every local reader link.
- Project the complete identity and operating contract into the English reader. Attribute current limits and licenses to their precise source and distinguish models, artifacts, organizations and services.
- This documentation assessment grants no runtime, benchmark, downloaded-weight verification, cache, final-rendering, clean-pass or final-gate credit.
