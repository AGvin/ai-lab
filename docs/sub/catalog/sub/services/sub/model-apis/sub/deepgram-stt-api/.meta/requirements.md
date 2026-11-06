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

## Follow-up original-source review — 2026-11-06 (no additional gate)

- Deepgram STT exposes prerecorded transcription through POST https://api.deepgram.com/v1/listen and live transcription through wss://api.deepgram.com/v1/listen. REST payloads, streaming transport, model-specific diarization/language/finalization and latency guarantees are not interchangeable; official endpoints accept an API token or supported temporary JWT.
- The original October 27, 2026 changelog withdraws dg-token callback-header verification. Treat callbacks as externally delivered sensitive transcription data: use documented Basic Auth for callback receivers or verify a secret in STT extra metadata where applicable, alongside consent, HTTPS and retention controls.
- Verified first-party source 1: https://developers.deepgram.com/reference/speech-to-text/listen-pre-recorded
- Verified first-party source 2: https://developers.deepgram.com/reference/speech-to-text/listen-streaming
- Verified first-party source 3: https://developers.deepgram.com/changelog/2026/10/27
- Scope: only current provider-documented hosted service identity and endpoint/version boundaries. No new metadata or entity, reader-repair credit, independent run, complete freshness/legal/security clearance, root-wide schema/cache/CI/render, clean pass or final delivery.
- Existing source gate was already accepted in Enrichment Batch 012; this follow-up adds **zero** identity, metadata or scoped-source acceptance credit. Avoid duplicate counting.
