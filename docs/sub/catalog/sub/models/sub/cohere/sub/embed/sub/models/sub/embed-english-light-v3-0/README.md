# Embed English Light v3

Embed English Light v3 is Cohere's earlier-generation english Light embedding model, identified as `embed-english-light-v3.0` in official model tables. It produces **384-dimensional** vectors with a **512-token** model context.

## Identity and provenance

The model is one of four distinct Embed v3 service model IDs. Light and full checkpoints are not interchangeable output-size switches; English and multilingual versions target different language needs. Cohere's current model table still lists them, but the latest family generation is v5. [Embed model details](https://docs.cohere.com/docs/cohere-embed) [Cohere models](https://docs.cohere.com/docs/models).

## Decision and operating boundaries

- Set mandatory `input_type` for v3 embedding API calls: `search_document` when building a vector corpus, `search_query` when retrieving, and `classification`/`clustering` when applicable. Vectors do not themselves retrieve documents or produce grounded answers. [Embeddings guide](https://docs.cohere.com/docs/embeddings) [Embed v2 API](https://docs.cohere.com/reference/embed).
- This version 3 model has **384 fixed dimensions**, **512 tokens of context**, and documented cosine similarity. Light is positioned as a smaller/faster alternative, but exact latency and ranking quality require measurement. Version 5 Pro/Fast interoperability is a **different version-specific contract**, not evidence that v3 and v4/v5 vector spaces can be mixed. [Cohere Embed details](https://docs.cohere.com/docs/cohere-embed).
- For version 3, image embedding is a separate image input mode (one image up to 5 MB per call, using a supported encoded image and `input_type=image`), not the fused text+image document format of newer models. Use the exact v3 endpoint contract rather than inferring multi-page PDF support. [Embeddings guide](https://docs.cohere.com/docs/embeddings) [Embed v2 API](https://docs.cohere.com/reference/embed).
- V2 embed models were retired on 2026-04-04, but these v3 IDs remain in the current model inventory. Verify actual tenant/region endpoint eligibility and prices before choosing a legacy model for new integrations. Switching embedding models usually requires re-embedding and vector index compatibility checks. [Retirement notice](https://docs.cohere.com/changelog/2026-04-04-embed-v2-aya-8b-retirement) [Cohere models](https://docs.cohere.com/docs/models).
- Current sources do not establish separately downloadable unrestricted model weights, measured throughput, internal parameter count or verified ultimate beneficial-owner/Russian control claims. No local inference or benchmark was performed.

## Catalog relations

- [Embed](../../../../) — model family.

## Official resources

- [Cohere Embed model table](https://docs.cohere.com/docs/cohere-embed).
- [Cohere model inventory](https://docs.cohere.com/docs/models).
- [Embed API v2 reference](https://docs.cohere.com/reference/embed).
- [Embedding usage guide](https://docs.cohere.com/docs/embeddings).
- [Embed v2 retirement notice](https://docs.cohere.com/changelog/2026-04-04-embed-v2-aya-8b-retirement).
