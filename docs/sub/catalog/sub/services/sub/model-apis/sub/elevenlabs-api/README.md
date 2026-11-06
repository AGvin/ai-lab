# ElevenLabs API

**ElevenLabs API**, also called **ElevenAPI**, is the hosted model-access and audio-processing interface operated by [ElevenLabs](../../../../../producers/sub/e/sub/elevenlabs/). It supports documented speech synthesis and recognition, streaming, voice resources and other available audio/agent workflows.

## Authentication and integration

The [first-party authentication guide](https://elevenlabs.io/docs/api-reference/authentication) uses the `xi-api-key` HTTP header for authenticated API requests. For example, the documented models endpoint is `https://api.elevenlabs.io/v1/models`. Keep a long-lived key on a trusted server or in a secret manager; do not include it in browser bundles. Scope keys by supported endpoint permissions, usage quota or IP restrictions, and use endpoint-specific limited tokens where available.

REST APIs, streaming speech endpoints, WebSockets and agent session interfaces can have different request formats and capabilities. Choose a supported model and voice/endpoint combination using the current reference; do not infer universal access or exact latency from a generic example. SDKs and the ElevenAgents application are related interfaces, not separate versions of this canonical API service.

## Data and rights

Treat source audio, transcripts and cloned voices as potentially sensitive or legally protected. Obtain permission and consent as appropriate, limit retained recordings and response logs, and review provider processing, usage charges and contractual requirements. Pricing, supported models, languages, quotas, voice-license terms and available regions can change.

This catalog entry documents vendor interfaces only; no API credentials, generated speech, live audio stream or production integration were exercised.

## Relations

- Produced by: [ElevenLabs](../../../../../producers/sub/e/sub/elevenlabs/)

## Official resources

- [API overview](https://elevenlabs.io/docs/api-reference/introduction)
- [Authentication and API keys](https://elevenlabs.io/docs/api-reference/authentication)
- [Streaming audio API](https://elevenlabs.io/docs/api-reference/streaming)
