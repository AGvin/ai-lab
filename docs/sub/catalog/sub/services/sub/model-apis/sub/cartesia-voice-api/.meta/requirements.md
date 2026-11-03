# Documentation Requirements

## Requirements

- Identify Cartesia Voice API as the hosted developer interface for speech generation and supported transcription workflows operated by Cartesia, distinct from the Cartesia organization, Sonic and Ink underlying models, SDK packages and the separately presented Managed Agents platform.
- Preserve grounded API examples: the [REST TTS Bytes endpoint](https://docs.cartesia.ai/api-reference/tts/bytes) documents `https://api.cartesia.ai/tts/bytes`, `Authorization: Bearer` and required `Cartesia-Version` headers, while the [TTS WebSocket](https://docs.cartesia.ai/api-reference/tts/websocket) has an additional session/stream protocol and supports a trusted-server API key or browser-suitable short-lived token. Do not assume one authentication or output contract fits every transport.
- Describe streaming TTS contexts, chunked responses and available real-time STT turn detection through supported endpoints, without hardcoding a model ID or benchmark latency as a permanently supported guarantee.
- Explain that Sonic, Ink, voices, SDKs and other audio models are related, separate model/client resources rather than duplicate frozen API-service candidates; other agent-building products do not become part of this service merely because the same provider offers them.
- Treat API version, model list, regional availability, pricing, concurrency, supported sample rates, languages, retention, and recording/data-processing terms as mutable. Check the current API reference and customer agreement before integration.
- Audio, speech recordings and cloned voices may contain personal, biometric or copyright-protected data. Require lawful consent/rights, secure key/token handling, restricted logs and data retention review. Never expose a long-lived API key in untrusted clients.
- Preserve one reciprocal `produced-by` / `produces` relation and a single Model APIs index entry.
- No authenticated speech request, uploaded audio, benchmark, verified model latency, privacy audit, full CI or whole-catalog clean pass is claimed.

## Validation

- [Overview](https://docs.cartesia.ai/get-started/overview), [REST TTS reference](https://docs.cartesia.ai/api-reference/tts/bytes), [TTS WebSocket](https://docs.cartesia.ai/api-reference/tts/websocket) and [real-time STT](https://docs.cartesia.ai/api-reference/stt/turns/websocket) support the scoped description.
- The producer and service links resolve and the materialized node appears exactly once in the Model APIs index.
