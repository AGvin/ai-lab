# Documentation Requirements

## Requirements

- Teach Indexing and Chunking as designing retrieval units and derived index state around source structure, downstream task, and retrieval evidence rather than one repository-wide character/token size.
- Consider headings, paragraphs, functions/classes, table regions, conversation turns, or other corpus-specific boundaries when they preserve useful information structure.
- Treat fixed-window size and overlap as tunable application parameters; use token-aware sizing when a concrete downstream budget requires it, but do not derive an optimal chunk size directly from advertised model context capacity.
- Preserve stable document/source identity plus useful hierarchy, page/section/location, version, and other provenance needed to reconnect each derived unit to its canonical source.
- Update or remove derived units consistently when source material changes so indexes do not silently mix obsolete and current versions; overlapping chunks remain derived views, not independent source truth.
- Evaluate segmentation with representative queries and boundary-crossing failure cases, measuring answer-bearing context rather than only keyword presence or vector similarity.
- Inspect duplicated evidence from excessive overlap, fragmented tables/code/definitions, lost headings/hierarchy, and one-size-fits-all segmentation across incompatible content types.
- Tune segmentation together with the retriever and downstream use rather than optimizing chunking in isolation.

## Validation

- One global chunk size is not presented as universally optimal.
- Derived chunks remain traceable to canonical source identity/version.
- Source updates have a defined derived-state refresh/removal path.
- Segmentation evaluation includes evidence that crosses candidate boundaries.
