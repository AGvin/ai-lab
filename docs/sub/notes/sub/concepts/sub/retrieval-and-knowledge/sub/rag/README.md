# RAG (Retrieval-Augmented Generation)

Legacy residual retained for implementation workflow, source-code retrieval, staged evaluation, and application-selection guidance that are intentionally outside the canonical Retrieval-Augmented Generation concept owner.

> **Migration note:** RAG identity, retrieval-conditioned generation, non-universal component boundaries, query-time retrieval versus model adaptation, retrieval/generation failure separation, grounding/security/citation non-guarantees, provenance requirements, and the canonical GraphRAG specialization are already preserved in `docs/sub/concepts/sub/ai-engineering/sub/architectures-and-patterns/sub/rag/`. The remaining material below stays here until its exact learning, retrieval-engineering, evaluation, security, or decision-support owner is verified.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Implementation-workflow residual

A practical RAG implementation usually needs separate ingestion/indexing and query-time flows, but the exact components depend on the data and retrieval strategy.

Typical ingestion concerns include parsing/normalization, source identity and versioning, segmentation, metadata/access-policy capture, optional learned representations, index updates, and removal of stale derived state.

Typical query-time concerns include query analysis, one or more retrieval routes, optional filtering/reranking, evidence/context assembly, generation, citation/grounding support, and explicit handling when the available evidence is insufficient.

Do not treat a vector store, embedding model, fixed chunk size, reranker, or one retrieve-once prompt shape as mandatory. Select each component because representative workload evidence shows it is useful.

## Source-code retrieval residual

Repository/code RAG often benefits from signals that generic prose retrieval does not preserve well, including file paths, symbols/signatures, classes/functions, imports/exports, exact strings, dependency relationships, language structure, and version/Git metadata.

Route exact symbol, configuration-key, error-string, or identifier questions through lexical/symbol-aware retrieval when that evidence is stronger than semantic similarity. Use semantic or hybrid retrieval where conceptual matching adds value instead of forcing one retriever over every query class.

## Staged-evaluation residual

Evaluate the pipeline at multiple layers so end-to-end answer quality does not hide retrieval defects.

Retrieval-oriented checks can include whether required evidence enters the candidate/final context set, recall/precision/ranking quality, reranker effects, filter/access behavior, freshness, and retrieval latency. Generation-oriented checks can include factual correctness, support/faithfulness to supplied evidence, citation quality, completeness, appropriate abstention, latency, and cost.

Preserve representative failure cases such as missing/unindexed evidence, broken segmentation, stale or contradictory sources, retrieval misses, prompt-injection content, ignored evidence, unsupported synthesis, and authorization mistakes. A stronger generator should not be used to mask a weak evidence pipeline.

## Application-selection residual

RAG is often useful for private, current, domain-specific, or frequently changing information, but compare it with simpler direct-context, structured-query/API, lexical search, fine-tuning, or deterministic application designs according to the actual requirement. Fine-tuning can adapt behavior without becoming a reliable searchable factual store, while small bounded source sets may not justify a full retrieval subsystem.

These implementation, source-code retrieval, evaluation, and application-selection practices remain migration source material until their exact learning, retrieval-engineering, evaluation, security, or decision-support owners are verified.
