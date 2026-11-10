# Documentation Requirements

## Requirements

- Define Inference Engines as locally or server-executable runtime/engine software primarily responsible for loading model artifacts and performing inference, optimization at execution, request batching and direct API serving; distinguish this execution role from cluster-wide distributed orchestration, complete application-facing integrated model platforms, and remote-only model API services.
- Use the node's category boundary and materialized direct-child set as its navigation scope.
- List every materialized direct child exactly once and keep child-specific identity, facts, references, setup, runtime behavior, and mutable state with the child profile.
- Do not reproduce or depend on legacy `catalog-item`, `catalog-index`, `common/index`, or `catalog/item` schema/template selectors.

## Validation

- Navigation matches the materialized direct children.
- The page remains category-level and does not duplicate concrete child profiles.
- Effective processing does not depend on a legacy `meta.yml` file.
