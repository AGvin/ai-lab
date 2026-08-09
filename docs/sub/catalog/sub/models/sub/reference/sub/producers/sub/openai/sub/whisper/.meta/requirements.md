# Documentation Requirements

## Requirements

- Identify Whisper as OpenAI's downloadable multilingual automatic-speech-recognition model family.
- Preserve model-family facts from the legacy Whisper page without inventing concrete release nodes that are not currently needed by the catalog.
- Keep inference software, model-selection comparisons, deployment instructions, and practical integration guidance outside the canonical model-family profile.

## Content Specification

- Use `Whisper` as the page title.
- Link the canonical OpenAI producer page through the `produced-by` relation.
- Preserve transcription, speech translation, and language identification as the core documented tasks.
- Preserve the encoder-decoder Transformer architecture family and the documented scale range from approximately 39 million to 1.55 billion parameters across released model sizes.
- Preserve the distinction between English-only and multilingual variants.
- Mention `large-v3` and `turbo` as notable upstream family variants without creating separate canonical child nodes in this migration pass.
- Include the official Whisper repository and paper.
- Explain that exact release lineage, checkpoints, and download variants remain tracked upstream until a concrete Whisper release is needed by comparisons, deployment notes, or evaluation evidence.

## Excluded Residual Content

Preserve outside this canonical family profile:

- installation and inference-tool instructions;
- runtime, hardware, quantization, and deployment guidance;
- speech-model comparisons and task-specific model selection;
- integration examples and workflow recommendations.

## Validation

- Whisper is not treated as a hosted API product identity.
- Family variants are not materialized as canonical child nodes without a real downstream documentation need.
- Software/runtime documentation is not duplicated on the model-family page.
- Producer and source links resolve correctly.
