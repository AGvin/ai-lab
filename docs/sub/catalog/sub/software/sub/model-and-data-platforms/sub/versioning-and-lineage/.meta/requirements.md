# Documentation Requirements

## Requirements

- Define Versioning and Lineage as tools primarily tracking reproducible relationships among source revisions, datasets, large artifacts, pipeline dependencies, experiments, and their outputs over time; distinguish this asset/provenance version-control role from hosted artifact-hub clients and broader end-to-end ML lifecycle platforms.
- Use the node's category boundary and materialized direct-child set as its navigation scope.
- List every materialized direct child exactly once and keep child-specific identity, facts, references, setup, runtime behavior, and mutable state with the child profile.
- Do not reproduce or depend on legacy `catalog-item`, `catalog-index`, `common/index`, or `catalog/item` schema/template selectors.

## Validation

- Navigation matches the materialized direct children.
- The page remains category-level and does not duplicate concrete child profiles.
- Effective processing does not depend on a legacy `meta.yml` file.
