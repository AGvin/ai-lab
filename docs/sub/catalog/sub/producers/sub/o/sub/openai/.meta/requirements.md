# Documentation Requirements

## Requirements

- Identify OpenAI as the canonical producer organization represented in this catalog.
- Preserve the official website and GitHub organization from canonical metadata.
- Preserve model-domain navigation without duplicating canonical semantic relation membership in requirements.
- Preserve Promptfoo Inc. as a distinct canonical organization in the documented organizational structure; do not treat Promptfoo software as a direct OpenAI-produced entity from organizational membership alone.
- Keep the OpenAI Skills repository deprecation status, successor repository, Skill Creator source status, and collection-specific distribution context with the collection owner.
- Keep model, assistant-workspace, coding-agent, framework, Promptfoo, access, pricing, plan, API, runtime, and selection information with their corresponding canonical owners.
- Render the standard `entity-relations` block from the validated current-entity relation projection.

## Content Specification

- Use `OpenAI` as the page title.
- Describe OpenAI concisely as the producer organization for the represented model, Agent Skill, assistant-workspace, coding-agent, and framework entities.
- Preserve the OpenAI model-domain view under `catalog/models/openai/` as navigation.
- Keep Promptfoo product provenance on the Promptfoo Inc. producer profile.
- Include the official website and GitHub organization.

## Validation

- The page does not duplicate model, individual Agent Skill, assistant-workspace, coding-agent, framework, or Promptfoo documentation.
- Product and service properties are not generalized into producer identity.
- The `entity-relations` block matches the validated current-entity relation projection and every rendered destination resolves to a canonical node.
- Model-domain navigation resolves to its canonical catalog node.
- Promptfoo organizational membership is not misrepresented as a direct OpenAI production relation.
- No link targets the removed `agent-skills/skills/` branch.

## Source-scoped operating boundaries

- Provenance does not imply one deployment or access policy. OpenAI publishes both hosted models and downloadable open weights; the latter are not served through its API or ChatGPT [Open-weight FAQ](https://help.openai.com/en/articles/11870455-openai-open-weight-models-gpt-oss).
- Lifecycle notices apply to the exact service and identifiers they name. Deprecation does not itself mean immediate shutdown [API deprecations](https://developers.openai.com/api/docs/deprecations).

## Source evidence

- [OpenAI official site](https://openai.com/).
- [OpenAI model catalog](https://developers.openai.com/api/docs/models).
- [Open-weight FAQ](https://help.openai.com/en/articles/11870455-openai-open-weight-models-gpt-oss).
- [gpt-oss-safeguard release](https://openai.com/index/introducing-gpt-oss-safeguard/).
- [API deprecations](https://developers.openai.com/api/docs/deprecations).
