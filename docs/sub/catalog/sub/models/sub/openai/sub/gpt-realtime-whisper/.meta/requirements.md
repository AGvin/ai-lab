# Documentation Requirements

## Requirements

- Identify GPT-Realtime-Whisper as OpenAI's current streaming speech-to-text model for low-latency realtime transcription.
- Preserve current first-party-documented audio-input/text-output identity, 16k context, 2,000 maximum output, transcript streaming, and realtime-transcription-session role only at current release scope.
- Keep pricing-by-audio-duration, latency/accuracy tuning, supported transport/session behavior, rate limits, and event semantics freshness-sensitive.
- Keep GPT-Realtime-Whisper distinct from GPT-Live-Transcribe and GPT-Transcribe; current independent model IDs represent separate transcription choices.

## Validation

- The entity represents one trained transcription model rather than the Realtime transcription API.
- Current availability remains source-backed.

## Source-scoped operating boundaries

- The realtime transcription session produces transcript events. Its transport, buffering, and turn handling are service behavior that should be selected for the application’s transcription workflow [Realtime transcription guide](https://developers.openai.com/api/docs/guides/realtime-transcription).
- The name does not establish that this hosted model uses a particular downloadable Whisper checkpoint. The open-weight Whisper family and this API identity remain distinct.

## Source evidence

- [gpt-realtime-whisper model reference](https://developers.openai.com/api/docs/models/gpt-realtime-whisper).
- [Realtime transcription guide](https://developers.openai.com/api/docs/guides/realtime-transcription).
- [Whisper repository](https://github.com/openai/whisper).
