# Documentation Requirements

## Requirements

- Present Inference Runtimes as the canonical software catalog index for software that loads models and executes inference locally, on servers, or across distributed serving infrastructure.
- List every materialized direct child exactly once.
- Preserve the category split between integrated platforms, inference engines, and distributed serving while keeping runtime-specific facts with child profiles.
- Do not reproduce or depend on legacy `catalog-item`, `catalog-index`, `common/index`, or `catalog/item` selectors.

## Validation

- Navigation matches the materialized direct children.
- The page remains category-level and does not duplicate concrete runtime profiles.
- The page contains no temporary-placeholder wording.
