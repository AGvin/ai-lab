# Documentation Requirements

## Requirements

- Define Model Libraries as reusable software packages centered on accessible pretrained model architectures, weights/model loaders, processors, and domain-specific model APIs (such as text, diffusion, or audio), which may support inference and fine-tuning; distinguish this primary role from general training frameworks, remote model hubs, and inference-only servers.
- Use the node's category boundary and materialized direct-child set as its navigation scope.
- List every materialized direct child exactly once and keep child-specific identity, facts, references, setup, runtime behavior, and mutable state with the child profile.
- Do not reproduce or depend on legacy `catalog-item`, `catalog-index`, `common/index`, or `catalog/item` schema/template selectors.

## Validation

- Navigation matches the materialized direct children.
- The page remains category-level and does not duplicate concrete child profiles.
- Effective processing does not depend on a legacy `meta.yml` file.
