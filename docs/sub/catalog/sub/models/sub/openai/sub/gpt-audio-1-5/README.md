# GPT-Audio-1.5

GPT Audio 1.5 is OpenAI’s `gpt-audio-1.5` model for audio input and output through Chat Completions. It was released in February 2026.

## Profile

The API profile lists text and audio input/output, a 128,000-token context window, 16,384-token maximum output, and a September 30, 2024 knowledge cutoff [Model reference](https://developers.openai.com/api/docs/models/gpt-audio-1.5).

## Operating boundaries

This is the REST Chat Completions audio surface, distinct from a Realtime session. Function calling and streaming are supported, while Structured Outputs are not listed as supported [Model reference](https://developers.openai.com/api/docs/models/gpt-audio-1.5).

Voice formats, transport, latency, and application permissions are deployment concerns. A generated tool call still requires the application’s authorization before execution.

## Relations

- Producer: [OpenAI](../../../../../producers/sub/o/sub/openai/README.md).

## Official resources

- [gpt-audio-1.5 model reference](https://developers.openai.com/api/docs/models/gpt-audio-1.5).
- [API changelog](https://developers.openai.com/api/docs/changelog).
