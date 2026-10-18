# GPT-Realtime-Whisper

GPT Realtime Whisper is OpenAI’s `gpt-realtime-whisper` speech-to-text model for live transcription.

## Profile

Its API profile documents tunable transcription latency, a 16,000-token context window, 2,000-token maximum output, and a September 30, 2024 knowledge cutoff [Model reference](https://developers.openai.com/api/docs/models/gpt-realtime-whisper).

## Operating boundaries

The realtime transcription session produces transcript events. Its transport, buffering, and turn handling are service behavior that should be selected for the application’s transcription workflow [Realtime transcription guide](https://developers.openai.com/api/docs/guides/realtime-transcription).

The name does not establish that this hosted model uses a particular downloadable Whisper checkpoint. The open-weight Whisper family and this API identity remain distinct.

## Relations

- Producer: [OpenAI](../../../../../producers/sub/o/sub/openai/README.md).

## Official resources

- [gpt-realtime-whisper model reference](https://developers.openai.com/api/docs/models/gpt-realtime-whisper).
- [Realtime transcription guide](https://developers.openai.com/api/docs/guides/realtime-transcription).
- [Whisper repository](https://github.com/openai/whisper).
