# Qwen3-ForcedAligner-0.6B

Qwen3-ForcedAligner-0.6B is the released Apache-2.0 timestamp-alignment companion to Qwen3-ASR.

## Decision and Operational Boundaries

- It requires audio plus supplied text and returns alignment/timing; it is not an automatic transcription or speaker-recognition model.
- The documented boundary is up to five minutes of speech in eleven languages; do not transfer the ASR models' language inventory or long-audio behavior.
- Validate supplied transcript accuracy and consent to process the recording; alignment is not independent evidence that a transcript is correct.

## Relationships

| Relationship | Catalog page |
| --- | --- |
| Member of | [Qwen3-ASR](../../../../) |

## Primary Sources

- [Official model card or license: Qwen/Qwen3-ForcedAligner-0.6B](https://huggingface.co/Qwen/Qwen3-ForcedAligner-0.6B)
- [Official repository: QwenLM/Qwen3-ASR](https://github.com/QwenLM/Qwen3-ASR)
