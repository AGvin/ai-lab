# Hybrid Search

Legacy residual retained for application patterns, fusion tuning, comparative evaluation, deduplication, and permission-consistency guidance that are intentionally outside the canonical Hybrid Retrieval concept owner.

> **Migration note:** Hybrid-retrieval identity, multi-retriever composition, candidate-generation versus fusion versus reranking boundaries, raw-score comparability limits, rank-based fusion semantics, implementation-dependent tuning parameters, and non-guarantees of universal improvement are already preserved in `docs/sub/concepts/sub/information-retrieval/sub/hybrid-retrieval/`. The remaining material below stays here until its exact learning, retrieval-engineering, evaluation, security, or decision-support owner is verified.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Application-pattern residual

Hybrid retrieval is often useful when one workload mixes natural-language intent with exact identifiers, technical terms, code/log strings, product codes, named entities, or other evidence that benefits from complementary retrieval signals. Representative examples include enterprise document search, code and log retrieval, product catalogs, and RAG systems that must answer both semantic questions and exact-reference queries.

Treat these as application patterns to evaluate rather than a rule that every search system should combine lexical and semantic retrieval.

## Fusion and evaluation residual

Useful implementation and evaluation practices include:

- establish lexical-only and semantic-only baselines before judging the combined route;
- compare hybrid behavior on representative query classes and inspect both improvements and regressions rather than relying only on an aggregate score;
- tune fusion weights, rank-fusion settings, candidate counts, and reranking stages against the target corpus instead of adopting an arbitrary fixed split such as 50/50;
- do not add raw lexical and vector scores directly unless their normalization/calibration contract makes that comparison meaningful;
- measure retrieval-stage quality separately from final answer quality so candidate-generation or fusion failures remain visible.

## Deduplication and permission residual

When multiple retrievers can surface the same source unit, deduplicate results using stable source/chunk identity while preserving provenance needed for evaluation and downstream citation or grounding.

Apply metadata, tenant, and permission constraints consistently across every retrieval path. A hybrid route must not broaden access merely because one retriever or index applies a different filtering policy.

These application, fusion, evaluation, deduplication, and permission-consistency practices remain migration source material until their exact learning, retrieval-engineering, evaluation, security, or decision-support owners are verified.
