# Documentation Requirements

## Requirements

- Present Local Agents as the canonical software index for installable or self-managed agent products whose primary agent execution surface is controlled by the user.
- Base classification on where the agent loop and workspace execution run, not on whether the software calls a remote model API or supports optional online integrations.
- List every materialized direct child exactly once with a concise, source-backed description of its primary role or execution surface.
- Keep concrete installation, runtime, model-access, tool-integration, security, and mutable provider facts with child software profiles.
- Keep products whose supported product surface materially includes managed hosted agent execution under the sibling Hybrid Agents index.
- Keep hosted-first agent services whose primary execution environment is vendor-operated under `catalog/services/development/agents/`.

## Content Specification

- Explain the Local Agents execution boundary before the child list.
- Describe all materialized direct children concisely from current official sources.
- Link the sibling Hybrid Agents index and the Hosted Development Agents service index as adjacent ownership boundaries.

## Validation

- Navigation matches the materialized direct children.
- Hosted model/API access alone does not change the primary ownership classification.
- Products with a material first-party hosted agent-execution surface are not retained here merely because they also provide a local client.
- Product summaries remain consistent with their canonical child profiles and official-source boundaries.
