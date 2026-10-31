# Documentation Requirements

## Requirements

- Identify GPT-Audio-1.5 as OpenAI's released audio-input/audio-output model for Chat Completions, introduced on 2026-02-23 and serving as the replacement for deprecated legacy GPT Audio families.
- Preserve current first-party-documented text/audio input-output, 128k context, 16,384 maximum output, function calling, and Chat Completions audio boundary only at current release scope.
- Keep pricing, voice selection, response formats, rate limits, endpoint support, and provider positioning freshness-sensitive.
- Keep GPT-Audio-1.5 distinct from realtime voice models: its primary served boundary is audio-capable Chat Completions rather than low-latency Realtime sessions.

## Validation

- The entity represents one trained model rather than an Audio API endpoint.
- Deprecated predecessor aliases are not materialized as new current identities.

## Source-scoped operating boundaries

- This is the REST Chat Completions audio surface, distinct from a Realtime session. Function calling and streaming are supported, while Structured Outputs are not listed as supported [Model reference](https://developers.openai.com/api/docs/models/gpt-audio-1.5).
- Voice formats, transport, latency, and application permissions are deployment concerns. A generated tool call still requires the application’s authorization before execution.

## Source evidence

- [gpt-audio-1.5 model reference](https://developers.openai.com/api/docs/models/gpt-audio-1.5).
- [API changelog](https://developers.openai.com/api/docs/changelog).
