# Gemini 3.8 Flash TTS

Stable text-to-speech model served as gemini-3.8-flash-tts, positioned by Google for expressive creative speech and complex dialogue; voice profiles and the Voices API are separate service assets.

## Relations

- Member of: [Gemini](../../../../)

## Source-scoped operating boundaries

- Input text is treated as the transcript to speak. Put speaker/style directions in speech_metadata, since inline directions may be read aloud. This text-to-audio endpoint is not a bidirectional Live model and does not expose tools or reasoning. [TTS request and capability reference](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts).
- Voice replication requires a 10–30-second reference recording and a separate prescribed consent recording from the same adult speaker. Stored voice profiles default to one-year retention; client-managed voice keys expire after seven days. These are service-specific identity and retention boundaries. [Voice replication requirements](https://ai.google.dev/gemini-api/docs/voice-replication).

## Official resources

- <https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts>
- <https://ai.google.dev/gemini-api/docs/changelog>
- <https://ai.google.dev/gemini-api/docs/voice-replication>
