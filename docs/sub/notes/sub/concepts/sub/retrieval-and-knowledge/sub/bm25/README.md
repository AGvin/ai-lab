# BM25

Legacy residual retained for baseline selection, analyzer/field tuning, and retrieval-evaluation guidance that are intentionally outside the canonical BM25 concept owner.

> **Migration note:** BM25 identity, probabilistic lexical-ranking origin, inverse-document-frequency-style weighting, term-frequency saturation, document-length normalization, `k1`/`b` boundaries, score non-comparability, and separation from semantic/hybrid retrieval are already preserved in `docs/sub/concepts/sub/information-retrieval/sub/lexical-retrieval/sub/bm25/`. The remaining material below stays here until its exact learning, retrieval-engineering, evaluation, or decision-support owner is verified.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Baseline and application residual

BM25 is often a useful inexpensive lexical baseline for technical terminology, identifiers, error messages, named entities, and as one candidate source in a hybrid retrieval system. Treat these as workload patterns to evaluate rather than evidence that BM25 is universally the correct first-stage retriever.

## Analyzer and field-tuning residual

Before tuning `k1` or `b`, verify that tokenization, stemming/normalization, stop-word behavior, field boundaries, and exact-field handling fit the corpus. Titles, body text, identifiers, and other fields can carry different retrieval meaning; a single combined field can hide those distinctions.

Parameter tuning should follow representative retrieval evidence rather than default-value folklore. Small parameter changes can matter less than a broken analyzer or field design.

## Evaluation residual

Evaluate BM25 on representative queries and compare it against relevant lexical, semantic, or hybrid alternatives under the same corpus and acceptance criteria. Include exact strings, rare terms, common terms, long/short documents, and cases where rare lexical evidence is present but not actually relevant.

Do not compare raw BM25 scores across unrelated queries or indexes as though they were calibrated confidence values, and do not discard a lexical baseline solely because a small semantic-search demo looked stronger.

These baseline, tuning, and evaluation practices remain migration source material until their exact learning, retrieval-engineering, evaluation, or decision-support owners are verified.
