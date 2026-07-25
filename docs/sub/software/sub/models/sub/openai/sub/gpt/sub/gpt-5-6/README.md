# GPT-5.6

GPT-5.6 is an OpenAI model generation introduced with a durable three-tier naming scheme: Sol, Terra, and Luna.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Generation structure

The number identifies the model generation. The tier name identifies the intended capability, latency, and cost position and may evolve on its own cadence.

- **GPT-5.6 Sol** — flagship tier for complex professional work, coding, reasoning, research, tool use, computer use, science, and cybersecurity.
- **GPT-5.6 Terra** — balanced tier for strong capability at a lower cost.
- **GPT-5.6 Luna** — fastest and most cost-efficient tier for high-volume workloads.

## Shared API characteristics

Official API documentation lists the following shared characteristics for the three tiers:

- text and image input;
- text output;
- multilingual and vision capabilities;
- Responses API and client SDK support;
- function calling, web search, file search, and computer use;
- configurable reasoning effort: `none`, `low`, `medium`, `high`, `xhigh`, and `max`;
- 1.05 million token context window;
- 128,000 maximum output tokens;
- February 16, 2026 knowledge cutoff.

## API identifiers

- Sol: `gpt-5.6-sol`
- Terra: `gpt-5.6-terra`
- Luna: `gpt-5.6-luna`
- Generation alias: `gpt-5.6`, which routes to `gpt-5.6-sol`

Use explicit tier identifiers when reproducibility, cost control, or stable workload evaluation matters.

## Pricing

OpenAI lists standard API token prices per one million tokens:

| Tier | Input | Output |
| --- | ---: | ---: |
| GPT-5.6 Sol | $5.00 | $30.00 |
| GPT-5.6 Terra | $2.50 | $15.00 |
| GPT-5.6 Luna | $1.00 | $6.00 |

Pricing, caching rules, regional availability, and product-plan access can change. Verify them before operational adoption.

## Product availability

GPT-5.6 is available through ChatGPT, Codex, and the OpenAI API. Product surfaces expose different tier and reasoning controls depending on the user's plan and rollout state.

ChatGPT product labels and plan-specific behavior are not separate model generations. Document them under the ChatGPT assistant node and link back to the canonical model pages.

## Migration guidance

OpenAI recommends starting GPT-5.5 or GPT-5.4 migrations with the existing reasoning setting, then testing both that setting and one level lower on representative workloads. GPT-5.6 may preserve or improve quality with fewer reasoning tokens, but the correct setting remains workload-specific.

Use the Responses API for reasoning, tool calling, and multi-turn workflows.

## Child nodes

Create separate pages for:

- GPT-5.6 Sol;
- GPT-5.6 Terra;
- GPT-5.6 Luna.

## Related pages

- [GPT model family](../../)
- [OpenAI models](../../../..)
- [Models](../../../../../..)
- [General repository disclaimer](../../../../../../../../disclaimer/)

## Sources

- [GPT-5.6 launch announcement](https://openai.com/index/gpt-5-6/)
- [OpenAI model catalog](https://developers.openai.com/api/docs/models)
- [OpenAI model guidance](https://developers.openai.com/api/docs/guides/latest-model)
- [GPT-5.6 in ChatGPT](https://help.openai.com/en/articles/20001354-gpt-56-in-chatgpt/)
