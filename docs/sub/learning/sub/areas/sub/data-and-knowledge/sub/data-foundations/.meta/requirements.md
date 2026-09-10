# Documentation Requirements

## Requirements

- Teach Data Foundations as the reusable basis for understanding data identity, structure, distributions, provenance, and lineage across training, evaluation, retrieval, and knowledge systems.
- Materialize only selected children with real source-backed content; the current package materializes `provenance-and-lineage/`.
- Treat dataset versions as explicit states produced by source material plus transformations, filtering, annotation, schema, and split assignments rather than as interchangeable file names.
- Preserve source identity, transformation history, collection period, version/time, and downstream dependency information needed to reproduce or reassess a result.
- Keep concrete licensing, permissions, consent, and sensitive-data obligations with dataset/governance evidence owners while teaching why those fields belong in lineage.

## Validation

- Data lineage remains distinct from model/checkpoint provenance while linking to it where training artifacts depend on data versions.
- Silent replacement of dataset state under one identity is not presented as acceptable lifecycle practice.
