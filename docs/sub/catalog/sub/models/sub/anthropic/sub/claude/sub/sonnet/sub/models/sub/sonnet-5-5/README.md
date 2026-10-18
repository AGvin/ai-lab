# Claude Sonnet 5.5

Claude Sonnet 5.5 is Anthropic's second release in the Claude 5.5 generation, following Opus 5.5. Anthropic positions it for coding, knowledge work, and tool-using tasks.

## Model series

- [Sonnet](../../../../)

## Provider profile

The following profile was checked against Anthropic documentation on October 18, 2026.

| Field | Provider-documented value |
| --- | --- |
| Claude API ID | `claude-sonnet-5-5` |
| Released | September 28, 2026 |
| Context / ordinary maximum output | 1M / 128K tokens |
| Input → output | Text and images → text |
| Thinking | Adaptive by default, with configurable effort |

## Use and compatibility

To suppress upfront thinking, current Sonnet 5.5 requests use `thinking: {"type": "between_tools"}` in place of `disabled`, at effort `high` or below; tool-progress thinking can still remain. Combining this mode with `xhigh` or `max` returns an error. Check the model's API change guidance before migrating from Sonnet 5. Shared 5.5 naming does not merge this release with Opus 5.5.

Anthropic currently documents the Claude API, Amazon Bedrock, Google Cloud, Microsoft Foundry, and Claude Platform on AWS. Platform-specific behavior, prices, cache rates, safeguards and fallback routing, data-retention availability, effort defaults, and alias behavior remain mutable. Comparative speed, cost, and benchmark claims are attributed to their provider or evaluator.

## Official resources

- [Sonnet 5.5 announcement](https://www.anthropic.com/claude-sonnet-5-5)
- [Sonnet 5.5 documentation](https://platform.claude.com/docs/en/models/sonnet-5-5/overview)
- [Sonnet 5.5 API changes](https://platform.claude.com/docs/en/models/sonnet-5-5/whats-new-sonnet-5-5)
- [Thinking compatibility and limits](https://platform.claude.com/docs/en/build-with-claude/thinking-troubleshooting)
- [Current Claude models](https://platform.claude.com/docs/en/models/overview)
