# Documentation Requirements

## Requirements

- Identify GPT-Realtime-2.1 Mini as OpenAI's current distilled realtime reasoning model for faster/lower-cost voice interactions with tool use.
- Preserve current first-party-documented text/audio input-output, image input, 128k context, 32k maximum output, reasoning support, function calling, and WebRTC/WebSocket/SIP deployment boundary.
- Keep pricing, rate limits, transport behavior, voice inventory, and comparative speed/cost positioning freshness-sensitive and provider-attributed.
- Keep GPT-Realtime-2.1 Mini separate from the full GPT-Realtime-2.1 model and from deprecated GPT-Realtime Mini.

## Validation

- The entity represents one trained model rather than a pricing tier or API endpoint.
- Distilled/cost positioning remains provider guidance.

## Source-scoped operating boundaries

- Function calling is supported; Structured Outputs and fine-tuning are not documented as supported for this model. [Model reference](https://developers.openai.com/api/docs/models/gpt-realtime-2.1-mini).
- Realtime event streaming is a session protocol; a generic streaming badge should not be used to deny streamed voice support. Browser sessions use server-created short-lived credentials, while application servers retain API keys and authorize tool actions [Realtime guide](https://developers.openai.com/api/docs/guides/realtime).

## Source evidence

- [gpt-realtime-2.1-mini model reference](https://developers.openai.com/api/docs/models/gpt-realtime-2.1-mini).
- [Realtime guide](https://developers.openai.com/api/docs/guides/realtime).
- [Voice server controls](https://developers.openai.com/api/docs/guides/voice-server-controls).
- [API changelog](https://developers.openai.com/api/docs/changelog).
