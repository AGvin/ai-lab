# Chunking

Legacy residual retained for corpus-specific segmentation, retrieval evaluation, source-metadata preservation, and ingestion-tuning guidance that are intentionally outside the canonical Indexing and Chunking concept owner.

> **Migration note:** Retrieval-unit and chunking identity, fixed-window/overlap/structure-aware/semantic/parent-child/dynamic strategy boundaries, localization-versus-context trade-offs, source-versus-derived-unit provenance, indexing scope, and separation from context-window capacity are already preserved in `docs/sub/concepts/sub/information-retrieval/sub/indexing-and-chunking/`. The remaining material below stays here until its exact learning, retrieval-engineering, evaluation, or decision-support owner is verified.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Corpus-specific segmentation residual

Choose retrieval units according to the source structure and downstream task rather than one repository-wide character or token size. Useful boundaries can follow headings, paragraphs, functions/classes, table regions, conversation turns, or other corpus-specific units when those structures preserve the information readers or retrievers need.

When fixed windows are appropriate, treat size and overlap as tunable application parameters. Use token-aware sizing when a concrete downstream model or provider budget makes it relevant, but do not derive an optimal retrieval unit directly from advertised context capacity.

## Provenance and ingestion residual

Preserve enough source metadata to reconnect every derived unit to the canonical source, including useful hierarchy, location/page/section, version, and document identity where applicable. Avoid treating overlapping copies as independent source truth.

When source material changes, the ingestion/indexing path should update or remove derived units consistently enough that retrieval does not silently mix obsolete and current versions.

## Evaluation and tuning residual

Evaluate segmentation with representative queries and failure cases, including questions whose evidence crosses a candidate boundary. Measure whether retrieved units contain sufficient answer-bearing context rather than checking only keyword presence or nearest-neighbor similarity.

Watch for duplicated evidence from excessive overlap, fragmented tables/code/definitions, loss of headings or hierarchy, and one-size-fits-all segmentation across incompatible content types. Tune these choices together with the retriever and downstream use rather than in isolation.

These segmentation, ingestion, provenance, and evaluation practices remain migration source material until their exact learning, retrieval-engineering, evaluation, or decision-support owners are verified.
