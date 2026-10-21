# Documentation Requirements

## Identity and provenance

- Embed 4 is Cohere’s multimodal embedding model identified by embed-v4.0.
- The release establishes text, image and mixed-content embeddings in one vector. It is a distinct generation from Embed 5 and remains listed in the current model comparison. [Embed 4 release](https://docs.cohere.com/changelog/embed-multimodal-v4) [Cohere Embed model comparison](https://docs.cohere.com/docs/cohere-embed).

## Operational decision boundaries

- The model has a 128K context and supports over 100 languages. Output dimensions are 256, 512, 1024 and 1536, with 1536 as the documented default; do not apply Embed 5’s 768 or 2048 dimensions to this version. [Cohere Embed model comparison](https://docs.cohere.com/docs/cohere-embed) [Embed 4 release](https://docs.cohere.com/changelog/embed-multimodal-v4).
- Choose the query/document input role and endpoint preprocessing deliberately, and keep the same model and vector representation across an index unless an explicit compatibility contract says otherwise. Long-context support does not ensure useful retrieval without appropriate chunking and evaluation. [Cohere Embed model comparison](https://docs.cohere.com/docs/cohere-embed) [Embed API reference](https://docs.cohere.com/reference/embed).
- Cohere documents its own platform, SageMaker and Microsoft deployment routes. No downloadable weight license or public parameter count was established here; a provider endpoint is a distribution route rather than another model. [Embed 4 release](https://docs.cohere.com/changelog/embed-multimodal-v4) [Cohere Embed model comparison](https://docs.cohere.com/docs/cohere-embed).

## Validation

- Preserve this canonical ID, type, aliases and prior relation membership; apply only the exact source-backed additive provenance and derivative repairs assessed for this node.
- Render every visible current-entity relation through the standard entity-relations contract, respecting explicit order and deterministic target-name ordering; resolve every local reader link.
- Project the complete identity and operating contract into the English reader. Attribute current limits and licenses to their precise source and distinguish models, artifacts, organizations and services.
- This documentation assessment grants no runtime, benchmark, downloaded-weight verification, cache, final-rendering, clean-pass or final-gate credit.
