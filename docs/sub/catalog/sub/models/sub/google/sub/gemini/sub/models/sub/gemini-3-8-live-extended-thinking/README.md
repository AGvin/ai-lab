# Gemini 3.8 Live Extended Thinking

Stable Live audio model served as gemini-3.8-live-extended-thinking, with background reasoning and asynchronous tools; it is distinct from ordinary Gemini 3.8 Live.

## Relations

- Member of: [Gemini](../../../../)

## Source-scoped operating boundaries

- Only non-blocking asynchronous function calls are supported; blocking calls error. turnComplete does not mean the model is idle: clients must track interaction_status before treating background work as complete. [Extended Thinking integration](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-live-extended-thinking).
- Thinking supports low, medium, and high, but not minimal. Proactive audio cannot be disabled. Pending tool work needs explicit application authorization, cancellation, and completion handling. [Model-specific control boundary](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-live-extended-thinking).

## Official resources

- <https://ai.google.dev/gemini-api/docs/models/gemini-3.8-live-extended-thinking>
- <https://ai.google.dev/gemini-api/docs/live-api/thinking>
- <https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-live-gemini-3-8-live-extended-thinking/>
