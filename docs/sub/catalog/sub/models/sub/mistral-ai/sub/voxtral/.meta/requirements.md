# Documentation Requirements

## Requirements

- Render the standard entity-relations block from the validated current-entity projection.

- Identify Voxtral as Mistral AI's speech/audio model family spanning transcription and text-to-speech workloads.
- Materialize Voxtral Mini Transcribe V2, Voxtral Realtime, and Voxtral 4B TTS separately because modality direction, latency model, weight availability, and licensing differ materially.
- Keep Mistral Studio audio playground and hosted endpoint pricing outside intrinsic model identity.
- Treat language support, diarization, timestamping, latency, voice/reference assets, licenses, API aliases, and runtime support as freshness-sensitive.

## Validation

- Producer provenance resolves to Mistral AI.
- ASR and TTS members are not conflated simply because they share the Voxtral brand.

## Source-backed profile

- Required reader orientation: Voxtral is Mistral AI’s audio-model family spanning audio understanding, transcription and speech generation.
- Preserve this model-scoped fact: Its represented models have different input/output directions and operating contracts: Small understands audio, Mini Transcribe handles offline transcription, Realtime streams transcription, and TTS generates speech. [Voxtral Small model card](https://docs.mistral.ai/models/voxtral-small-25-07) [Voxtral Mini Transcribe 2 model card](https://docs.mistral.ai/models/voxtral-mini-transcribe-26-02) [Voxtral Realtime model card](https://docs.mistral.ai/models/voxtral-mini-transcribe-realtime-26-02) [Voxtral TTS model card](https://docs.mistral.ai/models/voxtral-tts-26-03)

## Operational and interpretation boundaries

- Explain this boundary: Do not transfer diarization, system-prompt support, licensing or weight availability between members. A transcription label or synthesized voice is not proof of a speaker’s identity.

- Keep source-reported capabilities distinct from application-level correctness, authorization and measured deployment performance.
