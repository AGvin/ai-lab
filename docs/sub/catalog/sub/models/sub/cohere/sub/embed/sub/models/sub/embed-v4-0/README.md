# Embed 4

Embed 4 is Cohere’s multimodal embedding model identified by embed-v4.0.

## Identity and provenance

The release establishes text, image and mixed-content embeddings in one vector. It is a distinct generation from Embed 5 and remains listed in the current model comparison. [Embed 4 release](https://docs.cohere.com/changelog/embed-multimodal-v4) [Cohere Embed model comparison](https://docs.cohere.com/docs/cohere-embed).

## Decision and operating boundaries

- The model has a 128K context and supports over 100 languages. Output dimensions are 256, 512, 1024 and 1536, with 1536 as the documented default; do not apply Embed 5’s 768 or 2048 dimensions to this version. [Cohere Embed model comparison](https://docs.cohere.com/docs/cohere-embed) [Embed 4 release](https://docs.cohere.com/changelog/embed-multimodal-v4).
- Choose the query/document input role and endpoint preprocessing deliberately, and keep the same model and vector representation across an index unless an explicit compatibility contract says otherwise. Long-context support does not ensure useful retrieval without appropriate chunking and evaluation. [Cohere Embed model comparison](https://docs.cohere.com/docs/cohere-embed) [Embed API reference](https://docs.cohere.com/reference/embed).
- Cohere documents its own platform, SageMaker and Microsoft deployment routes. No downloadable weight license or public parameter count was established here; a provider endpoint is a distribution route rather than another model. [Embed 4 release](https://docs.cohere.com/changelog/embed-multimodal-v4) [Cohere Embed model comparison](https://docs.cohere.com/docs/cohere-embed).

## Catalog relations

- [Embed](../../../../) — series or family.

## Official resources

- [Embed 4 release](https://docs.cohere.com/changelog/embed-multimodal-v4).
- [Embed API reference](https://docs.cohere.com/reference/embed).
- [Cohere Embed model comparison](https://docs.cohere.com/docs/cohere-embed).
