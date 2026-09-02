# Keyword Search

Legacy residual retained for analyzer/index design, exact-field handling, query-feature, and retrieval-evaluation guidance that are intentionally outside the canonical Lexical Retrieval concept owner.

> **Migration note:** Lexical-retrieval identity, lexical evidence and ranked retrieval boundaries, analyzer/inverted-index foundations, exact-term strengths, normalization/stemming risks, BM25 ownership, semantic-retrieval distinction, and metadata-filtering separation are already preserved in `docs/sub/concepts/sub/information-retrieval/sub/lexical-retrieval/`. The remaining material below stays here until its exact learning, retrieval-engineering, evaluation, or decision-support owner is verified.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Analyzer and index-design residual

Configure lexical analysis according to the corpus rather than applying one normalization pipeline to every field. Preserve exact or non-analyzed representations for identifiers, API names, product codes, version strings, legal citations, names, or other values where stemming or token normalization could destroy the evidence the user intends to match.

Use field-aware indexing when document fields carry different retrieval meaning, and preserve positional information or phrase-query capability where word order materially changes the requested match.

## Query-feature residual

Useful application features can include required or excluded terms, exact phrases, field-scoped clauses, and carefully managed synonym or spelling-variation expansion. Treat such features as corpus- and search-engine-specific behavior to evaluate rather than universal lexical-search requirements.

Do not interpret raw term frequency as answer relevance, and do not eliminate lexical retrieval merely because a semantic route is also available when exact surface evidence remains important.

## Evaluation residual

Evaluate representative real queries across both precision and recall. Include exact identifiers, rare terminology, phrase/order-sensitive requests, common-term queries, synonyms, spelling variants, and cases where analyzers may over-normalize codes or names.

Inspect retrieval failures separately from downstream answer generation so an application does not hide lexical misses behind a superficially plausible final response.

These analyzer, index, query-feature, and evaluation practices remain migration source material until their exact learning, retrieval-engineering, evaluation, or decision-support owners are verified.
