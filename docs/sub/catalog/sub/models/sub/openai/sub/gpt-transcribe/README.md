# GPT-Transcribe

GPT Transcribe is OpenAI’s `gpt-transcribe` speech-to-text model for recorded audio and committed audio turns.

## Profile

The documented routes include completed audio files, streaming a file transcript, and committed turns over a Realtime WebSocket connection. Context, keywords, and multiple language hints can guide transcription [Speech-to-text guide](https://developers.openai.com/api/docs/guides/speech-to-text).

## Operating boundaries

Its output is a transcript rather than an assistant response. Keyword hints can introduce words that were not spoken, so lexical hints are not guaranteed constraints or evidence of what the recording contains [Speech-to-text guide](https://developers.openai.com/api/docs/guides/speech-to-text).

Committed-turn transcription and continuously emitted live transcript deltas have different event boundaries. Match completed transcripts to their item identifiers when handling multiple turns [Realtime transcription guide](https://developers.openai.com/api/docs/guides/realtime-transcription).

## Relations

- Producer: [OpenAI](../../../../../producers/sub/o/sub/openai/README.md).

## Official resources

- [gpt-transcribe model reference](https://developers.openai.com/api/docs/models/gpt-transcribe).
- [Speech-to-text guide](https://developers.openai.com/api/docs/guides/speech-to-text).
- [Realtime transcription guide](https://developers.openai.com/api/docs/guides/realtime-transcription).
