# Documentation Requirements

## Requirements

- Identify Gemini 3.8 Live Extended Thinking as the stable concrete `gemini-3.8-live-extended-thinking` model for high-reasoning real-time voice interactions.
- Preserve its background-reasoning and asynchronous-tool-call identity only to the extent supported by current first-party Live API documentation.
- Preserve the interaction-status lifecycle distinction from ordinary Live sessions when documenting integration behavior.
- Keep token limits, supported modalities, thinking controls, tool behavior, pricing, quotas, and API availability freshness-sensitive.
- Distinguish this model from Gemini 3.8 Live and from preview/legacy Live models.

## Validation

- Gemini 3.8 Live Extended Thinking remains a concrete Gemini model rather than an agent framework or service.
- Reasoning/tooling behavior is not generalized to other Gemini Live models.

## Verified identity and provenance

Stable Live audio model served as gemini-3.8-live-extended-thinking, with background reasoning and asynchronous tools; it is distinct from ordinary Gemini 3.8 Live.

## Source-scoped operating boundaries

- Only non-blocking asynchronous function calls are supported; blocking calls error. turnComplete does not mean the model is idle: clients must track interaction_status before treating background work as complete. [Extended Thinking integration](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-live-extended-thinking).
- Thinking supports low, medium, and high, but not minimal. Proactive audio cannot be disabled. Pending tool work needs explicit application authorization, cancellation, and completion handling. [Model-specific control boundary](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-live-extended-thinking).

## Source evidence

- <https://ai.google.dev/gemini-api/docs/models/gemini-3.8-live-extended-thinking>
- <https://ai.google.dev/gemini-api/docs/live-api/thinking>
