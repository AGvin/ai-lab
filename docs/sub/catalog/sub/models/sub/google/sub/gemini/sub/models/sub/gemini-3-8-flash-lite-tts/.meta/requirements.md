# Documentation Requirements

## Requirements

- Identify Gemini 3.8 Flash-Lite TTS as the generally available `gemini-3.8-flash-lite-tts` text-to-speech model released by Google on 2026-09-22.
- Preserve its fast/cost-efficient high-throughput TTS and real-time voice-agent-cascade positioning as current Google guidance rather than an independent AI Lab ranking.
- Keep supported languages, voice inventory, latency/quality guidance, pricing, quotas, API Voices features, and hosted-service behavior freshness-sensitive.
- Preserve its replacement relationship to the earlier `gemini-3.1-flash-tts-preview` only as current lifecycle guidance rather than collapsing the two model identities.

## Validation

- Gemini 3.8 Flash-Lite TTS remains a concrete Gemini model distinct from Gemini 3.8 Flash TTS.
- GA status remains source-backed.

## Verified identity and provenance

Stable text-to-speech model served as gemini-3.8-flash-lite-tts, positioned by Google for high-volume speech generation and cascaded voice agents; voice profiles and the Voices API are separate service assets.

## Source-scoped operating boundaries

- Input text is treated as the transcript to speak. Put speaker/style directions in speech_metadata, since inline directions may be read aloud. This text-to-audio endpoint is not a bidirectional Live model and does not expose tools or reasoning. [TTS request and capability reference](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts).
- Voice replication requires a 10–30-second reference recording and a separate prescribed consent recording from the same adult speaker. Stored voice profiles default to one-year retention; client-managed voice keys expire after seven days. These are service-specific identity and retention boundaries. [Voice replication requirements](https://ai.google.dev/gemini-api/docs/voice-replication).

## Source evidence

- <https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts>
- <https://ai.google.dev/gemini-api/docs/voice-replication>
