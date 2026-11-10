# Muse Voice Transcribe

Muse Voice Transcribe is Meta's released **audio-perception and speech-to-text model**. Meta documents real-time/streaming ASR, speaker diarization, endpointing and voice-activity detection, contextual or keyword biasing, and multilingual code-switching.

## Speech contract and limits

The documented model ID is `muse-voice-transcribe-1.0`, which identifies an access route rather than a different trained-model family. Its output is a transcript, **not speech synthesis or a speech-to-speech conversation**. Diarization labels are speaker turns or clusters, not real-world identity verification. Do not assume unsupported features such as emotion detection, sound-event recognition or word timestamps.

Supported languages, endpoints, rate limits, pricing and hosted availability are freshness-sensitive. Evaluate transcription and speaker attribution on representative audio and verify the current API contract.

## Family and official sources

- [Muse family](../../../../)
- [Meta model announcement](https://research.meta.ai/blog/introducing-muse-voice-transcribe)
- [Official developer documentation](https://dev.meta.ai/models/muse-voice-transcribe)
