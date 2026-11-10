# Claude Haiku 5.5

Anthropic released Claude Haiku 5.5 for high-volume, latency-sensitive work such as routing, extraction, classification, and subagent tasks.

## Model series

- [Haiku](../../../../)

## Provider profile

The following profile was checked against Anthropic documentation on October 18, 2026.

| Field | Provider-documented value |
| --- | --- |
| Claude API ID | `claude-haiku-5-5` |
| Released | October 7, 2026 |
| Context / ordinary maximum output | 1M / 128K tokens |
| Input → output | Text and images → text |
| Thinking | Adaptive; effort controls depth |

## Use and compatibility

Haiku 5.5 is a separate release from Haiku 4.5. Migration changes manual thinking controls, and retained assistant thinking blocks count toward input tokens. Consult the migration guide before assuming request or cost compatibility.

Anthropic currently documents access through the Claude API, Amazon Bedrock, Google Cloud, Microsoft Foundry, and Claude Platform on AWS. Platform IDs and restrictions, prompt-length pricing tiers, cache and batch behavior, tokenizer differences, effort defaults, cutoffs, and retirement commitments are mutable. Speed, cost, and benchmark comparisons are provider claims rather than independent workload acceptance results.

## Official resources

- [Haiku 5.5 announcement](https://www.anthropic.com/claude-haiku-5-5)
- [Haiku 5.5 documentation](https://platform.claude.com/docs/en/models/haiku-5-5/overview)
- [Migration to Haiku 5.5](https://platform.claude.com/docs/en/models/haiku-5-5/migration-guide)
