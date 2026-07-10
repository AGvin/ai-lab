# Vector Databases

A vector database stores embeddings and associated metadata, builds similarity indexes, and exposes operations for inserting, updating, filtering, and retrieving vectors.

## Core idea

The database is infrastructure around vector search. Useful capabilities include approximate nearest-neighbor indexing, metadata filters, namespaces or tenants, persistence, replication, deletion, and integration with document ingestion pipelines.

## Selection criteria

- Supported vector dimensions and distance metrics.
- Filtering behavior and access-control integration.
- Index build and update characteristics.
- Memory, storage, and operational requirements.
- Backup, replication, and disaster recovery.
- Hybrid lexical and vector retrieval support.

## Trade-offs and limitations

A dedicated vector database may simplify scale and operations but adds another system to maintain. General databases with vector extensions can be sufficient when data volume, latency, and update rates are moderate. The database cannot compensate for poor embeddings, chunking, or evaluation.

## Common mistakes

- Choosing a database before measuring workload requirements.
- Storing vectors without source IDs, versions, or deletion paths.
- Treating tenant metadata as a substitute for enforced authorization.
- Assuming faster nearest-neighbor search guarantees better RAG answers.

## Related concepts

- [Retrieval and Knowledge](../../)
- [Vector Search](../vector-search/)
- [Metadata Filtering](../metadata-filtering/)
- [Embeddings](../embeddings/)
