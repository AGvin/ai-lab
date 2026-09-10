# Documentation Requirements

## Requirements

- Present Agents as the canonical software catalog index for ready-to-use AI agent products that perform development or general computer tasks.
- Group materialized direct children by the product's primary execution boundary rather than by whether it can call a remote model API.
- Define Local Agents as products whose primary agent execution is installable or self-managed and controlled by the user; optional hosted model or API access alone does not make a product hybrid.
- Define Hybrid Agents as products whose current supported product surface materially spans both user-controlled local or self-managed execution and managed or hosted execution.
- Keep hosted-first development agents whose primary execution environment is vendor-operated under `catalog/services/development/agents/`.
- List every materialized direct child exactly once with a concise description of its ownership boundary.
- Keep product-specific identity, capabilities, setup, runtime behavior, deployment details, and service dependencies with the child profiles.
- Do not reproduce or depend on legacy `catalog-item`, `catalog-index`, `common/index`, or `catalog/item` selectors.

## Content Specification

- Link Local Agents and Hybrid Agents with concise descriptions that make their execution-boundary distinction understandable without internal taxonomy knowledge.
- Link the Hosted Development Agents service index as the adjacent catalog boundary for hosted-first products.

## Validation

- Navigation matches the materialized direct children.
- Optional remote model/API usage is not treated as sufficient evidence for Hybrid placement.
- Hosted-first services are not duplicated as software-agent profiles merely to complete the taxonomy.
- The page remains category-level and does not duplicate concrete agent profiles.
