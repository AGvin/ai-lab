# GPT-4o Transcribe Diarize

GPT-4o Transcribe Diarize (`gpt-4o-transcribe-diarize`) is a transcription model with built-in speaker diarization. It remains documented here because its published API shutdown affects existing integrations.

## Profile

The API reference lists a 16,000-token context window, 2,000-token maximum output, and a June 1, 2024 knowledge cutoff [Model reference](https://developers.openai.com/api/docs/models/gpt-4o-transcribe-diarize).

## Operating boundaries

OpenAI announced deprecation on August 26, 2026 and scheduled API shutdown for February 26, 2027. The notice names gpt-transcribe and gpt-live-transcribe as replacements; that does not establish feature-for-feature migration parity [API deprecations](https://developers.openai.com/api/docs/deprecations).

Diarization is available through the Transcription API, not the Realtime API. Speaker segments and optional speaker references support attribution within a recording; they are not independent verification of a person’s identity [Speech-to-text guide](https://developers.openai.com/api/docs/guides/speech-to-text).

## Relations

- Producer: [OpenAI](../../../../../producers/sub/o/sub/openai/README.md).

## Official resources

- [gpt-4o-transcribe-diarize model reference](https://developers.openai.com/api/docs/models/gpt-4o-transcribe-diarize).
- [Speech-to-text guide](https://developers.openai.com/api/docs/guides/speech-to-text).
- [API deprecations](https://developers.openai.com/api/docs/deprecations).
