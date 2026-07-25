# Whisper

Whisper is an OpenAI family of downloadable speech-recognition models for multilingual transcription, speech translation, and language identification.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Official profile

- Provider: OpenAI
- Model type: encoder-decoder Transformer for speech recognition
- Access model: downloadable model weights and local inference code
- License: MIT
- Input: audio
- Output: text and task metadata produced by the selected runtime
- Primary workloads: multilingual transcription, speech translation to English, and language identification

The official repository publishes several checkpoints with different parameter counts, memory requirements, and speed-quality trade-offs. A recommendation must name the exact checkpoint and runtime rather than referring only to `Whisper`.

## Selection guidance

Select the checkpoint from measured:

- word or character error rate on the target language, accent, noise, and domain;
- timestamp and segmentation quality;
- real-time factor and end-to-end latency;
- peak VRAM and host RAM;
- batching and concurrency behavior;
- terminology and proper-name accuracy;
- hallucination, repetition, and silence-handling failures.

Whisper is not a speaker-diarization model. Use a separate diarization system when speaker attribution is required, then validate alignment between transcript segments and speaker labels.

## Deployment boundary

Local weights can support offline or private workflows, but privacy also depends on the runtime, storage, logs, temporary files, and downstream processing. Hosted services that expose Whisper-derived models are separate deployments with their own versions, terms, retention, pricing, and behavior.

## Evidence boundary

Architecture, checkpoint list, access model, and license are provider-documented. Accuracy, speed, hardware fit, language quality, and accepted-result cost are checkpoint-, runtime-, and workload-specific.

## Related pages

- [OpenAI models](../..)
- [Models](../../../..)
- [Speech and Conversation](../../../../../../notes/sub/comparisons/sub/model-selection/sub/speech-and-conversation/)

## Sources

- [OpenAI Whisper repository](https://github.com/openai/whisper)
- [Whisper paper](https://arxiv.org/abs/2212.04356)
