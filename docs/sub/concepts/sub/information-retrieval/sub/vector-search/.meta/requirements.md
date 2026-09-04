# Documentation Requirements

## Requirements

- Use the reader-facing title `Vector Search`.
- Define vector search as retrieving or ranking items by comparing vector representations with a query vector using a defined similarity, distance, or inner-product relation and a search procedure over the vector collection.
- Distinguish vector search from semantic retrieval. Vector search is a mathematical/indexing mechanism; whether vector proximity represents semantic language similarity, image similarity, recommendation preference, or another relationship depends on how the vectors were produced and trained.
- Explain exact nearest-neighbor search versus approximate nearest-neighbor (ANN) search. Exact search evaluates the defined nearest-neighbor objective without approximation, while ANN methods trade some exact-neighbor recall or guarantees for improved speed, memory, or scale.
- Present graph, inverted/clustered, quantized/compressed, and exhaustive methods as important families without making one index family or implementation universal.
- Explain that the similarity/distance metric must match the representation contract. Cosine similarity, dot product, and Euclidean distance are not interchangeable by default, although normalization can make some rankings mathematically related in specific cases.
- Make clear that vector-search scores/distances are representation- and index-specific signals rather than calibrated relevance probabilities and generally should not be compared across unrelated representation models, metrics, or indexes without validation.
- Distinguish vector search from the canonical `ai-engineering/system-design/vector-databases/` concept. Vector search owns the retrieval/query mechanism over vector representations; a vector database owns persistent data management, indexing, query execution, updates, metadata, recovery, concurrency, and other DBMS responsibilities that may expose vector search as one capability.
- Distinguish vector search from the canonical `machine-learning/representation-learning/embeddings/` concept. Embeddings are reusable learned representations that can support retrieval and many other downstream tasks; vector search consumes compatible vector representations but does not own how embeddings are learned or imply that every embedding use case is a search problem.
- Keep concrete index parameters, hardware placement, vector dimensions, model migrations, benchmark measurements, filtering implementations, product features, and application-specific thresholds with their applicable engineering, catalog, evidence, or decision owners.
- Use the canonical entity references as research inputs for exact/approximate similarity-search and indexing trade-off boundaries when reader-facing rendering is activated.

## Validation

- Vector search is not equated with semantic search, embeddings, or vector-database products.
- Exact and approximate nearest-neighbor search are distinguished without implying one ANN recall/speed trade-off is universal.
- Similarity metrics are not treated as interchangeable without representation-specific assumptions.
- Raw similarity/distance scores are not presented as calibrated or universally comparable relevance values.
- The canonical Embeddings and Vector Databases concepts remain separate owners and are not collapsed into vector search.
- Legacy operational tuning guidance is not copied into the canonical concept as universal configuration.
