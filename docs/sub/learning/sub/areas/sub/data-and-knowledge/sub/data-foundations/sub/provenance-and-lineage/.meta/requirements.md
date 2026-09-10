# Documentation Requirements

## Requirements

- Teach Provenance and Lineage as recording where data came from, how it changed, which version was used, and what downstream artifacts/results depend on it.
- Preserve source/license/permission/consent information, collection period, annotation origin, transformations, filtering, synthetic additions, schema changes, and split assignments when they materially affect reuse or reproducibility.
- When errors, takedowns, corrected labels, access changes, consent changes, schema changes, or leakage are discovered, keep a traceable correction/deprecation path and identify dependent models, indexes, evaluations, or other artifacts that require reassessment.
- Retire or supersede dataset versions explicitly rather than silently replacing state under one identity; preserve enough lineage to reproduce historical evidence while preventing accidental selection of stale versions.

## Validation

- Provenance records support both forward impact analysis and backward reproduction.
- Public availability is not treated as evidence of reuse permission or privacy suitability.
- Historical evidence remains traceable after dataset correction or retirement.
