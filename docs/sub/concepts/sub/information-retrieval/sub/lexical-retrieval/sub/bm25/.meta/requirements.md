# Documentation Requirements

## Requirements

- Use the reader-facing title `BM25 (Okapi BM25)`.
- Define BM25 as a lexical document-ranking function derived from the probabilistic relevance framework that combines query-term evidence with inverse-document-frequency-style term importance, saturating term-frequency contribution, and document-length normalization.
- Explain term-frequency saturation: additional occurrences of a query term can increase its contribution, but the marginal gain decreases instead of growing linearly without bound.
- Explain document-length normalization as compensating for the greater opportunity longer documents have to contain query terms; describe `b` as the standard control over normalization strength without presenting one value as universally optimal.
- Explain `k1` as the standard control over term-frequency saturation/scaling in common BM25 formulations, while acknowledging that exact formulas, IDF definitions, defaults, and variants differ across publications and implementations.
- Make clear that BM25 is a ranking score, not a calibrated probability of relevance, factual correctness, or answer quality, and that raw BM25 scores are generally not meaningful as universal cross-query or cross-index thresholds without an explicitly validated implementation/context.
- Distinguish BM25 from Boolean/exact matching, TF-IDF/vector-space formulations, semantic embedding similarity, and hybrid retrieval. They may coexist in one retrieval system but are different retrieval/scoring mechanisms.
- Distinguish core BM25 from extensions such as BM25F or implementation-specific field weighting. Multi-field scoring and analyzer/index configuration can materially affect results but are not universal parts of the base concept.
- Explain that preprocessing/analyzers determine which lexical terms reach BM25 scoring; tokenization, stemming, stop-word handling, field boundaries, and corpus statistics can therefore matter as much as or more than small parameter changes.
- Keep concrete search-engine defaults, exact implementation formulas, field boosts, corpus tuning, benchmark results, hybrid fusion settings, and application-specific thresholds with their applicable engineering, catalog, evidence, or decision owners.
- Use the canonical entity references as research inputs for the probabilistic framework and BM25 parameter/variant boundaries when reader-facing rendering is activated.

## Validation

- The page does not describe BM25 as semantic/vector retrieval or as a calibrated relevance probability.
- Term-frequency saturation and document-length normalization are both represented in the conceptual explanation.
- `k1`, `b`, IDF, and score semantics are not tied to one implementation's exact defaults/formula as universal standards.
- BM25F and field-specific extensions are distinguished from the base BM25 concept.
- Raw BM25 scores are not presented as universally comparable across unrelated queries, indexes, or implementations.
- Legacy tuning advice is preserved only as contextual design guidance rather than universal parameter recommendations.
