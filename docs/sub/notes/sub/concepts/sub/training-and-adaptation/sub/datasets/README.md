# Datasets

Legacy residual retained for dataset-lifecycle execution, split/leakage verification, version/provenance operations, deployment-drift monitoring, and retirement guidance that are intentionally outside the canonical Datasets concept owner.

> **Migration note:** Dataset identity, version-sensitive composition, unit-of-observation semantics, source/label/metadata distinctions, coverage/representativeness boundaries, provenance, documentation limits, split roles, quality dimensions, deduplication/leakage, label uncertainty, maintenance/privacy/licensing, and synthetic/evaluation-dataset separation are already preserved in `docs/sub/concepts/sub/machine-learning/sub/data-centric-ml/sub/datasets/`. The remaining material below stays here until its exact learning, dataset-engineering, evaluation, governance, or project-operations owner is verified.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Lifecycle-execution residual

Define the target task, population, environment, time boundary, unit of observation, and acceptance criteria before collecting or generating data. Version source material, transformations, filtering, deduplication, annotations, synthetic additions, schema, and split assignments so a training or evaluation result can be reproduced against the effective dataset state.

Keep data cleaning proportional to the target use. Removing every duplicate, outlier, rare case, or incomplete record can destroy legitimate frequency or long-tail information; document the removal rule and its effect instead of treating cleaning as automatically beneficial.

## Split and leakage residual

Construct train/validation/test or other evaluation partitions according to the dependency structure of the data. Group by user, document/source, entity, session, time, repository, patient/device, or another leakage boundary when random row-level splitting would put correlated evidence on both sides.

Search for more than exact duplicates: shared source documents, derived/paraphrased examples, future information, entity overlap, benchmark exposure, generated variants, and labels computed from protected/future state can all invalidate independence.

## Provenance and governance residual

Preserve source/license/permission/consent information, collection period, annotation origin, transformations, known gaps, sensitive-data handling, and downstream obligations with each dataset version. Public availability is not a substitute for a concrete reuse or privacy decision.

When errors, takedowns, corrected labels, access changes, consent changes, schema changes, or leakage are discovered, create a traceable correction/deprecation path and identify downstream models, indexes, evaluations, or artifacts that require reprocessing or re-evaluation.

## Drift and retirement residual

Monitor whether deployment inputs, label policy, source availability, language/domain mix, or target population diverge from the dataset used to make the original evidence claim. Dataset freshness is a property of the use case, not only a timestamp.

Retire or supersede versions explicitly rather than silently replacing files under the same dataset identity. Keep enough lineage to reproduce old results and enough deprecation state to prevent stale data from being selected accidentally.

These lifecycle, leakage, provenance, governance, drift, and retirement practices remain migration source material until their exact learning, dataset-engineering, evaluation, governance, or project-operations owners are verified.
