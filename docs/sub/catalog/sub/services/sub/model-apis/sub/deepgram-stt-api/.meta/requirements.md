# Documentation Requirements

## Requirements

- Define Deepgram STT as the provider-hosted recognition service, not a local SDK, voice synthesizer, managed voice agent, underlying Nova model or Deepgram company profile. The frozen case is one hosted service identity.
- Ground prerecorded transcription in `POST https://api.deepgram.com/v1/listen` with `Authorization: Token <API_KEY>` and optional `Authorization: Bearer <JWT>`, and streaming in `wss://api.deepgram.com/v1/listen`. Both are documented first-party but not interchangeable request/response framing.
- Deepgram supports prerecorded input via hosted URL or uploaded media, real-time event streams and model-specific languages/features. Model version, diarization support, latency, stream finalization, API quotas, regions and prices are mutable; do not promise all features work with all models.
- Treat the [October 27, 2026 callback security change](https://developers.deepgram.com/changelog/2026/10/27) as material: the `dg-token` callback-header validation method is **no longer supported**. Recommend callback Basic Auth with an appropriately secret, authenticated HTTPS receiver; STT also documents matching a random `extra` metadata secret, with careful handling of request/response/log leakage. Do not claim those schemes authenticate all possible callback transports identically.
- Protect Deepgram long-lived API keys and use short-lived tokens for suitable client streams when the current SDK and provider endpoint support them. Audio and transcripts can contain personally identifying voices, sensitive conversations and regulated records; obtain applicable permissions/consent and apply retention/access and data residency controls.
- Avoid a speculative `produced-by` link to a missing standalone Deepgram producer node; first-party service docs establish the operator without accepting another frozen producer.
- No authenticated transcription, audio upload, WebSocket session, callback security penetration test, model accuracy benchmark, full privacy/contract audit, full CI or whole-catalog clean pass is claimed.

## Validation

- [STT overview](https://developers.deepgram.com/docs/stt/getting-started), [REST reference](https://developers.deepgram.com/reference/speech-to-text/listen-pre-recorded), [streaming reference](https://developers.deepgram.com/reference/speech-to-text/listen-streaming) and [October security changelog](https://developers.deepgram.com/changelog/2026/10/27) support documented scope.
- The Model APIs index links one canonical Deepgram STT service; no distinct developer SDK or model entity is added.
