# Documentation Requirements

## Requirements

- Preserve the canonical identity, exact published names, and provenance described below.
- Render the complete current entity relation projection with descriptive, resolving links.
- Attribute provider capability claims and keep access, routing, pricing, and lifecycle facts source-scoped.

## Content specification

- Grok Voice Transcribe 2.0 is the Grok speech-to-text model released on September 17, 2026.
- The Speech to Text guide documents batch file transcription and real-time WebSocket streaming, including timestamps, multiple channels, and transcript formatting. The default model is grok-voice-transcribe-2.0. [Speech to Text guide](https://docs.x.ai/developers/model-capabilities/audio/speech-to-text).

## Source-scoped operating boundaries

- The earlier grok-voice-transcribe-1.0 reached end of life on October 2, 2026. Requests to that slug now route to version 2.0, so it is no longer an independently selectable older model. [API release notes](https://docs.x.ai/developers/release-notes).
- This is an audio-to-text model, not a speech-to-speech agent. Language, format, diarization, upload, and streaming controls are API-specific and must be checked in the task guide. [Speech to Text guide](https://docs.x.ai/developers/model-capabilities/audio/speech-to-text).

## Validation

- The reader matches the identity and all source-scoped boundaries above.
- Mutable aliases, serving modes, and application products are not duplicated as trained-model identities.

## Source evidence

- [Speech to Text guide](https://docs.x.ai/developers/model-capabilities/audio/speech-to-text).
- [API release notes](https://docs.x.ai/developers/release-notes).
