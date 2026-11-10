# Jina Reader API

**Jina Reader API** is Jina AI's hosted web-data service that turns webpages and documents into LLM-friendly text and offers search results as text. The first-party [API reference](https://docs.jina.ai/) distinguishes `r.jina.ai` for reading and `s.jina.ai` for search from the separately cataloged `api.jina.ai` foundation-model endpoints.

## Reader and Search

The [official Reader site](https://jina.ai/reader) describes URL conversion, including browser-rendered pages and supported document formats. Requests to `r.jina.ai/{url}` return extracted readable content; `s.jina.ai` performs web search and text retrieval. Search requires a key; Reader may permit lower-rate unauthenticated requests. Authentication, quotas, processing regions and supported input types differ by endpoint and plan.

The [pinned upstream source README](https://github.com/jina-ai/reader/blob/1574bfd380d249c86c82db4dace0d9c8fe17e2b1/README.md) explicitly distinguishes the public **Apache-2.0 code branch** from the MongoDB-backed service storage not included in that checkout. Self-hostable source code is not the same product as access to Jina's hosted Reader API.

## Operational and rights boundaries

Web URLs, rendered content, proprietary PDFs, user queries and downloaded documents can contain private, copyrighted or hostile content. Enforce URL/input restrictions, protect API keys, treat extracted text as untrusted, check publisher terms and avoid unauthorized redistribution. Rate limits, data-processing options and payment rules are mutable.

No live web retrieval, extracted-data redistribution review, API request test or whole-catalog clean pass is claimed.

## Official sources

- [Jina API host reference](https://docs.jina.ai/)
- [Reader product](https://jina.ai/reader)
- [Pinned code README](https://github.com/jina-ai/reader/blob/1574bfd380d249c86c82db4dace0d9c8fe17e2b1/README.md)
- [Pinned source license](https://github.com/jina-ai/reader/blob/1574bfd380d249c86c82db4dace0d9c8fe17e2b1/LICENSE)
