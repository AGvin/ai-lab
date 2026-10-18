# Voxtral Mini 4B Realtime 2602

Voxtral Mini 4B Realtime 2602 is Mistral AI’s February 2026 streaming speech-to-text checkpoint.

## Translations

- English

## Relations

- Family: [Voxtral](../../../../)

## Model profile

The Apache 2.0 BF16 release uses a causal audio encoder and configurable transcription delay. Mistral recommends temperature 0 and a 480 ms delay in its model-card setup. [Voxtral Realtime weights and streaming limits](https://huggingface.co/mistralai/Voxtral-Mini-4B-Realtime-2602)

Its hosted model identifier is `voxtral-mini-transcribe-realtime-2602`. [Voxtral Realtime model card](https://docs.mistral.ai/models/voxtral-mini-transcribe-realtime-26-02)

## Operational boundaries

Realtime transcription currently cannot be combined with `diarize`. Offline speaker labels must not be assumed for this interface. [Realtime transcription limitations](https://docs.mistral.ai/studio/audio/speech_to_text/realtime_transcription)

Streaming attention does not provide an unlimited service session: runtime allocations and maximum model length still bound a deployment. Delay settings describe an accuracy/latency tradeoff, not guaranteed end-to-end latency. [Voxtral Realtime weights and streaming limits](https://huggingface.co/mistralai/Voxtral-Mini-4B-Realtime-2602)

## Official resources

- [Voxtral Realtime weights and streaming limits](https://huggingface.co/mistralai/Voxtral-Mini-4B-Realtime-2602)
- [Voxtral Transcribe 2 release](https://mistral.ai/news/voxtral-transcribe-2/)
- [Voxtral Realtime model card](https://docs.mistral.ai/models/voxtral-mini-transcribe-realtime-26-02)
- [Realtime transcription limitations](https://docs.mistral.ai/studio/audio/speech_to_text/realtime_transcription)
