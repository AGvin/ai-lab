# Claude Fable 5.1

Claude Fable 5.1 is Anthropic's concrete Fable release for demanding reasoning and long-horizon agentic work.

## Model series

- [Fable](../../../../)

## Provider profile

The following profile was checked against Anthropic documentation on October 18, 2026.

| Field | Provider-documented value |
| --- | --- |
| Claude API ID | `claude-fable-5-1` |
| Released | September 1, 2026 |
| Context / ordinary maximum output | 1M / 128K tokens |
| Input → output | Text and images → text |
| Thinking | Always-on adaptive thinking |

## Use and compatibility

Anthropic describes Fable 5.1 and [Mythos 5.1](../../../../../mythos/sub/models/sub/mythos-5-1/) as the same underlying model with different safeguards and access conditions. Their separate API IDs and hosted identities do not establish separate training. Fable's broader availability and Mythos's verification requirements must be checked for the deployment in question.

Anthropic requires 30-day data retention for this model; zero data retention needs its express authorization. Consult current migration guidance for platform applicability.

Selection depends on workload evaluation. Provider availability, prices, knowledge cutoffs, beta features, and retirement commitments can change; the current documentation provides those details.

## Official resources

- [Fable 5.1 documentation](https://platform.claude.com/docs/en/models/fable-5-1/overview)
- [Fable 5.1 and Mythos 5.1 announcement](https://www.anthropic.com/claude-fable-and-mythos-5-1)
- [Fable 5.1 and Mythos 5.1 system card](https://www.anthropic.com/claude-fable-5-1-mythos-5-1-system-card)
- [Fable 5.1 and Mythos 5.1 migration guidance](https://platform.claude.com/docs/en/models/fable-5-1/migration-guide)
- [Claude Platform release notes](https://platform.claude.com/docs/en/release-notes/overview)
