# Jina Search Foundation API

**Jina Search Foundation API** is a managed embedding, reranking and document-processing service associated with [Jina AI](../../../../../producers/sub/j/sub/jina-ai/), whose acquisition by Elastic was completed in October 2025. This is a hosted API, not a single downloadable search model or the separate Elastic Inference Service.

## Endpoints and access

The [official API reference](https://docs.jina.ai/) distinguishes three hosts: `api.jina.ai` for foundation-model operations, `r.jina.ai` for webpage/PDF reading, and `s.jina.ai` for web search. Foundation model endpoints include `POST /v1/embeddings`, `POST /v1/rerank` and `GET /v1/models`. Reader and Search serve different workflows and should not be confused with embedding or reranker execution.

Authenticated model requests include `Authorization: Bearer` using a protected Jina API key. Reader supports reduced unauthenticated limits, while Search requires a key. Exact models, document formats, embedding dimensions, available modalities and regional options are subject to the current endpoint contract.

## Rights and operations

Jina's legal notice refers users to applicable Elastic terms following the acquisition. Check privacy and processing obligations before sending customer documents, personal information or copyrighted content. Avoid placing keys in browser bundles or log records; measure costs and rate limits for the selected provider route. This profile does not represent an executed API request or an independent evaluation of model quality.

## Relations

- Produced by: [Jina AI](../../../../../producers/sub/j/sub/jina-ai/)

## Official resources

- [Jina AI API documentation](https://docs.jina.ai/)
- [Jina AI company and model overview](https://jina.ai/about-us/)
- [Jina legal and terms](https://jina.ai/legal/)
