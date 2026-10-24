# Embed 5 Fast

Embed 5 Fast is Cohere’s multimodal embedding model for low-latency, high-throughput querying.

## Identity and provenance

The release names embed-v5.0-fast as a concrete model. Pro and Fast are distinct model identities with a documented shared embedding space; shared space does not imply identical learned weights or identical retrieval quality. [Embed 5 release](https://docs.cohere.com/changelog/embed-v5) [Cohere Embed model comparison](https://docs.cohere.com/docs/cohere-embed).

## Decision and operating boundaries

- Version 5 supports text, image and mixed inputs, over 100 languages and a 128K context. It offers dimensions 256, 512, 768, 1024, 1536 and 2048, with 2048 as the documented default, and float, int8 and binary representations. [Cohere Embed model comparison](https://docs.cohere.com/docs/cohere-embed) [Embed 5 release](https://docs.cohere.com/changelog/embed-v5).
- Cohere recommends indexing with Pro and querying with Fast. Use compatible dimensions and preprocessing and ensure the retrieval system supports the chosen numeric encodings; Pro/Fast interoperability does not automatically make existing Embed 4 vectors compatible. Query and document input types remain distinct. [Embed 5 release](https://docs.cohere.com/changelog/embed-v5) [Embeddings usage guide](https://docs.cohere.com/docs/embeddings) [Embed API reference](https://docs.cohere.com/reference/embed).
- The Fast role is provider positioning, not a locally reproduced quality or latency ranking. The release documents Cohere API, Foundry, SageMaker and Model Vault routes; no public downloadable weight license or parameter count was established in this audit. [Embed 5 release](https://docs.cohere.com/changelog/embed-v5) [Cohere Embed model comparison](https://docs.cohere.com/docs/cohere-embed).

## Catalog relations

- [Embed](../../../../) — series or family.

## Official resources

- [Embed 5 release](https://docs.cohere.com/changelog/embed-v5).
- [Embeddings usage guide](https://docs.cohere.com/docs/embeddings).
- [Cohere Embed model comparison](https://docs.cohere.com/docs/cohere-embed).
- [Embed API reference](https://docs.cohere.com/reference/embed).
