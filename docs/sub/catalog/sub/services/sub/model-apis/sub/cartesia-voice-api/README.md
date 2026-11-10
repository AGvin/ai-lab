# Cartesia Voice API

**Cartesia Voice API** is a developer-facing hosted audio model service operated by [Cartesia](../../../../../producers/sub/c/sub/cartesia/). It exposes text-to-speech and speech-to-text capabilities through documented HTTP and WebSocket interfaces. The provider's Sonic and Ink model families, SDKs and Managed Agents are related resources with separate identities and lifecycles.

## API usage and transport boundary

The official [REST TTS Bytes example](https://docs.cartesia.ai/api-reference/tts/bytes) calls `https://api.cartesia.ai/tts/bytes`, authenticates using `Authorization: Bearer` and supplies the required `Cartesia-Version` header. The exact model ID, voice, format, and version are selected for the current endpoint, not assumed constant.

The [TTS WebSocket API](https://docs.cartesia.ai/api-reference/tts/websocket) supports streaming, context-based generation and audio chunks; its security schemes differ from the REST endpoint, including trusted-server API key and short-lived client tokens. [Realtime STT](https://docs.cartesia.ai/api-reference/stt/turns/websocket) supports turn-aware transcription. Do not interchange REST and WebSocket request bodies, token delivery, response framing or audio buffering without checking the contract.

## Production and data safety

Voice recordings, transcripts and cloned voices can contain personal or protected biometric and performance material. Obtain applicable rights and consent, limit collection and retention, secure credentials, and review vendor service agreements and upstream data-processing routes. Use short-lived client tokens instead of disclosing a permanent API key in a browser.

Availability, supported voices/models, quotas, formats, latency, prices and regions are mutable. This profile documents first-party contracts and does not claim an executed request, audited latency or legal certification.

## Relations

- Produced by: [Cartesia](../../../../../producers/sub/c/sub/cartesia/)

## Official resources

- [Cartesia developer overview](https://docs.cartesia.ai/get-started/overview)
- [TTS Bytes reference](https://docs.cartesia.ai/api-reference/tts/bytes)
- [TTS WebSocket reference](https://docs.cartesia.ai/api-reference/tts/websocket)
- [Real-time STT WebSocket](https://docs.cartesia.ai/api-reference/stt/turns/websocket)
