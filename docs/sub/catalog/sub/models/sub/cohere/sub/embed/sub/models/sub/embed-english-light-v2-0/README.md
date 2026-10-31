# Embed English Light v2

Embed English Light v2 (`embed-english-light-v2.0`) is a separately named historical Cohere **text-embedding** model, now retired from the hosted Cohere API.

## Historical identity and status

- Exact historical API identity: `embed-english-light-v2.0` for smaller, faster English-language text semantic embeddings for retrieval and classification. Cohere's **26 April 2023** rename maps the prior name `small` to this versioned identifier; it is a renamed service model, not a second alias model. Original reduced-compute Light identity with its own learned model; not a runtime output-dimension toggle of English v2 or a v3 alias. [Cohere rename](https://docs.cohere.com/changelog/model-names-are-changing).
- All three Cohere Embed v2 hosted model IDs were **retired 4 April 2026**; this model is no longer available through its legacy Cohere API route. The official retirement advises a fresh model/reindex decision rather than calling the v2 endpoint. [Retirement notice](https://docs.cohere.com/changelog/2026-04-04-embed-v2-aya-8b-retirement) [Deprecations](https://docs.cohere.com/docs/deprecations).

## Selection and operating boundaries

- This is a historical **text-only semantic embedding** model, not a chat generator, reranker, database, image-embedding model or a model-download license. Its fixed historical vector size/context must be verified against an exact archived provider contract before an operational migration; current v3/v4/v5 values are **not** valid substitutes. [Cohere model history](https://docs.cohere.com/changelog/model-names-are-changing) [Embedding API](https://docs.cohere.com/reference/embed).
- V2 features, provider availability and indexing behavior differ from newer Embed releases. Do not assume `input_type` handling, binary vectors, image inputs, configurable output dimensions, parameter size, embedding-space compatibility or independently validated model quality. The retirement date makes this model inappropriate for **new** endpoint integrations. [Embedding API](https://docs.cohere.com/reference/embed) [Retirement](https://docs.cohere.com/changelog/2026-04-04-embed-v2-aya-8b-retirement).
- Neither a public weight repository, an open-weight license, independent inference/benchmark nor ultimate beneficial ownership was established. Any migration needs explicit vector re-embedding/index compatibility evaluation and new endpoint access confirmation. [Cohere models](https://docs.cohere.com/docs/models).

## Catalog relations

- [Embed](../../../../) — model family.

## Official resources

- [Cohere original model renaming](https://docs.cohere.com/changelog/model-names-are-changing).
- [Cohere v2 retirement](https://docs.cohere.com/changelog/2026-04-04-embed-v2-aya-8b-retirement).
- [Deprecation history](https://docs.cohere.com/docs/deprecations).
- [Embedding API documentation](https://docs.cohere.com/reference/embed).
