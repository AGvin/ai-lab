# Documentation Requirements

## Historical identity and status

- Exact historical API identity: `embed-english-v2.0` for English-language text semantic embeddings for search, clustering and classification. Cohere's **26 April 2023** rename maps the prior name `large` to this versioned identifier; it is a renamed service model, not a second alias model. Original full-size English v2 service identity; distinct from Light v2 and from each v3/v4/v5 checkpoint. [Cohere rename](https://docs.cohere.com/changelog/model-names-are-changing).
- All three Cohere Embed v2 hosted model IDs were **retired 4 April 2026**; this model is no longer available through its legacy Cohere API route. The official retirement advises a fresh model/reindex decision rather than calling the v2 endpoint. [Retirement notice](https://docs.cohere.com/changelog/2026-04-04-embed-v2-aya-8b-retirement) [Deprecations](https://docs.cohere.com/docs/deprecations).

## Operational boundaries

- This is a historical **text-only semantic embedding** model, not a chat generator, reranker, database, image-embedding model or a model-download license. Its fixed historical vector size/context must be verified against an exact archived provider contract before an operational migration; current v3/v4/v5 values are **not** valid substitutes. [Cohere model history](https://docs.cohere.com/changelog/model-names-are-changing) [Embedding API](https://docs.cohere.com/reference/embed).
- V2 features, provider availability and indexing behavior differ from newer Embed releases. Do not assume `input_type` handling, binary vectors, image inputs, configurable output dimensions, parameter size, embedding-space compatibility or independently validated model quality. The retirement date makes this model inappropriate for **new** endpoint integrations. [Embedding API](https://docs.cohere.com/reference/embed) [Retirement](https://docs.cohere.com/changelog/2026-04-04-embed-v2-aya-8b-retirement).
- Neither a public weight repository, an open-weight license, independent inference/benchmark nor ultimate beneficial ownership was established. Any migration needs explicit vector re-embedding/index compatibility evaluation and new endpoint access confirmation. [Cohere models](https://docs.cohere.com/docs/models).

## Validation

- Preserve distinct v2 English/Light/Multilingual IDs while treating the 2023 original names as aliases only. Check the exact reciprocal parent Embed series membership, source evidence and reader links.
- Grant no API availability, download license, exact dimensionality, runtime, benchmarks, whole-catalog freshness, cache/schema/CI or publication gates without independent verification.
