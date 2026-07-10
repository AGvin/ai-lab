# Semantic Search

<!--
ai_content:
  managed: true
  l10n: true
-->

Semantic search retrieves content by comparing learned representations of meaning rather than relying only on exact word matches.

## Core idea

A query and candidate documents are embedded into vectors, then a vector index finds nearby items. This allows retrieval when the user and source use different wording, abbreviations, or paraphrases.

## Practical strengths

- Natural-language questions over documents.
- Cross-lingual or paraphrase-heavy retrieval.
- Finding conceptually related code, tickets, or notes.
- Matching user intent to products or support articles.

## Trade-offs and limitations

Semantic search may miss exact identifiers, rare names, version numbers, or negated phrases. It can also retrieve topically similar passages that do not contain the required answer. Results depend heavily on the embedding model, chunking, and domain.

## Good practice

Combine semantic search with metadata filters and, when exact terms matter, lexical search. Evaluate recall at several candidate counts rather than inspecting only the top result. Use reranking when initial vector similarity is too coarse.

## Common mistakes

- Treating nearest neighbors as verified answers.
- Using semantic search alone for SKUs, error codes, or legal citations.
- Comparing similarity scores across unrelated models or indexes.
- Ignoring access controls during retrieval.

## Related concepts

- [Retrieval and Knowledge](../../)
- [Embeddings](../embeddings/)
- [Hybrid Search](../hybrid-search/)
- [Vector Search](../vector-search/)
