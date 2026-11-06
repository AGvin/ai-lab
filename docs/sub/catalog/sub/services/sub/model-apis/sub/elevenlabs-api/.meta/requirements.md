# Documentation Requirements

## Requirements

- Identify ElevenLabs API / ElevenAPI as the hosted programmatic interface provided by ElevenLabs, not the producer itself, one permanent model ID, an installable open-source model or the full ElevenCreative/ElevenAgents UI platforms.
- Explain supported categories at a source-scoped level: speech synthesis, speech-to-text, streaming/audio, supported voice and agent resources. Every endpoint/model combination has its own permissions, limits and modality-specific contract; do not imply uniform feature coverage.
- Verify the vendor's API key authentication: `xi-api-key` request header and documented `https://api.elevenlabs.io/v1` API path. The official authentication guidance offers scoped keys, credit limits and IP allowlisting; secrets are never embedded in public client-side applications. Some endpoints use narrowly scoped temporary tokens rather than exposing a long-lived key.
- Streaming can use different transports and buffering semantics; do not present synchronous REST, chunked streaming, WebSocket and real-time agent interfaces as interchangeable. Record the exact chosen contract when implementing an integration.
- Treat models, voices, pricing, credit units, quotas, service guarantees, supported regions and data retention/processing as version- and customer-plan-sensitive. This scoped profile is not a complete freshness or contract audit.
- Voice recordings, identity cloning, transcripts and other audio data may be biometric, personal or copyright-protected. Obtain rights/consent for input, secure keys and output, control access and review applicable retention and provider data-processing terms.
- Maintain reciprocal `produced-by` / `produces` relation with `catalog/producers/e/elevenlabs`; index the service as one child of Model APIs. Do not duplicate every SDK or model as another canonical service.
- No authenticated API request, runtime audio generation, paid usage, performance validation, full privacy/license review, full CI or whole-catalog clean-pass claim.

## Validation

- [API introduction](https://elevenlabs.io/docs/api-reference/introduction), [authentication](https://elevenlabs.io/docs/api-reference/authentication) and [streaming](https://elevenlabs.io/docs/api-reference/streaming) support the listed bounded interfaces.
- Producer inverse, category index and reader relative links resolve without unsupported extra identities.
