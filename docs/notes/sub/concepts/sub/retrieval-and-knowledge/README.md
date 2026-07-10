# Retrieval and Knowledge

<!--
ai_content:
  managed: true
  l10n: true
-->

Concepts for connecting models to external information, searchable documents, and evidence-backed context.

Concepts are grouped by practical priority. Priority affects reading order, not thematic placement.

## Translations

- English — current
- [Українська](./l10n/uk_UA/)

## Essential

- [`rag/`](./sub/rag/) — Retrieval-Augmented Generation combines external retrieval with model generation.
- [`embeddings/`](./sub/embeddings/) — Numerical representations that place semantically related items near each other in vector space.
- [`chunking/`](./sub/chunking/) — Dividing source material into retrievable units while preserving enough context for use.
- [`semantic-search/`](./sub/semantic-search/) — Retrieval based on meaning rather than only exact word matches.
- [`hybrid-search/`](./sub/hybrid-search/) — Retrieval that combines semantic and lexical search signals.
- [`grounding/`](./sub/grounding/) — Constraining generated claims to supplied evidence, tools, or authoritative sources.

## Useful

- [`vector-search/`](./sub/vector-search/) — Nearest-neighbor retrieval over embedding vectors.
- [`vector-databases/`](./sub/vector-databases/) — Storage and indexing systems optimized for vectors and similarity search.
- [`keyword-search/`](./sub/keyword-search/) — Lexical retrieval based on terms that appear in the source text.
- [`reranking/`](./sub/reranking/) — A second-stage relevance model that reorders retrieved candidates.
- [`citations/`](./sub/citations/) — Links or references that connect generated statements to supporting sources.
- [`metadata-filtering/`](./sub/metadata-filtering/) — Restricting retrieval by attributes such as source, date, version, tenant, or access policy.

## Specialized

- [`bm25/`](./sub/bm25/) — A probabilistic lexical ranking method widely used in document retrieval.
- [`graph-rag/`](./sub/graph-rag/) — Retrieval-Augmented Generation that uses graph structures and relationships to assemble context.
- [`knowledge-graphs/`](./sub/knowledge-graphs/) — Structured representations of entities and their relationships.
