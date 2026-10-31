# Granite Speech 4.1 2B Plus

IBM speech checkpoint for speaker-attributed transcription and word-level timestamps. Speaker labels identify turns, not verified people.

## Operating boundaries

Use documented prompts to select rich-transcription modes. Do not assume punctuation or capitalization support. Evaluate timestamps, overlapping speakers and long recordings independently. The October 2026 update is an in-place checkpoint state rather than a separately materialized version. Published weights use Apache-2.0; hosted terms differ.

## Deployment and evidence

Pin the actual October-updated checkpoint revision, compatible processor, selected prompts and inference runtime, rather than assuming that the v2610 comparison label is a separately retrievable version. Measure memory, latency, speaker-label accuracy and timestamp shifts on representative recordings. Apache-2.0 applies to downloaded weights; hosted and packaged-artifact terms may differ. IBM evaluation results are producer-reported, not reproduced here; cache freshness and final rendering remain unverified.

- [Granite Speech 4.1 family](../../../../)
- [Official model card](https://huggingface.co/ibm-granite/granite-speech-4.1-2b-plus)
