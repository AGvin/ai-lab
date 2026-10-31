# Documentation Requirements

## Requirements

- Identify Gemini 3.8 Flash as the stable concrete `gemini-3.8-flash` model and preserve its September 2026 GA boundary.
- Preserve current provider-documented text/image/video/audio/PDF input, text output, 1,048,576-token input limit, 65,536-token output limit, and supported `low` / `medium` / `high` thinking levels.
- Attribute long-horizon software-engineering, autonomous-agent, and enterprise-workflow positioning to Google rather than treating it as an AI Lab ranking.
- Keep introductory pricing, service quotas, API rollout state, and preview-only hosted features freshness-sensitive.

## Validation

- Gemini 3.8 Flash remains a concrete member of Gemini rather than a separate family.
- Stable model identity is not conflated with mutable Gemini API or Google AI Studio behavior.

## Verified identity and provenance

Stable provider-hosted text-output model served as gemini-3.8-flash; multimedia input does not imply media generation or a Live API model.

## Source-scoped operating boundaries

- The current model supports function calls, code execution, caching, grounding, and structured outputs. Image/audio generation and Live API are unsupported; computer use is separately marked preview. [Model reference](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash).
- Thinking supports low, medium, and high; minimal returns an error. Use the version-specific model page because the generic latest-model guide now covers a newer generation. [Thinking configuration](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash).
- Model-generated tool requests require application validation and authorization before execution. A stable model release does not make every attached tool or preview capability production-ready. [Function-calling workflow](https://ai.google.dev/gemini-api/docs/function-calling).

## Source evidence

- <https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash>
- <https://ai.google.dev/gemini-api/docs/function-calling>
