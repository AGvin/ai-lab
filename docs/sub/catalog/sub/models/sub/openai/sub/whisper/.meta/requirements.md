# Documentation Requirements

## Requirements

- Identify Whisper as OpenAI's downloadable multilingual automatic-speech-recognition model family.
- Preserve family facts without inventing concrete release nodes solely for historical completeness.
- Distinguish the hosted `whisper-1` API model identity from the broader downloadable Whisper family.
- Keep inference software, model-selection comparisons, deployment instructions, and practical integration guidance outside the canonical family profile.

## Content Specification

- Use `Whisper` as the page title and link the canonical OpenAI producer.
- Preserve transcription, speech translation, language identification, encoder-decoder Transformer architecture, approximate 39M–1.55B family scale range, and English-only/multilingual variant distinction.
- Mention `large-v3` and `turbo` as upstream family variants without creating child nodes solely for completeness.
- State that `whisper-1` is a concrete hosted API model rather than an alias for the whole family.
- Include the official Whisper repository, paper, and current `whisper-1` model documentation.

## Validation

- Whisper family identity is not collapsed into `whisper-1`.
- `whisper-1` is not silently generalized to downloadable checkpoints.
- Family variants are not materialized without real downstream documentation need.
- Software/runtime guidance is not duplicated on the family page.

## Source-scoped operating boundaries

- OpenAI deprecated the hosted whisper-1 API model on August 26, 2026 with shutdown scheduled for February 26, 2027. This API notice does not retire downloadable Whisper checkpoints [API deprecations](https://developers.openai.com/api/docs/deprecations).
- The model card documents unspoken-text hallucinations and uneven performance by language and domain. Speaker or human-attribute classification is not established by the family’s ASR role [Whisper model card](https://github.com/openai/whisper/blob/main/model-card.md).

## Source evidence

- [Whisper repository](https://github.com/openai/whisper).
- [Whisper model card](https://github.com/openai/whisper/blob/main/model-card.md).
- [Introducing Whisper](https://openai.com/index/whisper/).
- [whisper-1 model reference](https://developers.openai.com/api/docs/models/whisper-1).
- [API deprecations](https://developers.openai.com/api/docs/deprecations).
