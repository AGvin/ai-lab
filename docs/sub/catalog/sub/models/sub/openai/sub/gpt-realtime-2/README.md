# GPT-Realtime-2

`gpt-realtime-2` is OpenAI’s concrete model for realtime voice applications. GPT Realtime 2 supports realtime speech interaction with reasoning and tool calling.

## Profile

The API profile lists text and audio input/output, image input, a 128,000-token context window, 32,000-token maximum output, and a September 30, 2024 knowledge cutoff [Model reference](https://developers.openai.com/api/docs/models/gpt-realtime-2).

## Operating boundaries

Function calling is supported; Structured Outputs and fine-tuning are not documented as supported for this model. Higher reasoning effort can increase latency and output-token use. [Model reference](https://developers.openai.com/api/docs/models/gpt-realtime-2).

Realtime event streaming is a session protocol; a generic streaming badge should not be used to deny streamed voice support. Browser sessions use server-created short-lived credentials, while application servers retain API keys and authorize tool actions [Realtime guide](https://developers.openai.com/api/docs/guides/realtime).

## Relations

- Producer: [OpenAI](../../../../../producers/sub/o/sub/openai/README.md).

## Official resources

- [gpt-realtime-2 model reference](https://developers.openai.com/api/docs/models/gpt-realtime-2).
- [Realtime guide](https://developers.openai.com/api/docs/guides/realtime).
- [Voice server controls](https://developers.openai.com/api/docs/guides/voice-server-controls).
- [API changelog](https://developers.openai.com/api/docs/changelog).
