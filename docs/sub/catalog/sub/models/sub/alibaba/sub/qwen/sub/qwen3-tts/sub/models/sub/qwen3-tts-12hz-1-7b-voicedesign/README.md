# Qwen3-TTS-12Hz-1.7B-VoiceDesign

Qwen3-TTS-12Hz-1.7B-VoiceDesign is a released Apache-2.0 12Hz speech-synthesis checkpoint. Text plus a natural-language voice description produces speech; a reference recording is not required.

## Decision and Operational Boundaries

- Use the corresponding Qwen3TTSModel operation and its required inputs; Base, CustomVoice, and VoiceDesign are separate checkpoints, not interchangeable flags.
- The 12Hz label describes the speech-token representation, not the output waveform sample rate; latency and memory depend on the selected runtime.
- Verify authorization for reference recordings and intended voice use; synthesized speech is not proof of speaker consent or authenticity.

## Relationships

| Relationship | Catalog page |
| --- | --- |
| Member of | [Qwen3-TTS](../../../../) |

## Primary Sources

- [Official model card or license: Qwen/Qwen3-TTS-12Hz-1.7B-VoiceDesign](https://huggingface.co/Qwen/Qwen3-TTS-12Hz-1.7B-VoiceDesign)
- [Official repository: QwenLM/Qwen3-TTS](https://github.com/QwenLM/Qwen3-TTS)
