# Whisper

Whisper is OpenAI’s downloadable multilingual automatic-speech-recognition model family. It supports transcription, speech translation, and language identification through an encoder-decoder Transformer architecture.

## Profile

The family spans approximately 39 million to 1.55 billion parameters and includes English-only and multilingual variants. large-v3 and turbo are upstream variants within this family [Whisper repository](https://github.com/openai/whisper).

The hosted whisper-1 API identity is separate from the downloadable family [Whisper API model reference](https://developers.openai.com/api/docs/models/whisper-1).

turbo is optimized for transcription and is not trained for speech translation into English [Whisper repository](https://github.com/openai/whisper).

## Operating boundaries

OpenAI deprecated the hosted whisper-1 API model on August 26, 2026 with shutdown scheduled for February 26, 2027. This API notice does not retire downloadable Whisper checkpoints [API deprecations](https://developers.openai.com/api/docs/deprecations).

The model card documents unspoken-text hallucinations and uneven performance by language and domain. Speaker or human-attribute classification is not established by the family’s ASR role [Whisper model card](https://github.com/openai/whisper/blob/main/model-card.md).

## Relations

- Producer: [OpenAI](../../../../../producers/sub/o/sub/openai/README.md).

## Official resources

- [Whisper repository](https://github.com/openai/whisper).
- [Whisper model card](https://github.com/openai/whisper/blob/main/model-card.md).
- [Introducing Whisper](https://openai.com/index/whisper/).
- [whisper-1 model reference](https://developers.openai.com/api/docs/models/whisper-1).
- [API deprecations](https://developers.openai.com/api/docs/deprecations).
