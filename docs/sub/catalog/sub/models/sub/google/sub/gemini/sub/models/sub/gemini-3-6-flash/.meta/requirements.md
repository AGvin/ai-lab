# Documentation Requirements

## Requirements

- Identify Gemini 3.6 Flash as a concrete stable provider-hosted multimodal model in the Gemini family.
- Preserve source-backed model code, modalities, token limits, and stable-release status.
- Keep mutable feature availability, service behavior, pricing, deployment workflow, and selection conclusions outside canonical identity.

## Content Specification

- Use `Gemini 3.6 Flash` as the page title and link the canonical Gemini family.
- Preserve stable model code `gemini-3.6-flash`.
- Preserve Gemini API and Google AI Studio as access products rather than model aliases.
- Preserve text/image/video/audio/PDF input, text output, 1,048,576-token input limit, and 65,536-token output limit from the current model page.
- Preserve the July 21, 2026 stable GA date from official release notes.
- Present fast coding/agentic/spatial positioning as provider claims rather than independent AI Lab task evidence.
- Treat currently supported API tools/features as mutable provider state that must be rechecked at use time.

## Validation

- Gemini API and Google AI Studio are not represented as model aliases.
- Mutable feature availability is not frozen into immutable identity.
- No downloadable-weight or local-hardware claim is inferred.
- Provider positioning is not presented as independent AI Lab quality evidence.
- The `member-of` relation resolves to Gemini.

## Verified identity and provenance

Stable provider-hosted text-output model served as gemini-3.6-flash; multimedia input does not imply media generation or a Live API model.

## Source-scoped operating boundaries

- The current model supports function calls, code execution, caching, grounding, and structured outputs. Image/audio generation and Live API are unsupported; computer use is separately marked preview. [Model reference](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash).
- Model-generated tool requests require application validation and authorization before execution. A stable model release does not make every attached tool or preview capability production-ready. [Function-calling workflow](https://ai.google.dev/gemini-api/docs/function-calling).

## Source evidence

- <https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash>
- <https://ai.google.dev/gemini-api/docs/function-calling>
