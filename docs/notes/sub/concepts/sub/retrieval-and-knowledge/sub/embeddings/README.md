# Embeddings

<!--
ai_content:
  managed: true
  l10n: true
-->

Embeddings are numerical vectors that represent the semantic or structural properties of text, images, audio, users, products, or other objects.

## Core idea

An embedding model maps an input into a fixed-length vector. Items with similar meaning or usage are usually placed closer together according to a distance measure such as cosine similarity or dot product. The vector itself is not a human-readable explanation; it is a learned representation optimized for particular tasks and training data.

## Practical use

- Semantic document and code search.
- Retrieval-Augmented Generation.
- Clustering and duplicate detection.
- Recommendation and similarity matching.
- Classification using nearest examples or lightweight models.

## Design considerations

Use the same embedding model and preprocessing for indexed documents and incoming queries. Record the model version and vector dimension. Evaluate retrieval on domain-specific queries, because a generally strong embedding model may perform poorly on product codes, legal terminology, or source code.

## Trade-offs and limitations

Embeddings compress information and can lose exact wording, dates, identifiers, or negation. Changing the embedding model normally requires re-embedding the index. Similarity scores are not calibrated probabilities and should not be interpreted as confidence without evaluation.

## Common mistakes

- Mixing vectors from incompatible embedding models.
- Using semantic retrieval for exact IDs without lexical search.
- Assuming a high similarity score proves factual relevance.
- Ignoring language, domain, and chunk-size effects.

## Related concepts

- [Retrieval and Knowledge](../../)
- [Vector Search](../vector-search/)
- [Semantic Search](../semantic-search/)
- [RAG](../rag/)
