# Cloudflare AI Search

Cloudflare AI Search (formerly AutoRAG) is a managed content-ingestion, indexing, search, and retrieval-augmented generation (RAG) service. It indexes connected websites, R2 objects, or uploaded documents for natural-language and hybrid search, with optional answer generation. Cloudflare announced general availability on **October 1, 2026**.

## Service boundary

AI Search manages content parsing, chunking, embeddings, vector and keyword indexing, retrieval, metadata filtering, and optional response generation as one hosted service. It uses Cloudflare Vectorize for vector-index infrastructure, but is not a replacement name for the [Vectorize service](../cloudflare-vectorize/). Workers AI models, AI Gateway routing, and source storage remain related but distinct product boundaries. A specific embedding, reranking, or generation model is not itself a new AI Search service identity.

Search and answer quality depend on the indexed corpus, freshness, retrieval mode, selected models, filtering, and evaluation protocol. The availability of managed RAG does not establish a universal quality or security guarantee.

## Operations and dated changes

The **November 2, 2026** Cloudflare changelog postponed AI Search usage billing from November 1 to **December 1, 2026**, without changing the published rates or included usage. It also changed the default recurring source-sync interval from six to **24 hours**; supported configurable intervals span 15 minutes to 24 hours. Check the live settings and pricing before planning operating costs or refresh latency. [Billing and sync changelog](https://developers.cloudflare.com/changelog/post/2026-11-02-billing-postponed-default-sync-interval/).

At general availability, Cloudflare described managed Workers AI embeddings and reranking as included in AI Search pricing, while generation, query rewriting, and external model providers retain distinct account/gateway billing boundaries. Verify current quotas, file/OCR limits, model availability, regions, indexing behavior, source access, retention, and authentication before using private or regulated content. [GA announcement](https://developers.cloudflare.com/changelog/post/2026-10-01-ai-search-generally-available/) · [Limits and pricing](https://developers.cloudflare.com/ai-search/platform/limits/).

## Relations

- Produced by [Cloudflare](../../../../../../../producers/sub/c/sub/cloudflare/).

## Official resources

- [AI Search documentation](https://developers.cloudflare.com/ai-search/)
- [Indexing and querying architecture](https://developers.cloudflare.com/ai-search/concepts/how-ai-search-works/)
- [General availability — October 1, 2026](https://developers.cloudflare.com/changelog/post/2026-10-01-ai-search-generally-available/)
- [Billing and sync correction — November 2, 2026](https://developers.cloudflare.com/changelog/post/2026-11-02-billing-postponed-default-sync-interval/)
