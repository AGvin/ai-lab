# Documentation Requirements

## Requirements

- Teach Hybrid Retrieval as combining complementary retrieval signals only when the workload benefits from both semantic intent and exact lexical or structured evidence.
- Establish lexical-only and semantic-only baselines before judging the combined route and evaluate representative query classes for both improvements and regressions.
- Tune fusion weights, rank-fusion settings, candidate counts, and reranking stages against the target corpus rather than adopting arbitrary fixed mixes.
- Do not add raw lexical and vector scores directly unless a documented normalization or calibration contract makes them comparable.
- Measure candidate-generation and fusion quality separately from downstream answer quality so retrieval-stage failures remain visible.
- Deduplicate overlapping results using stable source or chunk identity while preserving provenance needed for evaluation, grounding, or citation.
- Apply required metadata and scope filters consistently across every retrieval path so the combined route uses the same intended corpus boundaries.

## Validation

- Hybrid retrieval is not presented as mandatory for every search system.
- Individual retriever baselines remain available for comparison.
- Fusion tuning is evidence-based and raw incompatible scores are not naively combined.
- Required scope filters remain consistent across composed retrievers.
