# Documentation Requirements

## Requirements

- Present Model Gateways as the canonical index for self-managed software whose primary role is unifying model-provider access and controlling AI requests through provider abstraction, model API routing/fallback, model-aware policy, and usage or budget controls. Treat telemetry/evaluation features as secondary when the AI request-path gateway remains the product center; do not duplicate inference runtimes or provider-operated gateway services here.
- Use the node's category boundary and materialized direct-child set as its navigation scope.
- List every materialized direct child exactly once and keep child-specific identity, facts, references, setup, runtime behavior, and mutable state with the child profile.
- Do not reproduce or depend on legacy `catalog-item`, `catalog-index`, `common/index`, or `catalog/item` schema/template selectors.

## Validation

- Navigation matches the materialized direct children.
- The page remains category-level and does not duplicate concrete child profiles.
- Effective processing does not depend on a legacy `meta.yml` file.
