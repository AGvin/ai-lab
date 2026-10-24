# Gemini 3.8 Live

Stable audio-interaction model served as gemini-3.8-live through the Live API; Live Avatar is a serving capability rather than a separate model identity.

## Relations

- Member of: [Gemini](../../../../)

## Source-scoped operating boundaries

- Function calls default to asynchronous operation; blocking calls are optional. Applications must manage pending tool work and authorize side effects explicitly. [Live integration behavior](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-live).
- Proactive audio is always enabled and cannot be disabled. The thinking_level parameter is unsupported. Batch, caching, code execution, and structured outputs are not listed as supported. [Model-specific constraints](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-live).
- The model streams audio; text responses are available through output transcription. Keep recording, transcription, avatar display, and session handling scoped to the deployed Live application. [Input/output boundary](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-live).

## Official resources

- <https://ai.google.dev/gemini-api/docs/models/gemini-3.8-live>
- <https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-live-gemini-3-8-live-extended-thinking/>
- <https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-live-with-live-avatar/>
