# Documentation Requirements

## Requirements

- Define Lifecycle Platforms as systems whose primary role is coordinating and tracking development of ML or AI projects across experiments, models, pipelines, artifacts, registries, environments, and promotion/deployment stages; distinguish end-to-end project lifecycle management from a standalone hub client, dataset versioning tool, or inference-only runtime.
- Use the node's category boundary and materialized direct-child set as its navigation scope.
- List every materialized direct child exactly once and keep child-specific identity, facts, references, setup, runtime behavior, and mutable state with the child profile.
- Do not reproduce or depend on legacy `catalog-item`, `catalog-index`, `common/index`, or `catalog/item` schema/template selectors.

## Validation

- Navigation matches the materialized direct children.
- The page remains category-level and does not duplicate concrete child profiles.
- Effective processing does not depend on a legacy `meta.yml` file.
