# GPT-4o Mini TTS

GPT-4o Mini TTS converts text to speech and supports instructions controlling delivery, such as tone and speaking speed. Its model identifier is `gpt-4o-mini-tts`.

## Profile

Its model role is text input to audio output through the Speech API [Model reference](https://developers.openai.com/api/docs/models/gpt-4o-mini-tts).

The model reference gives a maximum input length of 2,000 tokens [Model reference](https://developers.openai.com/api/docs/models/gpt-4o-mini-tts).

## Operating boundaries

The October 1, 2026 deprecation notice names gpt-4o-mini-tts-2025-03-20 and gpt-4o-mini-tts-2025-12-15 for API shutdown on January 6, 2027. The model reference also marks this model line deprecated. The notice recommends gpt-realtime-2.1-mini; moving to that model requires checking its Realtime interface rather than assuming Speech API compatibility [API deprecations](https://developers.openai.com/api/docs/deprecations).

Voice inventory, audio format, streaming, and delivery instructions are service controls. Provider speed and quality positioning does not guarantee the same result for every voice or workload [Text-to-speech guide](https://developers.openai.com/api/docs/guides/text-to-speech).

## Relations

- Producer: [OpenAI](../../../../../producers/sub/o/sub/openai/README.md).

## Official resources

- [gpt-4o-mini-tts model reference](https://developers.openai.com/api/docs/models/gpt-4o-mini-tts).
- [Text-to-speech guide](https://developers.openai.com/api/docs/guides/text-to-speech).
- [API deprecations](https://developers.openai.com/api/docs/deprecations).
