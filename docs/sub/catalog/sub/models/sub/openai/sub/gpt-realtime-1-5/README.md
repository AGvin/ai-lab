# GPT-Realtime-1.5

`gpt-realtime-1.5` is OpenAI’s concrete model for realtime voice applications. GPT Realtime 1.5 is the realtime audio model released by OpenAI in February 2026.

## Profile

The API profile lists text and audio input/output, image input, a 32,000-token context window, 4,096-token maximum output, and a September 30, 2024 knowledge cutoff [Model reference](https://developers.openai.com/api/docs/models/gpt-realtime-1.5).

## Operating boundaries

Function calling is supported; Structured Outputs and fine-tuning are not documented as supported for this model. [Model reference](https://developers.openai.com/api/docs/models/gpt-realtime-1.5).

Realtime event streaming is a session protocol; a generic streaming badge should not be used to deny streamed voice support. Browser sessions use server-created short-lived credentials, while application servers retain API keys and authorize tool actions [Realtime guide](https://developers.openai.com/api/docs/guides/realtime).

## Relations

- Producer: [OpenAI](../../../../../producers/sub/o/sub/openai/README.md).

## Official resources

- [gpt-realtime-1.5 model reference](https://developers.openai.com/api/docs/models/gpt-realtime-1.5).
- [Realtime guide](https://developers.openai.com/api/docs/guides/realtime).
- [Voice server controls](https://developers.openai.com/api/docs/guides/voice-server-controls).
- [API changelog](https://developers.openai.com/api/docs/changelog).
