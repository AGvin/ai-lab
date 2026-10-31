# Documentation Requirements

## Requirements

- Define Evaluation Frameworks by their primary role in repeatable offline or controlled model, agent, and application assessment using tasks, datasets, test cases, scorers, and comparable metrics; distinguish independently runnable evaluation tooling from trace-first production observability platforms, even when both support scoring.
- Use the node's category boundary and materialized direct-child set as its navigation scope.
- List every materialized direct child exactly once and keep child-specific identity, facts, references, setup, runtime behavior, and mutable state with the child profile.
- Do not reproduce or depend on legacy `catalog-item`, `catalog-index`, `common/index`, or `catalog/item` schema/template selectors.

## Validation

- Navigation matches the materialized direct children.
- The page remains category-level and does not duplicate concrete child profiles.
- Effective processing does not depend on a legacy `meta.yml` file.
