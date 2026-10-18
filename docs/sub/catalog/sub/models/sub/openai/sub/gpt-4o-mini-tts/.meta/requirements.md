# Documentation Requirements

## Requirements

- Identify GPT-4o Mini TTS as OpenAI's text-to-speech model powered by GPT-4o Mini.
- Preserve text-input/audio-output identity, 2,000-token maximum input, promptable speaking-style controls, and current speech-generation role only while supported by first-party documentation.
- Preserve current lifecycle: OpenAI deprecated the `gpt-4o-mini-tts-2025-03-20` and `gpt-4o-mini-tts-2025-12-15` snapshots on 2026-10-01 and scheduled API shutdown for 2027-01-06; keep replacement guidance freshness-sensitive.
- Keep built-in voice inventory, recommended voices, output formats, pricing, streaming behavior, language guidance, API endpoints, aliases/snapshots, and rate limits freshness-sensitive.
- Keep GPT-4o Mini TTS distinct from the GPT-4o Mini text model and from realtime conversational/audio models.

## Validation

- The entity represents one trained speech-generation model rather than the Audio API speech endpoint.
- Snapshot lifecycle is explicit and aliases/snapshots are not duplicated as peer model identities.
- Voice/product availability is not treated as intrinsic model identity.

## Source-scoped operating boundaries

- The October 1, 2026 deprecation notice names gpt-4o-mini-tts-2025-03-20 and gpt-4o-mini-tts-2025-12-15 for API shutdown on January 6, 2027. The model reference also marks this model line deprecated. The notice recommends gpt-realtime-2.1-mini; moving to that model requires checking its Realtime interface rather than assuming Speech API compatibility [API deprecations](https://developers.openai.com/api/docs/deprecations).
- Voice inventory, audio format, streaming, and delivery instructions are service controls. Provider speed and quality positioning does not guarantee the same result for every voice or workload [Text-to-speech guide](https://developers.openai.com/api/docs/guides/text-to-speech).

## Source evidence

- [gpt-4o-mini-tts model reference](https://developers.openai.com/api/docs/models/gpt-4o-mini-tts).
- [Text-to-speech guide](https://developers.openai.com/api/docs/guides/text-to-speech).
- [API deprecations](https://developers.openai.com/api/docs/deprecations).
