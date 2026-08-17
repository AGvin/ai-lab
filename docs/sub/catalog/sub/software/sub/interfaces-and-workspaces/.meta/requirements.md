# Documentation Requirements

## Requirements

- Present Interfaces and Workspaces as the canonical software catalog index for user-facing applications used to interact with models, conversations, knowledge bases, agents, and integrated AI workspaces.
- Render the standard child-navigation block from the validated direct-child projection so every materialized direct child appears exactly once.
- Preserve the distinction between model clients, conversational platforms, integrated workspaces, and knowledge workspaces while keeping product-specific facts with child profiles.
- Do not reproduce or depend on legacy `catalog-item`, `catalog-index`, `common/index`, or `catalog/item` selectors.

## Validation

- The child-navigation block matches the validated materialized direct-child projection.
- The page remains category-level and does not duplicate concrete application profiles.
- The page contains no temporary-placeholder wording.
