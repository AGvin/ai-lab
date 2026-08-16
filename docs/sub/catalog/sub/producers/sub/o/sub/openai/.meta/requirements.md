# Documentation Requirements

## Requirements

- Identify OpenAI as the canonical producer organization represented in this catalog.
- Preserve the official website and GitHub organization from canonical metadata.
- Keep model-domain navigation while representing the current `produces` relations to GPT, Whisper, OpenAI Skills, ChatGPT, OpenAI Codex, and OpenAI Agents SDK.
- Preserve Promptfoo Inc. as a distinct canonical organization linked through `has-part`; do not treat Promptfoo software as a direct OpenAI-produced entity from organizational membership alone.
- Keep the OpenAI Skills repository deprecation status, successor repository, Skill Creator source status, and collection-specific distribution context with the collection owner.
- Keep model, ChatGPT, Codex, Agents SDK, Promptfoo, product-specific access, pricing, plan, API, runtime, and selection information with their corresponding canonical owners.

## Content Specification

- Use `OpenAI` as the page title.
- Describe OpenAI concisely as the producer organization for the represented model families, Agent Skill collection, assistant workspace, Codex software, and Agents SDK.
- Preserve the OpenAI model-domain view under `catalog/models/reference/producers/openai/` as navigation.
- Link GPT, Whisper, OpenAI Skills, ChatGPT, OpenAI Codex, and OpenAI Agents SDK through the producer's `produces` relations; do not link Skill Creator as a standalone catalog node.
- Link Promptfoo Inc. through the organizational `has-part` relation while keeping Promptfoo product provenance on the Promptfoo Inc. producer profile.
- Include the official website and GitHub organization.

## Validation

- The page does not duplicate model, individual Agent Skill, ChatGPT, Codex, Agents SDK, or Promptfoo documentation.
- Product and service properties are not generalized into producer identity.
- Model-domain and represented entity links resolve to canonical catalog nodes.
- Promptfoo organizational membership is not misrepresented as a direct OpenAI `produces` relation.
- No link targets the removed `agent-skills/skills/` branch.
