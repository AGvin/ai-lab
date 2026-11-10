# Documentation Requirements

## Requirements

- Define Integrated Platforms as application- or developer-facing software combining several model lifecycle-at-inference surfaces (such as model acquisition/configuration, runtime management, packaging, local UX and API exposure) into one coherent product; distinguish integrated workflows from standalone inference engines, distributed cluster schedulers and separately operated hosted model services. Do not require a desktop GUI: developer-first packaging and service platforms may also qualify.
- Use the node's category boundary and materialized direct-child set as its navigation scope.
- List every materialized direct child exactly once and keep child-specific identity, facts, references, setup, runtime behavior, and mutable state with the child profile.
- Do not reproduce or depend on legacy `catalog-item`, `catalog-index`, `common/index`, or `catalog/item` schema/template selectors.

## Validation

- Navigation matches the materialized direct children.
- The page remains category-level and does not duplicate concrete child profiles.
- Effective processing does not depend on a legacy `meta.yml` file.
