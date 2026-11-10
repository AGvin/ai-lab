# GPT-Realtime-2.1 Mini

`gpt-realtime-2.1-mini` is OpenAI’s concrete model for realtime voice applications. OpenAI describes mini as a distilled model for lower-cost, lower-latency voice use.

## Profile

The API profile lists text and audio input/output, image input, a 128,000-token context window, 32,000-token maximum output, and a September 30, 2024 knowledge cutoff [Model reference](https://developers.openai.com/api/docs/models/gpt-realtime-2.1-mini).

## Operating boundaries

Function calling is supported; Structured Outputs and fine-tuning are not documented as supported for this model. [Model reference](https://developers.openai.com/api/docs/models/gpt-realtime-2.1-mini).

Realtime event streaming is a session protocol; a generic streaming badge should not be used to deny streamed voice support. Browser sessions use server-created short-lived credentials, while application servers retain API keys and authorize tool actions [Realtime guide](https://developers.openai.com/api/docs/guides/realtime).

## Relations

- Producer: [OpenAI](../../../../../producers/sub/o/sub/openai/README.md).

## Official resources

- [gpt-realtime-2.1-mini model reference](https://developers.openai.com/api/docs/models/gpt-realtime-2.1-mini).
- [Realtime guide](https://developers.openai.com/api/docs/guides/realtime).
- [Voice server controls](https://developers.openai.com/api/docs/guides/voice-server-controls).
- [API changelog](https://developers.openai.com/api/docs/changelog).
