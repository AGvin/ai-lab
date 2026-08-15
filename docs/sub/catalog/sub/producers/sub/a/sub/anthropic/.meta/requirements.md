# Documentation Requirements

## Requirements

- Identify Anthropic as the canonical producer organization represented in this catalog.
- Preserve the official website and GitHub organization from the prior canonical metadata.
- Preserve model-domain navigation and link the canonical Anthropic Skills collection without duplicating model or skill details on the producer page.
- Keep collection composition, selected-skill purpose, dependencies, runtime/tool requirements, and source links with the Anthropic Skills collection owner.
- Keep product-specific access, pricing, plan, API, and model-selection information with their corresponding owners.

## Content Specification

- Use `Anthropic` as the page title.
- Describe Anthropic concisely as an AI research and product company represented here as a producer of documented models and Agent Skill resources.
- Link the Claude model family and Anthropic Skills collection from the producer's physically materialized `produces` relations; do not link collection-owned DOCX, PDF, PPTX, or XLSX skills as standalone catalog nodes.
- Preserve the Anthropic model-domain view under `catalog/models/reference/producers/anthropic/` as navigation rather than treating the view node itself as a produced entity.
- Include the official website and GitHub organization.

## Validation

- The page does not duplicate Claude, concrete model, or individual Agent Skill profiles.
- Product and service properties are not generalized into producer identity.
- The Anthropic/Claude and Anthropic/Anthropic Skills `produces` / `produced-by` relation pairs are physically present at both endpoints and semantically consistent.
- Model-domain and collection links resolve to canonical catalog nodes.
- No link targets the removed `agent-skills/skills/` branch.
