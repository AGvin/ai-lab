# Documentation Requirements

## Requirements

- Identify GPT-6 Luna as the concrete `gpt-6-luna` model released by OpenAI on 2026-09-22.
- Preserve current provider-documented text/image input, text output, 1,050,000-token context, 128,000-token maximum output, May 18 2026 knowledge cutoff, and `none` / `low` / `medium` / `high` / `xhigh` / `max` reasoning-effort controls.
- Present focused high-volume/cost-sensitive workload positioning as current OpenAI guidance rather than an independent AI Lab ranking.
- Keep pricing, processing tier, data residency, rate limits, built-in tool availability, and API behavior freshness-sensitive and outside intrinsic model identity.

## Validation

- GPT-6 Luna is a direct concrete member of GPT and remains distinct from GPT-6 Astra and GPT-6 Sol.
- Hosted/API properties are not generalized into permanent architectural facts.

## Source-scoped operating boundaries

- Responses is the tool-capable API surface. Chat Completions supports function calling only with reasoning effort set to none. [Model reference](https://developers.openai.com/api/docs/models/gpt-6-luna).
- OpenAI’s October 7, 2026 system card distinguishes the October ChatGPT update from the September version still used in Codex and Work. That product update is not evidence that every API request uses the October version [October GPT-6 system card](https://deploymentsafety.openai.com/gpt-6-october).
- Tool calls express proposed actions. The application remains responsible for permissions and for handling untrusted instructions in files, skills, and tool results [Latest-model guide](https://developers.openai.com/api/docs/guides/latest-model).

## Source evidence

- [gpt-6-luna model reference](https://developers.openai.com/api/docs/models/gpt-6-luna).
- [API changelog](https://developers.openai.com/api/docs/changelog).
- [Latest-model guide](https://developers.openai.com/api/docs/guides/latest-model).
- [GPT-6 October 2026 system card](https://deploymentsafety.openai.com/gpt-6-october).
