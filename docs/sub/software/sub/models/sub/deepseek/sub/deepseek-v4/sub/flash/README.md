# DeepSeek V4 Flash

DeepSeek V4 Flash is DeepSeek's lower-priced V4 model for long-context reasoning and agentic API workloads.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Official profile

- API model ID: `deepseek-v4-flash`
- Model version name: `DeepSeek-V4-Flash`
- Access forms: DeepSeek API, DeepSeek chat service, and an official open-weight release
- Architecture scale: 284 billion total parameters and 13 billion active parameters
- Context length: 1,000,000 tokens
- Maximum output: 384,000 tokens
- Modes: thinking by default, with non-thinking also supported

The API supports OpenAI Chat Completions and Anthropic-compatible protocols, JSON output, tool calls, chat prefix completion, and non-thinking FIM completion.

## Aliases and artifacts

The retired compatibility names `deepseek-chat` and `deepseek-reasoner` mapped to the non-thinking and thinking modes of `deepseek-v4-flash`; they were scheduled to become inaccessible after 2026-07-24 15:59 UTC. Use the exact V4 Flash ID.

DeepSeek announced official open weights, but the API ID and a downloadable artifact are distinct deployment identities. The cited release does not establish a license or a comparison-specific quantization.

## Pricing

At verification time, DeepSeek listed prices per million tokens of $0.0028 for cache-hit input, $0.14 for cache-miss input, and $0.28 for output.

## Selection and hardware guidance

Evaluate V4 Flash for economical long-context reasoning, tool use, and agent workflows. Confirm API behavior and artifact quality on representative tasks.

The official sources cited here do not publish a measured local deployment profile. Do not infer a VRAM requirement or consumer-GPU fit from parameter counts.

## Evidence

Specifications, aliases, API features, availability, and pricing were verified on 2026-07-25.

## Related pages

- [DeepSeek V4](../../)
- [DeepSeek models](../../../..)

## Sources

- [DeepSeek API models and pricing](https://api-docs.deepseek.com/quick_start/pricing/)
- [DeepSeek V4 preview release](https://api-docs.deepseek.com/news/news260424/)
