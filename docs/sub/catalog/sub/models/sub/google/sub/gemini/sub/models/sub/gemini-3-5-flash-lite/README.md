# Gemini 3.5 Flash-Lite

Stable text-output Gemini model served as gemini-3.5-flash-lite; Google's high-volume and latency-sensitive positioning does not define a separate agent product.

## Relations

- Member of: [Gemini](../../../../)

## Scope and boundaries

- API pricing, rate limits, routing, and availability remain freshness-sensitive.

## Official resources

- <https://ai.google.dev/gemini-api/docs/changelog>
- <https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite>
- <https://ai.google.dev/gemini-api/docs/function-calling>

## Source-scoped operating boundaries

- The model accepts text, images, video, audio, and PDFs with 1,048,576 input and 65,536 output token limits. It supports functions, structured outputs, caching, and grounding; it does not generate images/audio or provide Live API sessions. [Model reference](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite).
- Computer use remains a preview feature even though the model is stable. Applications must validate and authorize requested external actions. [Capability status](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite) · [Function-calling workflow](https://ai.google.dev/gemini-api/docs/function-calling).
