# Vector Search

Vector search finds items whose embedding vectors are nearest to a query vector according to a similarity or distance metric.

## Core idea

Exact nearest-neighbor search compares a query with every vector and becomes expensive at scale. Approximate nearest-neighbor indexes trade a small amount of recall for much faster search. Common index families organize vectors into graphs, clusters, or compressed partitions.

## Practical considerations

- Choose a metric compatible with how the embedding model was trained.
- Measure recall against an exact-search baseline on representative data.
- Tune candidate count, index parameters, and memory use together.
- Apply metadata and authorization filters before returning content.
- Rebuild or migrate indexes when vector dimensions or models change.

## Trade-offs and limitations

Approximate indexes may miss the true nearest items. High-dimensional vectors consume substantial memory. Similarity search also returns what is mathematically close, which is not always what is useful for the final task.

## Common mistakes

- Using Euclidean distance when the model expects normalized cosine similarity.
- Comparing scores across different indexes as though they were calibrated.
- Choosing index settings from synthetic benchmarks only.
- Forgetting deletion, versioning, or stale-vector cleanup.

## Related concepts

- [Retrieval and Knowledge](../../)
- [Embeddings](../embeddings/)
- [Vector Databases](../vector-databases/)
- [Reranking](../reranking/)
