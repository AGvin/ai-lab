# Documentation Requirements

## Requirements

- Present `software/` as the canonical catalog owner for installable or self-managed software grouped by primary role.
- Keep hosted-only or externally operated service identity under `catalog/services/`; keep models, datasets, hardware, and producers with their separate canonical catalog owners.
- Link every currently materialized direct software category exactly once.
- Treat category placement as primary-role ownership rather than an assertion that a product has only one capability.
- Keep the page concise; concrete software facts, installation details, operational guidance, and comparisons belong to their appropriate child or non-catalog owners.

## Content Specification

- List: development tools, agents, agent frameworks, inference runtimes, application frameworks, workflow engines, interfaces and workspaces, automation, model and data platforms, evaluation and observability, gateways, and data infrastructure.

## Validation

- The page contains no temporary-placeholder wording.
- Every listed child link resolves to a materialized direct child of `software/`.
- The page does not absorb hosted-only services, model identity, dataset identity, hardware identity, or producer identity.
- The page does not duplicate concrete software profiles.
