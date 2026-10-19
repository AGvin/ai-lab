# Documentation Requirements

## Requirements

- Identify Gemini Omni 1.1 Flash (`gemini-omni-1.1-flash`) as the generally available Gemini Omni model released on 2026-08-27 for conversational video generation and editing.
- Preserve source-backed generation/editing capabilities while keeping resolution controls, API parameters, pricing, and product integrations freshness-sensitive.
- Keep the deprecated `gemini-omni-flash-preview` route as historical preview evidence rather than a current peer model.

## Validation

- Current GA identity is not conflated with the June preview endpoint.
- Product-level Flow/Gemini/YouTube behavior is not treated as intrinsic model contract without model-level evidence.

## Verified identity and provenance

Stable Gemini Omni model served as gemini-omni-1.1-flash for video generation and conversational editing; the older gemini-omni-flash-preview is a separate historical serving route.

## Source-scoped operating boundaries

- The current API accepts text, images, and video. Input video is limited to ten seconds; outputs are 3–10 seconds at 24 FPS with documented resolutions from 360p through 4K. Keep these API limits separate from product UI behavior. [Stable model reference](https://ai.google.dev/gemini-api/docs/models/gemini-omni-flash).
- The old gemini-omni-flash-preview route has an earliest shutdown date of October 22, 2026. The stable 1.1 identity is not a preview merely because an overview groups Omni in a preview section. [Lifecycle table](https://ai.google.dev/gemini-api/docs/deprecations).
- Omni's family model card documents imperfect edit consistency, complex motion, and text rendering, plus safety filters and SynthID. Review generated output rather than treating these mitigations as accuracy guarantees. [Known limitations](https://deepmind.google/models/model-cards/gemini-omni-flash/).

## Source evidence

- <https://ai.google.dev/gemini-api/docs/models/gemini-omni-flash>
- <https://ai.google.dev/gemini-api/docs/deprecations>
- <https://deepmind.google/models/model-cards/gemini-omni-flash/>
