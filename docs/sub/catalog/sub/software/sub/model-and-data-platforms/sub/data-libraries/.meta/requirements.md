# Documentation Requirements

## Requirements

- Define Data Libraries as local programming libraries whose primary role is loading, representing, querying, transforming, splitting, streaming, and exporting datasets for ML/AI development; distinguish reusable in-process data APIs from dataset annotation platforms, hosted data hubs, and end-to-end training frameworks.
- Use the node's category boundary and materialized direct-child set as its navigation scope.
- List every materialized direct child exactly once and keep child-specific identity, facts, references, setup, runtime behavior, and mutable state with the child profile.
- Do not reproduce or depend on legacy `catalog-item`, `catalog-index`, `common/index`, or `catalog/item` schema/template selectors.

## Validation

- Navigation matches the materialized direct children.
- The page remains category-level and does not duplicate concrete child profiles.
- Effective processing does not depend on a legacy `meta.yml` file.
