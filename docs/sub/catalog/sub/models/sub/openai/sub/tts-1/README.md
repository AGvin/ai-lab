# TTS-1

TTS-1 is OpenAI’s text-to-speech model positioned for lower-latency speech generation. Its model identifier is `tts-1`.

## Profile

Its model role is text input to audio output through the Speech API [Model reference](https://developers.openai.com/api/docs/models/tts-1).

## Operating boundaries

OpenAI deprecated this model on October 1, 2026 and scheduled API shutdown for January 6, 2027. The notice recommends gpt-realtime-2.1-mini; moving to that model requires checking its Realtime interface rather than assuming Speech API compatibility [API deprecations](https://developers.openai.com/api/docs/deprecations).

Voice inventory, audio format, streaming, and delivery instructions are service controls. Provider speed and quality positioning does not guarantee the same result for every voice or workload [Text-to-speech guide](https://developers.openai.com/api/docs/guides/text-to-speech).

## Relations

- Producer: [OpenAI](../../../../../producers/sub/o/sub/openai/README.md).

## Official resources

- [tts-1 model reference](https://developers.openai.com/api/docs/models/tts-1).
- [Text-to-speech guide](https://developers.openai.com/api/docs/guides/text-to-speech).
- [API deprecations](https://developers.openai.com/api/docs/deprecations).
