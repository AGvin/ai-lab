# Documentation Requirements

## Requirements

- Teach BM25 as a strong inexpensive lexical baseline whose practical value depends on the corpus, analyzer, field design, and workload rather than default parameters alone.
- Verify tokenization, stemming/normalization, stop-word behavior, field boundaries, and exact-field handling before tuning `k1` or `b`; broken analysis can dominate small ranking-parameter changes.
- Use field-aware weighting when titles, body text, identifiers, or other fields carry different retrieval meaning.
- Tune parameters only against representative retrieval evidence rather than folklore or one fixed default.
- Evaluate exact strings, rare/common terms, long/short documents, and cases where rare lexical evidence is present but not relevant; compare against appropriate lexical, semantic, and hybrid alternatives under the same acceptance criteria.
- Use BM25 as one candidate source in hybrid retrieval when it improves exact lexical coverage.
- Do not compare raw BM25 scores across unrelated queries or indexes as calibrated confidence values.

## Validation

- BM25 is treated as a workload baseline, not a universal winner.
- Analyzer/field correctness is checked before parameter micro-tuning.
- Raw scores are not interpreted as cross-query confidence.
