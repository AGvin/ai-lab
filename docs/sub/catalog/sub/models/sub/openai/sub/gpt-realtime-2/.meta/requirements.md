# Documentation Requirements

## Requirements

- Identify GPT-Realtime-2 as OpenAI's released realtime reasoning voice model for low-latency speech-to-speech applications with configurable reasoning effort and tool use.
- Preserve current first-party-documented text/audio input-output, image input, 128k context, 32k maximum output, reasoning controls, function calling, and Realtime transport boundary only at current release scope.
- Keep pricing, latency, voice inventory, transport details, rate limits, and current provider positioning freshness-sensitive.
- Keep GPT-Realtime-2 distinct from GPT-Realtime-2.1 and GPT-Realtime-1.5 rather than collapsing independently addressable current model IDs into one identity.

## Validation

- The entity represents one trained model rather than the Realtime API.
- Comparative provider claims remain source-attributed.

## Source-scoped operating boundaries

- Function calling is supported; Structured Outputs and fine-tuning are not documented as supported for this model. Higher reasoning effort can increase latency and output-token use. [Model reference](https://developers.openai.com/api/docs/models/gpt-realtime-2).
- Realtime event streaming is a session protocol; a generic streaming badge should not be used to deny streamed voice support. Browser sessions use server-created short-lived credentials, while application servers retain API keys and authorize tool actions [Realtime guide](https://developers.openai.com/api/docs/guides/realtime).

## Source evidence

- [gpt-realtime-2 model reference](https://developers.openai.com/api/docs/models/gpt-realtime-2).
- [Realtime guide](https://developers.openai.com/api/docs/guides/realtime).
- [Voice server controls](https://developers.openai.com/api/docs/guides/voice-server-controls).
- [API changelog](https://developers.openai.com/api/docs/changelog).
