# Documentation Requirements

## Requirements

- Teach Citations and Provenance as preserving source identity and traceable support locations from authoritative retrieval/tool metadata rather than asking a model to reconstruct titles, URLs, page numbers, IDs, or timestamps from memory.
- Preserve stable source/version identity plus the most specific practical support location such as page, section, line range, record/field, timestamp, query result, or tool run.
- When preprocessing, chunking, OCR, moves, or re-indexing change intermediate representations, maintain a resolver/mapping so citations remain attached to the intended source evidence rather than silently drifting.
- Evaluate citation support correctness, material-claim coverage, location specificity, source/version resolvability, and source freshness/authority according to the task.
- Treat automatic citation/entailment evaluators as supporting evidence rather than unquestionable ground truth when risk warrants calibration or human review.
- Choose citation density according to verification risk and reader needs; compound or multi-source claims may require several references.
- Preserve application data-handling boundaries when rendering citations; traceability does not require exposing source details that the current reader should not receive.

## Validation

- Citation metadata comes from traceable source/tool state rather than model memory.
- Preprocessing/re-indexing does not silently invalidate evidence locations.
- Citation correctness and source authority/freshness remain separately checkable.
- Traceability does not broaden the intended visibility of source material.
