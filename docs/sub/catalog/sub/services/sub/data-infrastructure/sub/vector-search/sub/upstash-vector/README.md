# Upstash Vector

**Upstash Vector** is a managed, serverless vector database for storing numerical embeddings and performing similarity search in RAG, recommendations and related retrieval applications. It is not a downloadable vector-index engine or the embedding model that generated the vectors.

## Storage and retrieval

The [official service overview](https://upstash.com/docs/vector/overall/whatisvector) describes REST access, SDKs, similarity metrics, vector metadata and metadata filtering. Applications manage a remote index and issue insertion or search requests using the appropriate index endpoint and credential. Index dimensions, similarity metric, namespace separation and filtered query behavior must match the selected index configuration.

Although the service can integrate with embedding workflows, externally generated embeddings and model-provider contracts remain separate concerns. Model version changes can require re-embedding or partitioning existing indices.

## Operating boundaries

Avoid exposing index credentials in frontend code, tenant query logs or stored content. Review namespace isolation, delete/retention behavior, remote data residency, quotas, rate limiting and failure recovery; plan for access control and provider outages. Storage/traffic/request prices and tier-specific features change: use the [current pricing page](https://upstash.com/pricing/vector) and [service FAQ](https://upstash.com/docs/vector/help/faq) for a concrete deployment decision.

This profile is documentation only. No hosted index, query, embedding generation, backup restoration, compliance audit or whole-catalog clean pass was tested.

## Official sources

- [Vector service overview](https://upstash.com/docs/vector/overall/whatisvector)
- [Vector FAQ](https://upstash.com/docs/vector/help/faq)
- [Current Vector pricing](https://upstash.com/pricing/vector)
