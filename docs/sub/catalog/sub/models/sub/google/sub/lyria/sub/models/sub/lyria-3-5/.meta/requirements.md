# Documentation Requirements

## Requirements

- Identify Lyria 3.5 as Google's stable Lyria music-generation model released on 2026-09-03.
- Preserve current first-party model identity and keep earlier preview Lyria 3 Pro/Clip routes separate from the stable release.
- Treat generation controls, API limits, pricing, product integration, and regional availability as mutable source-scoped facts.

## Validation

- Lyria 3.5 is not described as preview.
- Earlier preview model routes are not treated as aliases of the stable model without upstream evidence.

## Verified identity and provenance

Stable music-generation model served as lyria-3.5, with text/image input and audio plus lyrics output; API GA timing is distinct from model-card publication.

## Source-scoped operating boundaries

- The API produces 44.1 kHz stereo music and text lyrics from text/image input. Live API, function calling, code execution, grounding, caching, and structured outputs are unsupported. [Lyria 3.5 model reference](https://ai.google.dev/gemini-api/docs/models/lyria-3.5).
- The model card documents safety filtering and SynthID, and prohibits uses that violate privacy or intellectual-property rights. Watermarking is a provenance mitigation, not a grant of rights or proof that output is appropriate for publication. [Use and safety boundary](https://deepmind.google/models/model-cards/lyria-3-5/).

## Source evidence

- <https://ai.google.dev/gemini-api/docs/models/lyria-3.5>
- <https://deepmind.google/models/model-cards/lyria-3-5/>
