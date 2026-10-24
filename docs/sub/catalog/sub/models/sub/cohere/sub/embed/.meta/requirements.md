# Documentation Requirements

## Identity and provenance

- Embed is Cohere’s embedding-model family for semantic search, multilingual retrieval, classification and clustering.
- The current materialized members are Embed 4, Embed 5 Pro and Embed 5 Fast. Each concrete model produces vectors; the family is not a vector database, search service or text-answering model. [Cohere Embed model comparison](https://docs.cohere.com/docs/cohere-embed) [Embed 5 release](https://docs.cohere.com/changelog/embed-v5).

## Operational decision boundaries

- Embed 4 and the two Embed 5 members accept text, images and mixed content, but supported vector dimensions and defaults differ. Version 5 Pro and Fast explicitly share an embedding space, allowing Pro indexing with Fast querying when dimensions, encodings and preprocessing are compatible with the retrieval system. [Cohere Embed model comparison](https://docs.cohere.com/docs/cohere-embed) [Embed 4 release](https://docs.cohere.com/changelog/embed-multimodal-v4) [Embed 5 release](https://docs.cohere.com/changelog/embed-v5).
- Choose output dimension, numeric representation, input type and truncation with the exact endpoint contract. Do not infer compatibility between Embed 4 and Embed 5 merely because Pro/Fast interoperability is documented within version 5. [Cohere Embed model comparison](https://docs.cohere.com/docs/cohere-embed) [Embeddings usage guide](https://docs.cohere.com/docs/embeddings) [Embed API reference](https://docs.cohere.com/reference/embed).
- Current public sources describe hosted and managed deployment routes; this audit establishes no downloadable weights, parameter total or open-weight license for these members. Provider search-quality comparisons require task-specific validation. [Embed 4 release](https://docs.cohere.com/changelog/embed-multimodal-v4) [Embed 5 release](https://docs.cohere.com/changelog/embed-v5).

## Validation

- Preserve this canonical ID, type, aliases and prior relation membership; apply only the exact source-backed additive provenance and derivative repairs assessed for this node.
- Render every visible current-entity relation through the standard entity-relations contract, respecting explicit order and deterministic target-name ordering; resolve every local reader link.
- Project the complete identity and operating contract into the English reader. Attribute current limits and licenses to their precise source and distinguish models, artifacts, organizations and services.
- This documentation assessment grants no runtime, benchmark, downloaded-weight verification, cache, final-rendering, clean-pass or final-gate credit.
