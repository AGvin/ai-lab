# GPT-5.6 Luna

GPT-5.6 Luna is the fastest and most cost-efficient hosted tier in OpenAI's GPT-5.6 generation.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Official profile

- Model ID: `gpt-5.6-luna`
- Access form: hosted OpenAI API model
- Modalities: text and image input; text output
- Context window: 1,050,000 tokens
- Maximum output: 128,000 tokens
- Knowledge cutoff: February 16, 2026
- Reasoning: configurable reasoning-token support
- Fine-tuning: not supported

The official model page lists streaming, function calling, structured outputs, web search, file search, code interpreter, hosted shell, apply patch, computer use, MCP, and tool search among its supported capabilities.

## Pricing and limits

Standard API prices per one million tokens were $1.00 input, $0.10 cached input, and $6.00 output when verified on 2026-07-25. OpenAI applies a long-context multiplier above 272,000 input tokens.

Rate limits, regional availability, tool charges, caching rules, and prices are mutable service properties rather than parts of the model identity.

## Selection guidance

Consider Luna for high-volume hosted text work, low-latency routing, classification, extraction, drafting, and tool-integrated workflows whose required quality has been validated at this tier.

Do not infer that the lowest-cost GPT-5.6 tier is the cheapest route per accepted result. Measure omission risk, retries, verification calls, tool cost, latency, and escalation frequency against Terra, Sol, local models, and specialists.

OpenAI does not publish downloadable Luna weights or a local hardware profile on the cited model page; do not infer a VRAM requirement.

## Evidence

Specifications, capabilities, availability, and pricing were verified against the official model page on 2026-07-25. Role suitability, reliability, quality ceiling, and accepted-result cost remain workload-specific recommendations requiring evaluation.

## Related pages

- [GPT-5.6](../..)
- [GPT model family](../../../..)
- [OpenAI models](../../../../../..)

## Sources

- [GPT-5.6 Luna model page](https://developers.openai.com/api/docs/models/gpt-5.6-luna)
- [GPT-5.6 launch announcement](https://openai.com/index/gpt-5-6/)
