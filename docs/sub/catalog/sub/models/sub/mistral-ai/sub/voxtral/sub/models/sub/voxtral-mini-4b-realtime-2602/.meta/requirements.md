# Documentation Requirements

## Requirements

- Render the standard entity-relations block from the validated current-entity projection.

- Identify this checkpoint as the Apache-2.0 open-weight live-transcription member of Voxtral Transcribe 2.
- Keep latency, streaming behavior, language coverage, context, runtime support, and benchmark claims source-scoped.

## Validation

- Membership resolves to Voxtral.

## Source-backed profile

- Required reader orientation: Voxtral Mini 4B Realtime 2602 is Mistral AI’s February 2026 streaming speech-to-text checkpoint.
- Preserve this model-scoped fact: The Apache 2.0 BF16 release uses a causal audio encoder and configurable transcription delay. Mistral recommends temperature 0 and a 480 ms delay in its model-card setup. [Voxtral Realtime weights and streaming limits](https://huggingface.co/mistralai/Voxtral-Mini-4B-Realtime-2602)
- Preserve this model-scoped fact: Its hosted model identifier is `voxtral-mini-transcribe-realtime-2602`. [Voxtral Realtime model card](https://docs.mistral.ai/models/voxtral-mini-transcribe-realtime-26-02)

## Operational and interpretation boundaries

- Explain this boundary: Realtime transcription currently cannot be combined with `diarize`. Offline speaker labels must not be assumed for this interface. [Realtime transcription limitations](https://docs.mistral.ai/studio/audio/speech_to_text/realtime_transcription)
- Explain this boundary: Streaming attention does not provide an unlimited service session: runtime allocations and maximum model length still bound a deployment. Delay settings describe an accuracy/latency tradeoff, not guaranteed end-to-end latency. [Voxtral Realtime weights and streaming limits](https://huggingface.co/mistralai/Voxtral-Mini-4B-Realtime-2602)

- Keep source-reported capabilities distinct from application-level correctness, authorization and measured deployment performance.
