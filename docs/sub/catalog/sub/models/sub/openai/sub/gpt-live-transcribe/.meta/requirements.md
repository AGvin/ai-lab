# Documentation Requirements

## Requirements

- Identify GPT-Live-Transcribe as OpenAI's current low-latency streaming speech-to-text model for live audio.
- Preserve audio-input/text-output identity, transcript-delta streaming, tunable latency, keyword hints, multilingual hints, and current realtime-transcription-session role only while supported by first-party documentation.
- Keep supported languages, transport/session behavior, pricing, limits, event schemas, and endpoint requirements freshness-sensitive.
- Keep GPT-Live-Transcribe distinct from GPT-Live-1 conversational voice and GPT-Transcribe file/committed-turn transcription.

## Validation

- The entity represents one trained transcription model rather than the Realtime transcription API.
- Current recommended-live-transcription status remains source-scoped.

## Source-scoped operating boundaries

- For this model, omit turn_detection or set it to null. server_vad and semantic_vad are not supported; the client commits turns explicitly [Realtime transcription guide](https://developers.openai.com/api/docs/guides/realtime-transcription).
- Deltas are interim events. Completion order across turns is not guaranteed, so use item_id to associate completed text with the correct committed turn [Realtime transcription guide](https://developers.openai.com/api/docs/guides/realtime-transcription).

## Source evidence

- [gpt-live-transcribe model reference](https://developers.openai.com/api/docs/models/gpt-live-transcribe).
- [Realtime transcription guide](https://developers.openai.com/api/docs/guides/realtime-transcription).
- [Speech-to-text guide](https://developers.openai.com/api/docs/guides/speech-to-text).
