# Embed

Embed is Cohere’s embedding-model family for semantic search, multilingual retrieval, classification and clustering.

## Identity and provenance

The Embed family contains three historical retired v2 text-embedding models (English, English Light and Multilingual), four later v3 checkpoints (English/Multilingual; standard/Light), Embed 4, and Embed 5 Pro and Fast. Each concrete model produces vectors; the family is not a vector database, search service or text-answering model. [Cohere Embed model comparison](https://docs.cohere.com/docs/cohere-embed) [Embed 5 release](https://docs.cohere.com/changelog/embed-v5).

## Decision and operating boundaries

- The three original **Embed v2** API model identities are separately named: `embed-english-v2.0`, `embed-english-light-v2.0` and `embed-multilingual-v2.0`. Cohere's April 26, 2023 rename maps them from the former `large`, `small` and `multilingual-22-12` model names; the old names are **aliases, not additional models**. All three historical hosted routes were **retired 4 April 2026**: requests fail. [Original model rename](https://docs.cohere.com/changelog/model-names-are-changing) [Retirement](https://docs.cohere.com/changelog/2026-04-04-embed-v2-aya-8b-retirement) [Deprecation index](https://docs.cohere.com/docs/deprecations).
- Historical v2 embeddings are **text-only**. Do not inherit v3 image-input modes, mandatory v3 `input_type`, v4/v5 mixed text/image embedding, optional output dimensions or v5 Pro/Fast shared embedding spaces. Source-verified v2 API names and model scopes are stronger than historical details of exact fixed vector dimensions or context: those values require dated original evidence before prescribing a migration. [Model rename](https://docs.cohere.com/changelog/model-names-are-changing) [Cohere Embed API](https://docs.cohere.com/reference/embed) [Current Embed table](https://docs.cohere.com/docs/cohere-embed).
- Deprecated v2 endpoints must not be recommended for new integrations. Migrations to live v3/v4/v5 routes require application-side re-embedding, index and similarity review, task-specific quality tests, rights/compliance checks and eligibility verification; an older name or reported model throughput is not proof of interchangeable vectors. No downloadable weight rights, independent benchmark, ownership tracing or runtime execution is claimed. [Retirement](https://docs.cohere.com/changelog/2026-04-04-embed-v2-aya-8b-retirement) [Model comparison](https://docs.cohere.com/docs/cohere-embed).
- Embed 4 and the two Embed 5 members accept text, images and mixed content, but supported vector dimensions and defaults differ. Version 5 Pro and Fast explicitly share an embedding space, allowing Pro indexing with Fast querying when dimensions, encodings and preprocessing are compatible with the retrieval system. [Cohere Embed model comparison](https://docs.cohere.com/docs/cohere-embed) [Embed 4 release](https://docs.cohere.com/changelog/embed-multimodal-v4) [Embed 5 release](https://docs.cohere.com/changelog/embed-v5).
- Choose output dimension, numeric representation, input type and truncation with the exact endpoint contract. Do not infer compatibility between Embed 4 and Embed 5 merely because Pro/Fast interoperability is documented within version 5. [Cohere Embed model comparison](https://docs.cohere.com/docs/cohere-embed) [Embeddings usage guide](https://docs.cohere.com/docs/embeddings) [Embed API reference](https://docs.cohere.com/reference/embed).
- Current public sources describe hosted and managed deployment routes; this audit establishes no downloadable weights, parameter total or open-weight license for these members. Provider search-quality comparisons require task-specific validation. [Embed 4 release](https://docs.cohere.com/changelog/embed-multimodal-v4) [Embed 5 release](https://docs.cohere.com/changelog/embed-v5).

- Four earlier Embed v3 models are now separately materialized: English/Multilingual standard (1,024-dimensional) and Light (384-dimensional), each with 512-token input context. They accept text and individual image embedding inputs through version-3-specific APIs, **not** the fused mixed input format of v4/v5. Version 3 requires `input_type`; each v3 image request is limited to one image up to 5 MB. [Cohere model table](https://docs.cohere.com/docs/models) [Embed v2 API](https://docs.cohere.com/reference/embed).
- Older v3 index dimensions and embedding spaces must not silently reuse v4/v5 indexes or assume documented v5 Pro/Fast cross-tier compatibility. The April 2026 retirement only names older v2 embeddings; v3 appears in current model tables but exact regional/account availability still requires revalidation. [Cohere Embed guide](https://docs.cohere.com/docs/cohere-embed) [Retirement notice](https://docs.cohere.com/changelog/2026-04-04-embed-v2-aya-8b-retirement).

## Catalog relations

- [Cohere](../../../../../producers/sub/c/sub/cohere/) — producer.
- [Embed English v2](sub/models/sub/embed-english-v2-0/) — retired historical v2 member.
- [Embed English Light v2](sub/models/sub/embed-english-light-v2-0/) — retired historical v2 member.
- [Embed Multilingual v2](sub/models/sub/embed-multilingual-v2-0/) — retired historical v2 member.
- [Embed English v3](sub/models/sub/embed-english-v3-0/) — member.
- [Embed English Light v3](sub/models/sub/embed-english-light-v3-0/) — member.
- [Embed Multilingual v3](sub/models/sub/embed-multilingual-v3-0/) — member.
- [Embed Multilingual Light v3](sub/models/sub/embed-multilingual-light-v3-0/) — member.
- [Embed 4](sub/models/sub/embed-v4-0/) — member.
- [Embed 5 Fast](sub/models/sub/embed-v5-0-fast/) — member.
- [Embed 5 Pro](sub/models/sub/embed-v5-0-pro/) — member.

## Official resources

- [Original 2023 model-name mapping](https://docs.cohere.com/changelog/model-names-are-changing).
- [Embed v2 retirement](https://docs.cohere.com/changelog/2026-04-04-embed-v2-aya-8b-retirement).
- [Cohere deprecation history](https://docs.cohere.com/docs/deprecations).
- [Embed 4 release](https://docs.cohere.com/changelog/embed-multimodal-v4).
- [Cohere Embed model comparison](https://docs.cohere.com/docs/cohere-embed).
- [Embed 5 release](https://docs.cohere.com/changelog/embed-v5).
- [Embeddings usage guide](https://docs.cohere.com/docs/embeddings).
- [Embed API reference](https://docs.cohere.com/reference/embed).
- [Embed v2 retirement scope](https://docs.cohere.com/changelog/2026-04-04-embed-v2-aya-8b-retirement).
