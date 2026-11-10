# Documentation Requirements

## Requirements

- Identify Muse Voice Transcribe as Meta's released speech-to-text/audio-perception model and preserve its concrete model identity separately from the Meta Model API service surface.
- Preserve source-backed streaming ASR, speaker diarization, endpointing, contextual/keyword biasing and multilingual/code-switching capabilities only with current first-party scope.
- Keep model ID aliases/endpoints, pricing, rate limits, supported-language counts and hosted availability freshness-sensitive.
- Do not infer speech synthesis, speech-to-speech conversation, word-level timestamps, emotion detection, or sound-event detection where Meta's current documentation does not provide them.

## Validation

- The model is not conflated with a complete voice-agent stack or hosted speech service.
- Diarization labels are not represented as real-world speaker identity.
