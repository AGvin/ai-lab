# GPT-Realtime-Translate

GPT Realtime Translate is OpenAI’s `gpt-realtime-translate` model for interpreting live speech into translated audio and transcript deltas.

## Profile

The API profile lists a 16,000-token context window, 2,000-token maximum output, and a September 30, 2024 knowledge cutoff [Model reference](https://developers.openai.com/api/docs/models/gpt-realtime-translate).

## Operating boundaries

It uses the dedicated /v1/realtime/translations session. The model continuously interprets incoming audio; it does not use the assistant response lifecycle or tool-calling behavior of a standard voice-agent session [Realtime translation guide](https://developers.openai.com/api/docs/guides/realtime-translation).

A browser receives a short-lived client secret created by a server. Standard API credentials stay on the server [Realtime translation guide](https://developers.openai.com/api/docs/guides/realtime-translation).

## Relations

- Producer: [OpenAI](../../../../../producers/sub/o/sub/openai/README.md).

## Official resources

- [gpt-realtime-translate model reference](https://developers.openai.com/api/docs/models/gpt-realtime-translate).
- [Realtime translation guide](https://developers.openai.com/api/docs/guides/realtime-translation).
