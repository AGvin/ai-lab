# Documentation Requirements

## Requirements

- Identify GPT-6 Astra as the concrete `gpt-6-astra` model introduced by OpenAI on 2026-09-03.
- Preserve current provider-documented text/image input, text output, 1,050,000-token context, 128,000-token maximum output, April 30 2026 knowledge cutoff, and `low` / `medium` / `high` / `xhigh` / `max` reasoning-effort controls.
- Present complex reasoning, coding, computer-use, research, and document-work positioning as current OpenAI guidance rather than an independent AI Lab ranking.
- Keep pricing, plan rollout, rate limits, mutable tool availability, and routing behavior freshness-sensitive and outside intrinsic model identity.

## Validation

- GPT-6 Astra is a direct concrete member of GPT; no speculative GPT-6 series is created solely to anticipate future sibling models.
- Hosted product availability is distinguished from architectural/model facts.

## Source-scoped operating boundaries

- Tool use requires Responses; Chat Completions does not support tools for this model. Reasoning effort none and minimal are not supported. [Model reference](https://developers.openai.com/api/docs/models/gpt-6-astra).
- Tool calls express proposed actions. The application remains responsible for permissions and for handling untrusted instructions in files, skills, and tool results [Latest-model guide](https://developers.openai.com/api/docs/guides/latest-model).

## Source evidence

- [gpt-6-astra model reference](https://developers.openai.com/api/docs/models/gpt-6-astra).
- [API changelog](https://developers.openai.com/api/docs/changelog).
- [Latest-model guide](https://developers.openai.com/api/docs/guides/latest-model).
