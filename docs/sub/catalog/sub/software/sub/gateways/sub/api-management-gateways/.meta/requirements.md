# Documentation Requirements

## Requirements

- Present API Management Gateways as the canonical index for self-managed products whose primary role is general-purpose API ingress, proxying, routing, authentication, traffic policy, and governance, with AI or MCP traffic supported as a material capability rather than the sole defining product identity. Keep model-provider-first gateways under Model Gateways and hosted producer-operated control planes under Services.
- Use the node's category boundary and materialized direct-child set as its navigation scope.
- List every materialized direct child exactly once and keep child-specific identity, facts, references, setup, runtime behavior, and mutable state with the child profile.
- Do not reproduce or depend on legacy `catalog-item`, `catalog-index`, `common/index`, or `catalog/item` schema/template selectors.

## Validation

- Navigation matches the materialized direct children.
- The page remains category-level and does not duplicate concrete child profiles.
- Effective processing does not depend on a legacy `meta.yml` file.
