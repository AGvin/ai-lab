# Documentation Requirements

## Requirements

- Identify GPT-Realtime-2.1 as OpenAI's current realtime reasoning voice model with tool use.
- Preserve current first-party-documented text/audio input-output, image input, 128k context, 32k maximum output, reasoning-effort control, function calling, and WebRTC/WebSocket/SIP realtime deployment boundary.
- Keep mutable pricing, latency behavior, voice inventory, transport details, endpoint behavior, rate limits, and provider positioning freshness-sensitive.
- Keep GPT-Realtime-2.1 distinct from GPT-Live-1: Realtime 2.1 owns realtime reasoning/tool-use voice-agent behavior while GPT-Live owns the full-duplex conversational front-end/delegation model boundary.

## Validation

- The entity represents one trained model rather than the Realtime API itself.
- Provider guidance is not converted into an independent model ranking.

## Source-scoped operating boundaries

- Function calling is supported; Structured Outputs and fine-tuning are not documented as supported for this model. Higher reasoning effort can increase latency and output-token use. [Model reference](https://developers.openai.com/api/docs/models/gpt-realtime-2.1).
- Realtime event streaming is a session protocol; a generic streaming badge should not be used to deny streamed voice support. Browser sessions use server-created short-lived credentials, while application servers retain API keys and authorize tool actions [Realtime guide](https://developers.openai.com/api/docs/guides/realtime).

## Source evidence

- [gpt-realtime-2.1 model reference](https://developers.openai.com/api/docs/models/gpt-realtime-2.1).
- [Realtime guide](https://developers.openai.com/api/docs/guides/realtime).
- [Voice server controls](https://developers.openai.com/api/docs/guides/voice-server-controls).
- [API changelog](https://developers.openai.com/api/docs/changelog).
