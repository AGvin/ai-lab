# GPT-Realtime-2.1

`gpt-realtime-2.1` is OpenAI’s concrete model for realtime voice applications. OpenAI positions this release as an improvement to Realtime 2 for alphanumeric speech, noisy audio, silence, and interruptions.

## Profile

The API profile lists text and audio input/output, image input, a 128,000-token context window, 32,000-token maximum output, and a September 30, 2024 knowledge cutoff [Model reference](https://developers.openai.com/api/docs/models/gpt-realtime-2.1).

## Operating boundaries

Function calling is supported; Structured Outputs and fine-tuning are not documented as supported for this model. Higher reasoning effort can increase latency and output-token use. [Model reference](https://developers.openai.com/api/docs/models/gpt-realtime-2.1).

Realtime event streaming is a session protocol; a generic streaming badge should not be used to deny streamed voice support. Browser sessions use server-created short-lived credentials, while application servers retain API keys and authorize tool actions [Realtime guide](https://developers.openai.com/api/docs/guides/realtime).

## Relations

- Producer: [OpenAI](../../../../../producers/sub/o/sub/openai/README.md).

## Official resources

- [gpt-realtime-2.1 model reference](https://developers.openai.com/api/docs/models/gpt-realtime-2.1).
- [Realtime guide](https://developers.openai.com/api/docs/guides/realtime).
- [Voice server controls](https://developers.openai.com/api/docs/guides/voice-server-controls).
- [API changelog](https://developers.openai.com/api/docs/changelog).
