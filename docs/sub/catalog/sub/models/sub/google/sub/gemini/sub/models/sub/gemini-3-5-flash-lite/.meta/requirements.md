# Documentation Requirements

## Requirements

- Identify Gemini 3.5 Flash-Lite as Google's stable low-latency/cost-efficient Gemini model, generally available since 2026-07-21.
- Preserve its source-backed positioning for high-volume automation and subagent workloads without turning provider positioning into an independent ranking.
- Keep API pricing, rate limits, routing, and availability freshness-sensitive.

## Validation

- Current GA status is not confused with earlier preview routes.
- The model is not collapsed into Gemini 3.5 Flash or later 3.6/3.7/3.8 Flash identities.

## Verified identity and provenance

Stable text-output Gemini model served as gemini-3.5-flash-lite; Google's high-volume and latency-sensitive positioning does not define a separate agent product.

## Source-scoped operating boundaries

- The model accepts text, images, video, audio, and PDFs with 1,048,576 input and 65,536 output token limits. It supports functions, structured outputs, caching, and grounding; it does not generate images/audio or provide Live API sessions. [Model reference](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite).
- Computer use remains a preview feature even though the model is stable. Applications must validate and authorize requested external actions. [Capability status](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite) · [Function-calling workflow](https://ai.google.dev/gemini-api/docs/function-calling).

## Source evidence

- <https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite>
- <https://ai.google.dev/gemini-api/docs/function-calling>
