# Documentation Requirements

## Requirements

- Identify OpenAI as the canonical producer organization represented in this catalog.
- Preserve the official website and GitHub organization from canonical metadata.
- Keep model-domain navigation while representing the current `produces` relations to GPT, Whisper, OpenAI Skills, ChatGPT, OpenAI Codex, and OpenAI Agents SDK.
- Keep the OpenAI Skills repository deprecation status, successor repository, Skill Creator source status, and collection-specific distribution context with the collection owner.
- Keep model, ChatGPT, Codex, Agents SDK, product-specific access, pricing, plan, API, runtime, and selection information with their corresponding canonical owners.

## Content Specification

- Use `OpenAI` as the page title.
- Describe OpenAI concisely as the producer organization for the represented model families, Agent Skill collection, assistant workspace, Codex software, and Agents SDK.
- Preserve the OpenAI model-domain view under `catalog/models/reference/producers/openai/` as navigation.
- Link GPT, Whisper, OpenAI Skills, ChatGPT, OpenAI Codex, and OpenAI Agents SDK through the producer's `produces` relations; do not link Skill Creator as a standalone catalog node.
- Include the official website and GitHub organization.

## Validation

- The page does not duplicate model, individual Agent Skill, ChatGPT, Codex, or Agents SDK documentation.
- Product and service properties are not generalized into producer identity.
- Model-domain and represented entity links resolve to canonical catalog nodes.
- No link targets the removed `agent-skills/skills/` branch.
