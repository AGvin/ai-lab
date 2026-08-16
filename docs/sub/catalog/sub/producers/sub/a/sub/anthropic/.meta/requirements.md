# Documentation Requirements

## Requirements

- Identify Anthropic as the canonical producer organization represented in this catalog.
- Preserve the official website and GitHub organization from the prior canonical metadata.
- Preserve model-domain navigation and link the canonical Anthropic Skills collection and Claude Code software profile without duplicating their owned details on the producer page.
- Keep collection composition, selected-skill purpose, dependencies, runtime/tool requirements, and source links with the Anthropic Skills collection owner.
- Keep Claude Code capabilities, installation, access, pricing, plan, runtime, and workflow details with the Claude Code software owner.
- Keep product-specific access, pricing, plan, API, and model-selection information with their corresponding owners.

## Content Specification

- Use `Anthropic` as the page title.
- Describe Anthropic concisely as an AI research and product company represented here as a producer of documented models, Agent Skill resources, and Claude Code.
- Link the Claude model family, Anthropic Skills collection, and Claude Code through the producer's `produces` relations; do not link collection-owned DOCX, PDF, PPTX, or XLSX skills as standalone catalog nodes.
- Preserve the Anthropic model-domain view under `catalog/models/reference/producers/anthropic/` as navigation rather than treating the view node itself as a produced entity.
- Include the official website and GitHub organization.

## Validation

- The page does not duplicate Claude, concrete model, individual Agent Skill, or Claude Code product documentation.
- Product and service properties are not generalized into producer identity.
- Model-domain, collection, and Claude Code links resolve to canonical catalog nodes.
- No link targets the removed `agent-skills/skills/` branch.
