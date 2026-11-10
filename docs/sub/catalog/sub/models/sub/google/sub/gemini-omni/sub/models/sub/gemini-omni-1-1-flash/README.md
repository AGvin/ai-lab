# Gemini Omni 1.1 Flash

Stable Gemini Omni model served as gemini-omni-1.1-flash for video generation and conversational editing; the older gemini-omni-flash-preview is a separate historical serving route.

## Relations

- Member of: [Gemini Omni](../../../../)

## Official resources

- <https://blog.google/innovation-and-ai/models-and-research/google-labs/new-creative-controls-google-flow/>
- <https://ai.google.dev/gemini-api/docs/changelog>
- <https://ai.google.dev/gemini-api/docs/models/gemini-omni-flash>
- <https://ai.google.dev/gemini-api/docs/deprecations>
- <https://deepmind.google/models/model-cards/gemini-omni-flash/>

## Source-scoped operating boundaries

- The current API accepts text, images, and video. Input video is limited to ten seconds; outputs are 3–10 seconds at 24 FPS with documented resolutions from 360p through 4K. Keep these API limits separate from product UI behavior. [Stable model reference](https://ai.google.dev/gemini-api/docs/models/gemini-omni-flash).
- The old gemini-omni-flash-preview route has an earliest shutdown date of October 22, 2026. The stable 1.1 identity is not a preview merely because an overview groups Omni in a preview section. [Lifecycle table](https://ai.google.dev/gemini-api/docs/deprecations).
- Omni's family model card documents imperfect edit consistency, complex motion, and text rendering, plus safety filters and SynthID. Review generated output rather than treating these mitigations as accuracy guarantees. [Known limitations](https://deepmind.google/models/model-cards/gemini-omni-flash/).
