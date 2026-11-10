# Documentation Requirements

## Requirements

- Identify GPT-Transcribe as OpenAI's current high-accuracy speech-to-text model for completed files, streamed file transcripts, and committed turns in Realtime sessions.
- Preserve audio-input/text-output identity plus current context/keyword/language-hint and detected-language behavior only while supported by first-party documentation.
- Keep file streaming, endpoint behavior, language support, pricing, rate limits, response formats, diarization interaction, and Realtime-session details freshness-sensitive.
- Keep GPT-Transcribe distinct from GPT-Live-Transcribe, which is optimized for low-latency transcript deltas from ongoing live audio.

## Validation

- The entity represents a trained transcription model rather than the transcription API.
- Replacement/deprecation guidance for older transcription models remains source-scoped.

## Source-scoped operating boundaries

- Its output is a transcript rather than an assistant response. Keyword hints can introduce words that were not spoken, so lexical hints are not guaranteed constraints or evidence of what the recording contains [Speech-to-text guide](https://developers.openai.com/api/docs/guides/speech-to-text).
- Committed-turn transcription and continuously emitted live transcript deltas have different event boundaries. Match completed transcripts to their item identifiers when handling multiple turns [Realtime transcription guide](https://developers.openai.com/api/docs/guides/realtime-transcription).

## Source evidence

- [gpt-transcribe model reference](https://developers.openai.com/api/docs/models/gpt-transcribe).
- [Speech-to-text guide](https://developers.openai.com/api/docs/guides/speech-to-text).
- [Realtime transcription guide](https://developers.openai.com/api/docs/guides/realtime-transcription).
