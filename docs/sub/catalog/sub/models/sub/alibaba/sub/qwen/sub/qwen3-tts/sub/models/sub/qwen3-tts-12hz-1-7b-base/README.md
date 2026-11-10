# Qwen3-TTS-12Hz-1.7B-Base

Qwen3-TTS-12Hz-1.7B-Base is a released Apache-2.0 12Hz speech-synthesis checkpoint. Text plus reference audio enables voice-cloned speech, and the Base checkpoint supports downstream fine-tuning.

## Decision and Operational Boundaries

Qwen3-TTS-12Hz-1.7B-Base is a released Apache-2.0 12Hz speech-synthesis checkpoint. Standard voice cloning uses synthesis text, reference audio (`ref_audio`), and its transcript (`ref_text`); the Base checkpoint also supports downstream fine-tuning.

- Use the corresponding Qwen3TTSModel operation and its required inputs; Base, CustomVoice, and VoiceDesign are separate checkpoints, not interchangeable flags.
- Setting `x_vector_only_mode=True` uses only the reference speaker embedding and removes the `ref_text` requirement, but may reduce cloning quality.
- The 12Hz label describes the speech-token representation, not the output waveform sample rate; latency and memory depend on the selected runtime.
- Verify authorization for reference recordings and intended voice use; synthesized speech is not proof of speaker consent or authenticity.

## Relationships

| Relationship | Catalog page |
| --- | --- |
| Member of | [Qwen3-TTS](../../../../) |

## Primary Sources

- [Official model card or license: Qwen/Qwen3-TTS-12Hz-1.7B-Base](https://huggingface.co/Qwen/Qwen3-TTS-12Hz-1.7B-Base)
- [Official repository: QwenLM/Qwen3-TTS](https://github.com/QwenLM/Qwen3-TTS)
