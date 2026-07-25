# GPT-5.6 Terra

GPT-5.6 Terra is the balanced capability-and-cost tier of OpenAI's GPT-5.6 generation.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Official profile

- Model ID: `gpt-5.6-terra`
- Access form: hosted OpenAI API model
- Modalities: text and image input; text output
- Context window: 1,050,000 tokens
- Maximum output: 128,000 tokens
- Knowledge cutoff: February 16, 2026
- Reasoning: reasoning-token support
- Fine-tuning: not supported

The official model page lists streaming, function calling, structured outputs, web search, file search, code interpreter, hosted shell, apply patch, computer use, MCP, and tool search among its supported capabilities.

## Pricing and limits

Standard API prices per one million tokens were $2.50 input, $0.25 cached input, and $15.00 output when verified on 2026-07-25. OpenAI applies a long-context multiplier above 272,000 input tokens.

Rate limits, regional availability, tool charges, and prices are mutable service properties rather than parts of the model identity.

## Selection guidance

Consider Terra for hosted reasoning, coding, multimodal analysis, and tool-using workloads that need a lower token price than the Sol tier. Validate quality, latency, and total tool cost on representative tasks.

OpenAI does not publish downloadable Terra weights or a local hardware profile on the cited model page; do not infer a VRAM requirement.

## Evidence

Specifications, capabilities, availability, and pricing were verified against the official model page on 2026-07-25.

## Related pages

- [GPT-5.6](../../)
- [GPT model family](../../../..)

## Sources

- [GPT-5.6 Terra model page](https://developers.openai.com/api/docs/models/gpt-5.6-terra)
