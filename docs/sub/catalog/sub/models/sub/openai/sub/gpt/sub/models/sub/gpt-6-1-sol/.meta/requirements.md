# Documentation Requirements

## Requirements

- Identify GPT-6.1 Sol as the concrete `gpt-6.1-sol` model released by OpenAI on 2026-09-29.
- Preserve current provider-documented text/image input, text output, 1,050,000-token context, 128,000-token maximum output, April 30 2026 knowledge cutoff, and `low` / `medium` / `high` / `xhigh` / `max` reasoning-effort controls only while current first-party documentation supports them.
- Preserve the current product boundary that `none` and `minimal` reasoning efforts are not supported and that Responses is the primary tool-calling surface.
- Treat Multi-agent as a current beta serving capability of GPT-6.1 Sol rather than a separate trained-model identity.
- Present OpenAI's near-Astra / lower-cost positioning as provider guidance rather than an independent AI Lab ranking.
- Keep pricing, processing tiers, data residency, rate limits, built-in tool availability, long-context pricing thresholds, and API behavior freshness-sensitive.

## Validation

- GPT-6.1 Sol is a direct concrete member of GPT and remains distinct from GPT-6 Sol, GPT-6 Astra, and GPT-6 Luna.
- Multi-agent beta is not materialized as a peer trained model.
- Hosted/API properties are not generalized into permanent architectural facts.

## Source-scoped operating boundaries

- Tool use requires Responses; Chat Completions does not support tools for this model. Reasoning effort none and minimal are not supported. [Model reference](https://developers.openai.com/api/docs/models/gpt-6.1-sol).
- Multi-agent is a beta serving capability. Processing tier, parallel work, and enabled tools are configuration rather than separate trained-model identities [Latest-model guide](https://developers.openai.com/api/docs/guides/latest-model).
- Tool calls express proposed actions. The application remains responsible for permissions and for handling untrusted instructions in files, skills, and tool results [Latest-model guide](https://developers.openai.com/api/docs/guides/latest-model).

## Source evidence

- [gpt-6.1-sol model reference](https://developers.openai.com/api/docs/models/gpt-6.1-sol).
- [API changelog](https://developers.openai.com/api/docs/changelog).
- [Latest-model guide](https://developers.openai.com/api/docs/guides/latest-model).
