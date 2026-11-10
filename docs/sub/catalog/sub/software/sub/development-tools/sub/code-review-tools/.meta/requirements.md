# Documentation Requirements

## Requirements

- Define Code Review Tools as software whose primary role is inspecting proposed code changes, commits, or pull-request diffs and producing actionable correctness, security, quality, or maintainability feedback, including inline review comments and suggested changes; distinguish review-first products from codebase-indexing intelligence, code editors, and general automated test runners.
- Use the node's category boundary and materialized direct-child set as its navigation scope.
- List every materialized direct child exactly once and keep child-specific identity, facts, references, setup, runtime behavior, and mutable state with the child profile.
- Do not reproduce or depend on legacy `catalog-item`, `catalog-index`, `common/index`, or `catalog/item` schema/template selectors.

## Validation

- Navigation matches the materialized direct children.
- The page remains category-level and does not duplicate concrete child profiles.
- Effective processing does not depend on a legacy `meta.yml` file.
