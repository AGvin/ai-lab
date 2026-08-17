# Documentation Requirements

## Requirements

- Identify Anthropic as the canonical producer organization represented in this catalog.
- Preserve the official website and GitHub organization from the prior canonical metadata.
- Preserve model-domain navigation without duplicating model, collection, or software-owned details on the producer page.
- Keep collection composition, selected-skill purpose, dependencies, runtime/tool requirements, and source links with their collection owner.
- Keep software capabilities, installation, access, pricing, plan, runtime, and workflow details with their software owner.
- Keep product-specific access, pricing, plan, API, and model-selection information with their corresponding owners.
- Render the standard `entity-relations` block from the validated current-entity relation projection.

## Content Specification

- Use `Anthropic` as the page title.
- Describe Anthropic concisely as an AI research and product company represented here as a producer of documented models, Agent Skill resources, and software.
- Preserve the Anthropic model-domain view under `catalog/models/reference/producers/anthropic/` as navigation rather than treating the view node itself as a produced entity.
- Include the official website and GitHub organization.

## Validation

- The page does not duplicate model, individual Agent Skill, or software product documentation.
- Product and service properties are not generalized into producer identity.
- The `entity-relations` block matches the validated current-entity relation projection and every rendered destination resolves to a canonical node.
- Model-domain navigation resolves to its canonical catalog node.
- No link targets the removed `agent-skills/skills/` branch.
