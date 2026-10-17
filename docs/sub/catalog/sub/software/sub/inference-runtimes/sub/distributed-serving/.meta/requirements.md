# Documentation Requirements

## Requirements

- Define Distributed Serving as multi-instance or cluster-oriented model deployment control planes and orchestration layers whose primary role is scheduling, scaling, routing, rollout, and serving coordination across worker/model-server instances; distinguish orchestration products from the underlying single-worker inference engine and local all-in-one runners, even when an orchestrator bundles a runtime.
- Use the node's category boundary and materialized direct-child set as its navigation scope.
- List every materialized direct child exactly once and keep child-specific identity, facts, references, setup, runtime behavior, and mutable state with the child profile.
- Do not reproduce or depend on legacy `catalog-item`, `catalog-index`, `common/index`, or `catalog/item` schema/template selectors.

## Validation

- Navigation matches the materialized direct children.
- The page remains category-level and does not duplicate concrete child profiles.
- Effective processing does not depend on a legacy `meta.yml` file.
