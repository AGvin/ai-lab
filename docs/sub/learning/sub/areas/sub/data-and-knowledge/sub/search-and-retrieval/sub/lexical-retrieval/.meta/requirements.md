# Documentation Requirements

## Requirements

- Teach Lexical Retrieval as corpus-aware term/token matching and ranking where analyzers, fields, exact representations, phrases, and query operators materially affect results.
- Preserve exact or non-analyzed fields for identifiers, API names, product codes, versions, legal citations, names, and other evidence that stemming or normalization could damage.
- Use field-aware indexing when titles, body text, identifiers, or other fields carry different retrieval meaning; retain positional/phrase capability when order matters.
- Treat required/excluded terms, exact phrases, field clauses, synonyms, and spelling expansion as backend/corpus-specific tools to evaluate rather than universal requirements.
- Evaluate precision and recall on representative queries including rare/exact strings, common terms, phrase/order-sensitive cases, synonyms, spelling variants, and analyzer failure cases.
- Preserve lexical retrieval as a complementary route when semantic retrieval is also available and exact surface evidence remains important.
- Materialize and link `bm25/` as the selected lexical-ranking method with source-backed practical material.

## Validation

- One analyzer pipeline is not assumed appropriate for every field or corpus.
- Raw term frequency is not treated as answer relevance.
- Exact evidence is not lost merely to normalize text for ranking.
