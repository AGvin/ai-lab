# Qwen3-ASR-0.6B

Qwen3-ASR-0.6B is a released Apache-2.0 model for language identification and speech-to-text across 30 languages and 22 Chinese dialects.

## Decision and Operational Boundaries

- Keep transcription separate from translation, speech synthesis, speaker authentication, and timestamp alignment; timestamps can require the separate ForcedAligner.
- Streaming and offline support are runtime-dependent. The later -hf checkpoints are native-Transformers packaging, not independently trained peer identities.
- Recordings and transcripts remain sensitive; authorize capture and review recognition errors before consequential use.

## Relationships

| Relationship | Catalog page |
| --- | --- |
| Member of | [Qwen3-ASR](../../../../) |

## Primary Sources

- [Official model card or license: Qwen/Qwen3-ASR-0.6B](https://huggingface.co/Qwen/Qwen3-ASR-0.6B)
- [Official repository: QwenLM/Qwen3-ASR](https://github.com/QwenLM/Qwen3-ASR)
