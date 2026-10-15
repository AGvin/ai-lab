# Documentation Requirements

## Requirements

- Define Visual AI Workflows as engines primarily designed for graphical or node-based composition and execution of AI or generative-media pipelines; distinguish this role from backend application/data orchestration and from inference engines or dashboards that merely expose a workflow view.
- Use the node's category boundary and materialized direct-child set as its navigation scope.
- List every materialized direct child exactly once and keep child-specific identity, facts, references, setup, runtime behavior, and mutable state with the child profile.
- Do not reproduce or depend on legacy `catalog-item`, `catalog-index`, `common/index`, or `catalog/item` schema/template selectors.

## Validation

- Navigation matches the materialized direct children.
- The page remains category-level and does not duplicate concrete child profiles.
- Effective processing does not depend on a legacy `meta.yml` file.
