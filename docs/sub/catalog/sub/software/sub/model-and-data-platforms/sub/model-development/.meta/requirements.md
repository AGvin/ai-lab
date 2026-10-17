# Documentation Requirements

## Requirements

- Define Model Development as reusable local frameworks, libraries, and toolchains whose primary role is implementing, training, adapting, fine-tuning, or reinforcing machine-learning and foundation models, including distributed training and training-time efficiency; distinguish this role from pretrained architecture/model-loading libraries, post-training model artifact optimization, and end-to-end lifecycle management platforms.
- Use the node's category boundary and materialized direct-child set as its navigation scope.
- List every materialized direct child exactly once and keep child-specific identity, facts, references, setup, runtime behavior, and mutable state with the child profile.
- Do not reproduce or depend on legacy `catalog-item`, `catalog-index`, `common/index`, or `catalog/item` schema/template selectors.

## Validation

- Navigation matches the materialized direct children.
- The page remains category-level and does not duplicate concrete child profiles.
- Effective processing does not depend on a legacy `meta.yml` file.
