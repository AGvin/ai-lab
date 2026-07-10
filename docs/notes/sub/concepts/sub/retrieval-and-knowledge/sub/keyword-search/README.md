# Keyword Search

Keyword search retrieves documents using lexical evidence: terms, phrases, field matches, and statistical importance of words in the corpus.

## Core idea

Lexical retrieval is strong when exact wording matters. It can find product codes, API names, error messages, quotations, and domain-specific terminology that semantic models may blur. Search engines commonly apply tokenization, stemming, field weights, and ranking functions such as BM25.

## Practical use

- Exact identifiers and technical strings.
- Legal citations, version numbers, and named entities.
- Search with required or excluded terms.
- Filtering by structured document fields.
- Providing the lexical half of hybrid retrieval.

## Trade-offs and limitations

Keyword search may fail when the query uses different wording from the source. Stemming and analyzers can also damage exact identifiers. A query with common terms may return many superficially matching results.

## Good practice

Use field-aware indexing and preserve non-analyzed fields for exact matches. Support phrase queries where word order matters. Measure both precision and recall with real queries instead of tuning only on a few examples.

## Common mistakes

- Applying aggressive stemming to codes or names.
- Assuming keyword frequency equals answer relevance.
- Ignoring synonyms and spelling variation.
- Replacing lexical retrieval entirely with embeddings.

## Related concepts

- [Retrieval and Knowledge](../../)
- [BM25](../bm25/)
- [Hybrid Search](../hybrid-search/)
- [Metadata Filtering](../metadata-filtering/)
