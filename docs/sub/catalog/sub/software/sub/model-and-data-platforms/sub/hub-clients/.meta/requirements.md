# Documentation Requirements

## Requirements

- Define Hub Clients as installable SDKs or command-line clients whose primary role is programmatic access to model, dataset, and artifact hubs (search, download, upload, repository and metadata management); distinguish client libraries from hosted hub services, model runtime engines, and complete ML lifecycle platforms.
- Use the node's category boundary and materialized direct-child set as its navigation scope.
- List every materialized direct child exactly once and keep child-specific identity, facts, references, setup, runtime behavior, and mutable state with the child profile.
- Do not reproduce or depend on legacy `catalog-item`, `catalog-index`, `common/index`, or `catalog/item` schema/template selectors.

## Validation

- Navigation matches the materialized direct children.
- The page remains category-level and does not duplicate concrete child profiles.
- Effective processing does not depend on a legacy `meta.yml` file.
