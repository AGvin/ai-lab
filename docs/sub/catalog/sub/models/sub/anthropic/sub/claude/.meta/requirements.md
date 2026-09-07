# Documentation Requirements

## Requirements

- Identify Claude as Anthropic's long-lived hosted model family.
- Preserve family-level facts without duplicating series or concrete-model specifications.
- Represent the currently materialized Fable, Opus, Sonnet, Haiku, and Mythos lines as model series; keep their concrete release facts with the corresponding model nodes.
- Keep product surfaces, pricing, cloud availability, and migration behavior outside family identity unless needed to explain a model-family boundary.

## Content Specification

- Use `Claude` as the page title and link Anthropic through the canonical `produced-by` relation.
- Link every materialized Claude series exactly once: Fable, Opus, Sonnet, Haiku, and Mythos.
- Keep Claude Code, Claude Platform, Anthropic plans, and cloud integrations distinct from model identity.
- Include current official model-overview and model-ID/versioning documentation.

## Validation

- Concrete Claude models are reached through their materialized series rather than linked as arbitrary family children.
- Series are not treated as second top-level families.
- Concrete model IDs, context limits, pricing, availability constraints, and migration notes are not generalized to all Claude models.
