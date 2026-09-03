# Documentation Requirements

## Requirements

- Teach Semantic Retrieval as meaning/representation-driven retrieval whose usefulness depends on the representation, domain, segmentation, filters, and actual query distribution.
- Cover natural-language, paraphrase-heavy, cross-lingual, and intent-oriented application patterns as hypotheses to evaluate rather than guarantees of superiority over lexical retrieval.
- Preserve lexical/exact-match routes for identifiers, rare names, versions, error codes, legal citations, negation, and other surface-form evidence that representation similarity can blur.
- Combine metadata/structured filtering and reranking where explicit scope or broad candidate sets require them; relevance does not replace eligibility checks.
- Evaluate representative domain queries at multiple candidate counts, measuring answer-bearing candidate recall rather than only top-result topical similarity.
- Diagnose misses from representation choice, segmentation, filters, domain shift, or exact-term requirements and distinguish retrieval failure from downstream answer failure.
- Do not treat nearest neighbors or high similarity values as verified answers.

## Validation

- Semantic retrieval is not presented as universally better than lexical retrieval.
- Similarity is not treated as authorization or factual correctness.
- Candidate-set evaluation checks for useful evidence rather than only topical relatedness.
