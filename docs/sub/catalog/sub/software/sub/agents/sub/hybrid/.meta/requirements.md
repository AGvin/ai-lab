# Documentation Requirements

## Requirements

- Present Hybrid Agents as the canonical software index for agent products whose current supported product surface materially spans both user-controlled local or self-managed execution and managed or hosted execution.
- Base classification on supported execution and deployment surfaces, not on vendor branding or the mere use of a hosted model API.
- List every materialized direct child exactly once with a concise, source-backed description of the execution surfaces that make it relevant to this category.
- Keep product-specific capabilities, installation, runtime behavior, deployment modes, hosted dependencies, and mutable service state with each child profile.
- Keep products whose primary execution remains user-controlled under the sibling Local Agents index.
- Keep hosted-first agent services whose primary execution environment is vendor-operated under `catalog/services/development/agents/`.

## Content Specification

- Explain the Hybrid Agents boundary before the child list.
- Describe Claude Code, Factory Droid, GitHub Copilot, Kilo Code, OpenAI Codex, and OpenHands concisely from current official sources.
- Link the sibling Local Agents index and the Hosted Development Agents service index as adjacent ownership boundaries.

## Validation

- Navigation matches the materialized direct children.
- The page does not imply that every Hybrid Agent requires a vendor cloud control plane for all supported deployment modes.
- Optional hosted access alone does not change a primarily local product into a Hybrid Agent.
- Product summaries remain consistent with their canonical child profiles and official-source boundaries.
