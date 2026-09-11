# Documentation Requirements

## Requirements

- Present `datasets/` as the factual catalog owner for identifiable concrete AI-relevant datasets and dataset families whose provenance, composition, versions, licenses, access, and intended uses have durable reader value.
- Keep reusable dataset concepts and methodology with concept/learning owners. In particular, do not duplicate the `Evaluation Datasets` concept, benchmark methodology, scoring rules, metrics, evaluation results, or implementation tutorials here.
- Distinguish a concrete dataset from a benchmark that uses it, from an evaluation harness/software implementation, and from a hosted dataset platform.
- Preserve source-backed provenance, construction and curation context, version/variant identity, intended and unsupported uses, licensing/access constraints, known contamination or leakage concerns, and important coverage limitations only to the depth supported by current upstream sources.
- Treat dataset contents, revisions, variants, mirrors, licenses, access paths, and benchmark membership as version-sensitive facts where applicable; do not silently compare materially different revisions as the same dataset.
- Materialize children only for concrete source-backed datasets with durable AI Lab value. Do not create empty training/evaluation/modality taxonomy branches for symmetry.
- Render the standard direct-child navigation from the validated materialized child projection.

## Validation

- Every child represents an identifiable dataset or dataset family rather than a generic dataset concept, benchmark score, leaderboard, software harness, or transient hosted view.
- Dataset and benchmark identities are not collapsed when the benchmark includes additional task, protocol, scoring, or reporting semantics.
- Provenance, version, license/access, and intended-use claims are source-backed and scoped to the applicable release or variant.
- Navigation exposes only materialized children and does not imply that the initial dataset set is exhaustive.
