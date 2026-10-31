# Documentation Requirements

## Requirements

- Identify GPT-Live-1 as OpenAI's released full-duplex voice model introduced in ChatGPT and made available in the API on 2026-09-10.
- Preserve its source-backed role as the front-end conversational voice layer that can listen and speak concurrently and delegate deeper reasoning/actions to a paired backend model and agent harness.
- Keep API pricing, voice inventory, transport support, telephony integration, and product-plan availability as mutable access/deployment facts rather than intrinsic model identity.
- Preserve benchmark claims only with their named benchmark, evaluation date, and source context.

## Validation

- GPT-Live-1 is not described as the backend reasoning model used by a complete voice agent.
- API GA status is distinguished from the model's earlier ChatGPT rollout.
- Mutable voice/API features are freshness-scoped.

## Source-scoped operating boundaries

- The API release became generally available on September 10, 2026. Backend inference is separate from the voice session, and access and capacity are determined by the service [API changelog](https://developers.openai.com/api/docs/changelog).
- Keep credentials, business rules, and action authorization on the server. A delegated action or sideband connection does not itself authorize execution [Voice server controls](https://developers.openai.com/api/docs/guides/voice-server-controls).

## Source evidence

- [gpt-live-1 model reference](https://developers.openai.com/api/docs/models/gpt-live-1).
- [GPT-Live system card](https://deploymentsafety.openai.com/gpt-live).
- [GPT-Live API guide](https://developers.openai.com/api/docs/guides/live).
- [API changelog](https://developers.openai.com/api/docs/changelog).
- [Voice server controls](https://developers.openai.com/api/docs/guides/voice-server-controls).
