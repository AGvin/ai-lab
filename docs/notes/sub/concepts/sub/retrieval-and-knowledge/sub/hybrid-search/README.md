# Hybrid Search

Hybrid search combines semantic vector retrieval with lexical retrieval so results benefit from both meaning and exact-term matching.

## Core idea

The two retrievers produce candidate lists or scores that must be merged. Common methods include weighted score fusion, reciprocal rank fusion, or retrieving separate candidate sets and passing them to a reranker. The best method depends on whether exact identifiers, natural-language meaning, or both are important.

## Practical use

- Enterprise document search with technical terms.
- Code and log retrieval.
- Product catalogs containing descriptions and SKUs.
- RAG systems that must handle both questions and exact references.

## Trade-offs and limitations

Hybrid retrieval adds indexing, tuning, and evaluation complexity. Raw vector and lexical scores are usually on different scales and should not be added without normalization or a rank-based fusion method. Poor fusion can reduce the strengths of both systems.

## Good practice

Evaluate lexical-only, semantic-only, and hybrid baselines separately. Inspect which query types improve or regress. Apply metadata and permission filters consistently to both retrieval paths.

## Common mistakes

- Using an arbitrary 50/50 score weight without testing.
- Returning duplicate chunks from both retrievers.
- Evaluating only final answer quality and hiding retrieval failures.
- Applying different access-control rules to each index.

## Related concepts

- [Retrieval and Knowledge](../../)
- [Semantic Search](../semantic-search/)
- [Keyword Search](../keyword-search/)
- [Reranking](../reranking/)
