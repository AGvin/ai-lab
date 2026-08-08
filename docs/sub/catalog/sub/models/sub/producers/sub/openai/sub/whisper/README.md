# Whisper

Whisper is OpenAI's downloadable multilingual automatic-speech-recognition model family for transcription, speech translation, and language identification.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Canonical producer

- [OpenAI](../../../../../../../../../producers/sub/o/sub/openai/)

## Model-family profile

Whisper uses an encoder-decoder Transformer architecture. The released family spans model sizes from approximately 39 million to 1.55 billion parameters and includes English-only and multilingual variants.

The upstream family also includes later variants such as `large-v3` and `turbo`. This migration keeps Whisper at the family level because no current catalog requirement depends on separate canonical pages for those releases; exact checkpoint lineage and downloads remain available upstream until a concrete release is needed by comparisons, deployment notes, or evaluation evidence.

## Scope boundary

This canonical page owns Whisper family identity, producer relation, shared model-family characteristics, and authoritative references. Installation, inference software, runtime and hardware guidance, quantization, speech-model comparisons, task-specific model selection, and integration workflows belong to software, deployment/workflow, decision-support, or evidence documentation.

## Official resources

- [OpenAI Whisper repository](https://github.com/openai/whisper)
- [Whisper paper](https://cdn.openai.com/papers/whisper.pdf)
