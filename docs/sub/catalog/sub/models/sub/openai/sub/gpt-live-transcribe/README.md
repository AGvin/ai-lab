# GPT-Live-Transcribe

GPT Live Transcribe is OpenAI’s `gpt-live-transcribe` model for low-latency transcription of ongoing speech.

## Profile

It emits live transcript deltas and supports latency controls, contextual hints, keywords, and multiple language hints [Model reference](https://developers.openai.com/api/docs/models/gpt-live-transcribe).

## Operating boundaries

For this model, omit turn_detection or set it to null. server_vad and semantic_vad are not supported; the client commits turns explicitly [Realtime transcription guide](https://developers.openai.com/api/docs/guides/realtime-transcription).

Deltas are interim events. Completion order across turns is not guaranteed, so use item_id to associate completed text with the correct committed turn [Realtime transcription guide](https://developers.openai.com/api/docs/guides/realtime-transcription).

## Relations

- Producer: [OpenAI](../../../../../producers/sub/o/sub/openai/README.md).

## Official resources

- [gpt-live-transcribe model reference](https://developers.openai.com/api/docs/models/gpt-live-transcribe).
- [Realtime transcription guide](https://developers.openai.com/api/docs/guides/realtime-transcription).
- [Speech-to-text guide](https://developers.openai.com/api/docs/guides/speech-to-text).
