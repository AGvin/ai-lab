# Cartesia

Cartesia develops speech and conversational voice AI models and operates developer-facing APIs for text-to-speech, speech-to-text and voice-related workflows. Its official documentation describes Sonic speech generation, Ink transcription and separately operated Managed Agents.

## Provider and service boundary

**Cartesia Voice API** exposes hosted speech-model capabilities with documented REST and WebSocket interfaces. Model families and selectable voices do not each become an independent producer or API-service identity. Managed Agents is a related hosted workflow offering, not a synonym for the API or a separately accepted frozen candidate in this package.

Specific model identifiers, voice and language support, request transports, pricing and availability can change. Consult the current [API reference](https://docs.cartesia.ai/api-reference/tts/bytes) for the selected endpoint rather than relying on broad promotional latency or accuracy statements.

Generated speech, copied voices and transcribed audio may contain sensitive or rights-protected material. Obtain appropriate authorization and consent for source voices, limit access to credentials and check relevant retention, security and contractual terms before production use.

## Relations

- Produces: [Cartesia Voice API](../../../../../services/sub/model-apis/sub/cartesia-voice-api/)

## Official resources

- [Cartesia](https://cartesia.ai/)
- [Official overview](https://docs.cartesia.ai/get-started/overview)
- [TTS endpoint reference](https://docs.cartesia.ai/api-reference/tts/bytes)
