# Documentation Requirements

## Requirements

- Define Dataset Curation as platforms and tools whose primary role is assembling, labeling/annotating, cleaning, reviewing, quality-controlling, sampling, or improving training and evaluation datasets, including human-in-the-loop data operations; distinguish curation workflows from dataset-loading libraries, generic model training runtimes, and hosted raw-data storage.
- Use the node's category boundary and materialized direct-child set as its navigation scope.
- List every materialized direct child exactly once and keep child-specific identity, facts, references, setup, runtime behavior, and mutable state with the child profile.
- Do not reproduce or depend on legacy `catalog-item`, `catalog-index`, `common/index`, or `catalog/item` schema/template selectors.

## Validation

- Navigation matches the materialized direct children.
- The page remains category-level and does not duplicate concrete child profiles.
- Effective processing does not depend on a legacy `meta.yml` file.
