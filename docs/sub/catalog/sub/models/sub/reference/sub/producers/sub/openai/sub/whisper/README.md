# Whisper

Whisper is OpenAI's downloadable multilingual automatic-speech-recognition model family for transcription, speech translation, and language identification.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Canonical producer

- [OpenAI](../../../../../../../../../producers/sub/o/sub/openai/)

## Model-family profile

Whisper uses an encoder-decoder Transformer architecture. The released family spans model sizes from approximately 39 million to 1.55 billion parameters and includes English-only and multilingual variants.

The upstream family also includes later variants such as `large-v3` and `turbo`. This migration keeps Whisper at the family level because no current reviewed destination requires separate canonical pages for those releases.

OpenAI's current hosted API catalog also exposes `whisper-1` as a specific general-purpose speech-recognition model. That hosted model ID is not an alias for the entire downloadable Whisper family; it should receive its own concrete model/access representation when downstream documentation needs exact API identity.

## Scope boundary

This page owns Whisper family identity, producer relation, shared model-family characteristics, and authoritative references. Exact release/checkpoint lineage, hosted `whisper-1`, installation, inference software, runtime/hardware guidance, quantization, speech-model comparisons, and integration workflows belong to concrete model/artifact, software/deployment, selection, or evidence owners when materialized.

## Official resources

- [OpenAI Whisper repository](https://github.com/openai/whisper)
- [Whisper paper](https://cdn.openai.com/papers/whisper.pdf)
- [Whisper API model](https://developers.openai.com/api/docs/models/whisper-1)
