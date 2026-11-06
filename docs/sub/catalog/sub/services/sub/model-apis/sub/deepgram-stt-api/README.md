# Deepgram Speech-to-Text API

The **Deepgram Speech-to-Text API** transcribes prerecorded and streaming speech using Deepgram-hosted recognition models. It is a managed service, separate from its downloadable SDKs, voice-agent products, speech generation endpoints and individual model versions.

## REST and streaming

For prerecorded audio, Deepgram documents `POST https://api.deepgram.com/v1/listen` with `Authorization: Token <API_KEY>` or an appropriate temporary bearer token. Requests can reference remote media or upload supported local audio. Real-time transcription uses `wss://api.deepgram.com/v1/listen`, with a WebSocket handshake and streaming audio/results lifecycle. An HTTP request is not interchangeable with a live stream's framing, finalization or disconnection rules.

The available languages, diarization models, speaker options, output metadata, transcript accuracy and per-region concurrency depend on the current endpoint and model. Consult the actual [REST](https://developers.deepgram.com/reference/speech-to-text/listen-pre-recorded) or [WebSocket](https://developers.deepgram.com/reference/speech-to-text/listen-streaming) contract.

## Callback security and audio privacy

**As of October 27, 2026, the `dg-token` callback header is no longer a supported verification mechanism.** The [official change notice](https://developers.deepgram.com/changelog/2026/10/27) recommends Basic Auth for callback endpoints; speech-to-text also supports matching a secret returned in `extra` metadata. Use HTTPS, unique scoped credentials, careful secret handling and protected logs. Do not rely on the deprecated callback-header method or confuse callback verification with the authorization used to make API requests.

Audio, transcripts and speaker labels may expose personal and confidential information. Obtain appropriate recording permissions and consent, restrict key/token exposure, and review retention, regional processing and contractual rules before sending production recordings. No audio was transmitted, transcription generated or callback authentication tested for this entry.

## Official resources

- [STT getting started](https://developers.deepgram.com/docs/stt/getting-started)
- [Pre-recorded STT API](https://developers.deepgram.com/reference/speech-to-text/listen-pre-recorded)
- [Streaming STT API](https://developers.deepgram.com/reference/speech-to-text/listen-streaming)
- [October 27, 2026 callback security update](https://developers.deepgram.com/changelog/2026/10/27)
