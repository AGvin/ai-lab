# Documentation Requirements

## Requirements

- Identify Lyria as Google's music-generation model family.
- Materialize stable released Lyria identities and keep preview/experimental routes outside the released collection.
- Keep Google Flow Music and other product integrations separate from trained-model identity.

## Validation

- Preview Lyria routes are not promoted to stable peers.
- Product availability and model identity remain distinct.

## Verified identity and provenance

Google music-generation model family; released model identities are separate from Flow Music, experimental realtime routes, and generated audio assets.

## Source-scoped operating boundaries

- The represented stable API model is Lyria 3.5. Lyria RealTime and product integrations do not establish that the stable song-generation endpoint supports Live API interaction. [Stable API capabilities](https://ai.google.dev/gemini-api/docs/models/lyria-3.5).
- Google documents product-level filtering and SynthID plus acceptable-use restrictions covering privacy and intellectual-property rights. Generated music still requires application-specific review and rights assessment. [Lyria model card](https://deepmind.google/models/model-cards/lyria-3-5/).

## Source evidence

- <https://deepmind.google/models/lyria/>
- <https://ai.google.dev/gemini-api/docs/models/lyria-3.5>
- <https://deepmind.google/models/model-cards/lyria-3-5/>
