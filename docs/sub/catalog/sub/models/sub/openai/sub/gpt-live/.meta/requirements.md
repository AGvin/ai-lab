# Documentation Requirements

## Requirements

- Identify GPT-Live as OpenAI's model family for natural full-duplex voice interaction.
- Keep the front-end conversational voice model identity distinct from backend reasoning models, agent harnesses, ChatGPT Voice product behavior, and API transport/runtime features.
- Link the canonical OpenAI producer and materialized concrete GPT-Live models.
- Preserve modality, full-duplex behavior, interruption handling, and delegation boundaries only where current first-party sources support them.

## Validation

- GPT-Live is not conflated with the Realtime API or ChatGPT Voice as product/service identities.
- Backend model delegation is not represented as intrinsic reasoning performed by GPT-Live itself.
- Model-specific availability, pricing, and feature details remain scoped to concrete releases.

## Source-scoped operating boundaries

- GPT-Live-1 became generally available in the API in September 2026. That release does not establish the same API availability for GPT-Live-1 mini [API changelog](https://developers.openai.com/api/docs/changelog).
- Session transport, duration billing, backend selection, and concurrent-session limits belong to the service. Backend tool execution requires application authorization and server-held credentials [GPT-Live guide](https://developers.openai.com/api/docs/guides/live).

## Source evidence

- [GPT-Live system card](https://deploymentsafety.openai.com/gpt-live).
- [GPT-Live API guide](https://developers.openai.com/api/docs/guides/live).
- [API changelog](https://developers.openai.com/api/docs/changelog).
- [Voice server controls](https://developers.openai.com/api/docs/guides/voice-server-controls).
