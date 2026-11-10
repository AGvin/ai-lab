# Documentation Requirements

## Requirements

- Identify Gemini 3.8 Flash TTS as the generally available `gemini-3.8-flash-tts` text-to-speech model released by Google on 2026-09-22.
- Preserve its text-to-audio identity, current flagship creative/studio-quality positioning, supported language/voice capabilities, and model-specific controls only while current first-party documentation supports them.
- Keep the Gemini API Voices endpoint, voice design/replication features, custom/prebuilt voice inventory, pricing, quotas, and hosted-service behavior as freshness-sensitive serving/product surfaces rather than separate trained-model identities.
- Do not generalize TTS capability to other Gemini 3.8 models.

## Validation

- Gemini 3.8 Flash TTS remains a concrete Gemini model distinct from Gemini 3.8 Flash-Lite TTS and text/multimodal Gemini 3.8 Flash.
- GA status remains source-backed.

## Verified identity and provenance

Stable text-to-speech model served as gemini-3.8-flash-tts, positioned by Google for expressive creative speech and complex dialogue; voice profiles and the Voices API are separate service assets.

## Source-scoped operating boundaries

- Input text is treated as the transcript to speak. Put speaker/style directions in speech_metadata, since inline directions may be read aloud. This text-to-audio endpoint is not a bidirectional Live model and does not expose tools or reasoning. [TTS request and capability reference](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts).
- Voice replication requires a 10–30-second reference recording and a separate prescribed consent recording from the same adult speaker. Stored voice profiles default to one-year retention; client-managed voice keys expire after seven days. These are service-specific identity and retention boundaries. [Voice replication requirements](https://ai.google.dev/gemini-api/docs/voice-replication).

## Source evidence

- <https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts>
- <https://ai.google.dev/gemini-api/docs/voice-replication>
