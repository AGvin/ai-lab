# Claude Sonnet 5

Claude Sonnet 5 is Anthropic's hosted Sonnet model for agentic, coding, reasoning, and knowledge-work workloads.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Official profile

- API model ID: `claude-sonnet-5`
- Access form: Claude API, Claude Platform, Claude Code, and Anthropic's Claude plans
- Context window: 1,000,000 tokens by default and at maximum
- Maximum output: 128,000 tokens
- Reasoning: adaptive thinking is enabled by default

Anthropic describes Sonnet 5 as able to plan and use tools such as browsers and terminals. Product and cloud-platform availability are deployment dimensions, not separate model identities.

## Pricing

Anthropic announced introductory Claude Platform pricing of $2 per million input tokens and $10 per million output tokens through 2026-08-31. It announced standard pricing of $3 input and $15 output per million tokens after that boundary.

Pricing and plan availability were verified on 2026-07-25 and can change.

## Limitations and migration notes

- Manual extended thinking is removed; use adaptive thinking and the effort parameter.
- Non-default `temperature`, `top_p`, or `top_k` values return an error.
- Priority Tier was not available for Sonnet 5 at verification time.
- The updated tokenizer can change token counts, so recount representative prompts before migration.

This is a hosted model; the cited sources do not publish downloadable weights or local hardware requirements.

## Selection guidance

Evaluate Sonnet 5 for coding agents, tool use, reasoning, and knowledge work. Treat Anthropic's benchmark comparisons as provider-reported evidence and validate the model on the intended workflow.

## Evidence

Specifications, behavior, availability, and time-bounded pricing were verified on 2026-07-25.

## Related pages

- [Claude model family](../../)
- [Anthropic models](../../../..)

## Sources

- [Introducing Claude Sonnet 5](https://www.anthropic.com/research/claude-sonnet-5)
- [Claude Sonnet 5 platform changes](https://platform.claude.com/docs/en/about-claude/models/whats-new-sonnet-5)
