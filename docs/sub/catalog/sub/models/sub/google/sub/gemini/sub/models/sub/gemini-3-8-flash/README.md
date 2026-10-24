# Gemini 3.8 Flash

Stable provider-hosted text-output model served as gemini-3.8-flash; multimedia input does not imply media generation or a Live API model.

## Relations

- Member of: [Gemini](../../../../)

## Official resources

- <https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash>
- <https://ai.google.dev/gemini-api/docs/function-calling>

## Source-scoped operating boundaries

- The current model supports function calls, code execution, caching, grounding, and structured outputs. Image/audio generation and Live API are unsupported; computer use is separately marked preview. [Model reference](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash).
- Thinking supports low, medium, and high; minimal returns an error. Use the version-specific model page because the generic latest-model guide now covers a newer generation. [Thinking configuration](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash).
- Model-generated tool requests require application validation and authorization before execution. A stable model release does not make every attached tool or preview capability production-ready. [Function-calling workflow](https://ai.google.dev/gemini-api/docs/function-calling).
