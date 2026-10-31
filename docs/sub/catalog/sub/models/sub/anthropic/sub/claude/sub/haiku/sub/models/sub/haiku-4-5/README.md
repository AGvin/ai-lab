# Claude Haiku 4.5

Claude Haiku 4.5 is a concrete model in Anthropic's Haiku series for latency-sensitive and cost-sensitive workloads.

## Model series

- [Haiku](../../../../)

## Provider profile

The following profile was checked against Anthropic documentation on October 18, 2026.

| Field | Provider-documented value |
| --- | --- |
| Claude API ID | `claude-haiku-4-5-20251001` |
| Lifecycle | Active (legacy) |
| Context / maximum output | 200K / 64K tokens |
| Thinking | Manual extended thinking |

## Use and compatibility

The legacy classification does not mean the model is retired. Anthropic now points to [Haiku 5.5](../haiku-5-5/) as the current Haiku release. Migrating changes thinking controls and token accounting, so existing integrations need the model-specific migration guidance.

The dated ID is the concrete snapshot; convenience aliases and provider IDs are access surfaces. Prices, knowledge cutoffs, platform availability, and retirement conditions remain mutable provider details.

## Official resources

- [Haiku 4.5 documentation](https://platform.claude.com/docs/en/models/haiku-4-5/overview)
- [Migration to Haiku 5.5](https://platform.claude.com/docs/en/models/haiku-5-5/migration-guide)
- [Model IDs and versioning](https://platform.claude.com/docs/en/about-claude/models/model-ids-and-versions)
