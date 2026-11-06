# Documentation Requirements

## Requirements

- Render the standard entity-relations block from the validated current-entity projection.

- Identify Voxtral Mini Transcribe V2 as the batch-transcription member of Voxtral Transcribe 2.
- Keep diarization, context biasing, word timestamps, language coverage, hosted pricing, and benchmark claims current-source scoped.

## Validation

- Membership resolves to Voxtral.

## Source-backed profile

- Required reader orientation: Voxtral Mini Transcribe V2 is the offline transcription model also named Voxtral Mini Transcribe 2 in Mistral’s February 2026 model catalog.
- Preserve this model-scoped fact: The GA Premier release `voxtral-mini-2602` is optimized for transcription only. It supports speaker diarization, vocabulary biasing and word or segment timestamps through the transcription interface. [Voxtral Mini Transcribe 2 model card](https://docs.mistral.ai/models/voxtral-mini-transcribe-26-02) [Offline and realtime transcription contracts](https://docs.mistral.ai/studio/audio/speech_to_text) [Offline transcription and timestamp options](https://docs.mistral.ai/studio/audio/speech_to_text/offline_transcription)

## Operational and interpretation boundaries

- Explain this boundary: The offline transcription guide currently makes `timestamp_granularities` incompatible with an explicit `language` parameter. Check the request combination before submitting audio. [Offline transcription and timestamp options](https://docs.mistral.ai/studio/audio/speech_to_text/offline_transcription)
- Explain this boundary: Mistral reports that overlapping speech typically yields a transcript of one speaker. Context biasing is optimized for English; other-language biasing remains experimental. [Voxtral Transcribe 2 release](https://mistral.ai/news/voxtral-transcribe-2/)
- Explain this boundary: Speaker labels separate speakers in a recording; they are not verified identities. Transcription and timestamp estimates need checking against the audio when used as evidence. The offline model is not the separately released Realtime checkpoint.

- Keep source-reported capabilities distinct from application-level correctness, authorization and measured deployment performance.
