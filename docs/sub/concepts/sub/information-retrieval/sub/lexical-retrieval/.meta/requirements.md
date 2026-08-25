# Documentation Requirements

## Requirements

- Use the reader-facing title `Lexical Retrieval` and introduce `keyword search` as a common practical label rather than a separate canonical concept leaf.
- Define lexical retrieval as retrieving or ranking information through evidence derived from the lexical form of query and indexed content, such as terms, tokens, phrases, fields, positions, and corpus/document statistics.
- Explain that lexical matching can range from exact/Boolean term conditions to weighted ranked retrieval; do not reduce the category to literal substring matching or to one ranking function.
- Explain the role of an analyzer/tokenization pipeline and inverted index as common implementation foundations while keeping tokenizer choice, stemming/lemmatization, stop-word handling, phrase/position indexing, and field configuration as system-specific design decisions.
- Distinguish lexical retrieval from semantic/vector retrieval. Lexical methods can strongly preserve exact identifiers, terminology, phrases, and rare terms, but they do not require learned embeddings or vector-neighbor similarity.
- Make clear that lexical normalization can intentionally broaden matching and can also damage exact identifiers or distinctions; `lexical` therefore does not mean every query must match raw text byte-for-byte.
- Present BM25 as an important selected lexical ranking method while keeping its detailed scoring semantics in the `bm25/` child node.
- Distinguish metadata/attribute filtering from lexical relevance scoring even when both participate in one search request.
- Keep concrete analyzer configurations, index schemas, search-engine syntax, field boosts, synonym dictionaries, benchmark tuning, and hybrid-routing decisions with their applicable engineering, catalog, evidence, or decision owners.
- Use the canonical entity references as research inputs for lexical indexing and ranking terminology when reader-facing rendering is activated.

## Validation

- The page does not create a separate canonical `keyword-search` child or treat keyword search as only raw substring matching.
- Lexical retrieval is distinguished from semantic/vector similarity and from metadata filtering.
- No stemming, tokenizer, analyzer, field layout, or ranking method is presented as universally required.
- Exact lexical evidence is not presented as automatic proof of relevance.
- BM25 is introduced without duplicating its complete child definition.
- Legacy implementation advice is preserved only as scoped design boundaries rather than universal configuration guidance.
