# GPT-4o Mini Transcribe

GPT-4o Mini Transcribe (`gpt-4o-mini-transcribe`) is a smaller transcription model powered by GPT-4o mini. It remains documented here because its published API shutdown affects existing integrations.

## Profile

The API reference lists a 16,000-token context window, 2,000-token maximum output, and a June 1, 2024 knowledge cutoff [Model reference](https://developers.openai.com/api/docs/models/gpt-4o-mini-transcribe).

## Operating boundaries

OpenAI announced deprecation on August 26, 2026 and scheduled API shutdown for February 26, 2027. The notice names gpt-transcribe and gpt-live-transcribe as replacements; that does not establish feature-for-feature migration parity [API deprecations](https://developers.openai.com/api/docs/deprecations).

This specialized speech-to-text identity is distinct from the general-purpose GPT-4o or GPT-4o mini chat model. File transcription and supported transcript streaming remain task-specific API behavior [Speech-to-text guide](https://developers.openai.com/api/docs/guides/speech-to-text).

The earlier gpt-4o-mini-transcribe-2025-03-20 snapshot has a separate January 20, 2027 shutdown date; migration deadlines must follow the exact identifier in use [API deprecations](https://developers.openai.com/api/docs/deprecations).

## Relations

- Producer: [OpenAI](../../../../../producers/sub/o/sub/openai/README.md).

## Official resources

- [gpt-4o-mini-transcribe model reference](https://developers.openai.com/api/docs/models/gpt-4o-mini-transcribe).
- [Speech-to-text guide](https://developers.openai.com/api/docs/guides/speech-to-text).
- [API deprecations](https://developers.openai.com/api/docs/deprecations).
