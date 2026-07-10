# BM25

BM25 is a probabilistic lexical ranking function used to score how well a document matches query terms.

## Core idea

BM25 rewards documents containing important query terms while controlling for term frequency and document length. A term that appears in few documents receives more weight than a common term. Repeating a term helps only up to a saturation point, which prevents raw frequency from dominating the ranking.

## Practical use

- Search for exact technical terminology.
- Retrieve error messages, identifiers, and named entities.
- Provide a lexical candidate set for hybrid search.
- Establish a strong, inexpensive retrieval baseline.

## Important parameters

- `k1` controls how quickly term-frequency benefit saturates.
- `b` controls document-length normalization.

Defaults are often reasonable, but analyzers, field weights, stop words, and document structure usually matter more than small parameter changes.

## Trade-offs and limitations

BM25 does not understand paraphrases or broader semantic similarity unless query expansion or synonyms are added. It can also overvalue rare terms that are not actually relevant.

## Common mistakes

- Tuning parameters before fixing tokenization and field design.
- Using one combined field for titles, body text, and identifiers.
- Assuming BM25 scores are comparable across different queries.
- Discarding BM25 because embeddings perform better on a small demo set.

## Related concepts

- [Retrieval and Knowledge](../../)
- [Keyword Search](../keyword-search/)
- [Hybrid Search](../hybrid-search/)
- [Semantic Search](../semantic-search/)
