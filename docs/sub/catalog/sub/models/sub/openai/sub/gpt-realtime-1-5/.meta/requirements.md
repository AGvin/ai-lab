# Documentation Requirements

## Requirements

- Identify GPT-Realtime-1.5 as OpenAI's released realtime audio model introduced on 2026-02-23 and still separately available in the current model catalog.
- Preserve current first-party-documented text/audio input-output, image input, 32k context, 4,096 maximum output, function calling, and WebRTC/WebSocket/SIP realtime boundary only at current release scope.
- Keep pricing, voice inventory, latency, rate limits, transport details, and provider positioning freshness-sensitive.
- Keep GPT-Realtime-1.5 distinct from the documented GPT-Realtime-2 and GPT-Realtime-2.1 releases. A distinct endpoint, alias, or serving setting does not by itself prove distinct weights.

## Validation

- The entity represents one trained model rather than the Realtime API.
- Lifecycle remains current/source-backed and is not inferred from marketing wording alone.

## Source-scoped operating boundaries

- Function calling is supported; Structured Outputs and fine-tuning are not documented as supported for this model. [Model reference](https://developers.openai.com/api/docs/models/gpt-realtime-1.5).
- Realtime event streaming is a session protocol; a generic streaming badge should not be used to deny streamed voice support. Browser sessions use server-created short-lived credentials, while application servers retain API keys and authorize tool actions [Realtime guide](https://developers.openai.com/api/docs/guides/realtime).

## Source evidence

- [gpt-realtime-1.5 model reference](https://developers.openai.com/api/docs/models/gpt-realtime-1.5).
- [Realtime guide](https://developers.openai.com/api/docs/guides/realtime).
- [Voice server controls](https://developers.openai.com/api/docs/guides/voice-server-controls).
- [API changelog](https://developers.openai.com/api/docs/changelog).
