# Documentation Requirements

## Requirements

- Present `decision-support/` as the top-level owner for explicitly selected reader journeys whose primary job is choosing a route under real constraints rather than describing one canonical entity or explaining one concept.
- Materialize only decision-support branches that have been explicitly selected and have real content. The current selected branch is `user-scenarios/`; do not infer or create additional comparison, recommendation, portfolio, or decision-guide branches from the parent name alone.
- Keep canonical entity identity and intrinsic facts in `catalog/`, and link those owners rather than duplicating complete profiles inside decision-support pages.
- Keep evidence, concepts, implementation guidance, and risk/governance material with their own canonical owners when those domains are separately selected; decision-support pages may reference them as inputs without taking over their ownership.
- Use child navigation only for physically materialized, validated decision-support children.

## Validation

- Every materialized direct child is an explicitly selected decision-support journey with real content.
- No empty placeholder branches are created to anticipate unresolved taxonomy.
- Decision-support pages do not become duplicate canonical entity profiles or evidence stores.
- The current materialization does not imply that the broader non-catalog decision-support taxonomy has been finalized beyond `user-scenarios/`.
