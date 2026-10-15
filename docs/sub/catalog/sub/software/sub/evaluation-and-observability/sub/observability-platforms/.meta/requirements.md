# Documentation Requirements

## Requirements

- Define Observability Platforms by their primary role in collecting, correlating, visualizing, and investigating runtime traces, logs, usage, latency, costs, failures, and production behavior of AI applications and agents; treat embedded evaluations as a platform capability rather than automatically reclassifying these products as standalone evaluation frameworks.
- Use the node's category boundary and materialized direct-child set as its navigation scope.
- List every materialized direct child exactly once and keep child-specific identity, facts, references, setup, runtime behavior, and mutable state with the child profile.
- Do not reproduce or depend on legacy `catalog-item`, `catalog-index`, `common/index`, or `catalog/item` schema/template selectors.

## Validation

- Navigation matches the materialized direct children.
- The page remains category-level and does not duplicate concrete child profiles.
- Effective processing does not depend on a legacy `meta.yml` file.
