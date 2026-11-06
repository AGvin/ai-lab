# Qwen3-ASR

Released 0.6B/1.7B speech-recognition models with a separately named ForcedAligner companion for timestamp alignment.

## Decision and Operational Boundaries

- Preserve the exact member's input/output and license contract; do not turn toolkit options, quantizations, or hosted aliases into peer model identities.
- Recognition returns text; forced alignment requires supplied text and returns timing. Neither produces speech or establishes speaker identity.
- Treat recordings as sensitive, authorize capture/transcription, and review transcripts before consequential use.

## Relationships

| Relationship | Catalog page |
| --- | --- |
| Member of | [Qwen](../../) |
| Produced by | [Qwen Team](../../../../../../../producers/sub/q/sub/qwen-team/) |
| Includes | [Qwen3-ASR-0.6B](./sub/models/sub/qwen3-asr-0-6b/) |
| Includes | [Qwen3-ASR-1.7B](./sub/models/sub/qwen3-asr-1-7b/) |
| Includes | [Qwen3-ForcedAligner-0.6B](./sub/models/sub/qwen3-forcedaligner-0-6b/) |

## Primary Sources

- [Official repository: QwenLM/Qwen3-ASR](https://github.com/QwenLM/Qwen3-ASR)
