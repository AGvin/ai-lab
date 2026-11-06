# Documentation Requirements

## Requirements

- Identify Milvus as the open-source distributed vector database/vector-search software developed by Zilliz and donated to the LF AI & Data Foundation.
- Preserve its primary placement under `data-infrastructure/vector-search` rather than classifying it as an application framework, embedding model, or managed cloud service.
- Keep self-managed Milvus distinct from Zilliz Cloud and other managed Milvus offerings; compatibility with the Milvus API does not make a hosted service the same canonical identity.
- Treat current 3.x/2.x release lines, storage architecture, indexing/search capabilities, hybrid/full-text features, consistency modes, scaling/topology, hardware acceleration, SDK compatibility, deployment methods, and support matrices as freshness-sensitive.
- Keep Milvus Lite/standalone/distributed/deployment modes, external collections, SDKs, connectors, and AI-agent integrations as product surfaces or deployment modes unless upstream later establishes an independently durable product identity.
- Attribute performance/scale comparisons to Zilliz/Milvus or the cited evaluator and preserve exact dataset, index, hardware, topology, concurrency, and software configuration.
- Preserve Zilliz producer provenance while keeping LF AI & Data Foundation stewardship/governance distinct from product authorship.

## Validation

- The node remains self-managed vector-search infrastructure rather than Zilliz Cloud.
- Deployment modes and SDKs are not duplicated as peer canonical products by default.
- Mutable scale/performance claims remain configuration-scoped.
- Producer provenance resolves bidirectionally to Zilliz.
