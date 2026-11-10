# Documentation Requirements

## Requirements

- Render the standard entity-relations block from the validated current-entity projection.

- Identify Voxtral 4B TTS 2603 as Mistral's open-weight text-to-speech member of the Voxtral line.
- Preserve the current CC-BY-NC-4.0/non-commercial licensing boundary inherited by the released model/reference-voice package.
- Keep supported languages, reference voices, latency, runtime support, evaluation, and hosted access freshness-sensitive.

## Validation

- Membership resolves to Voxtral.

## Source-backed profile

- Required reader orientation: Voxtral 4B TTS 2603 is Mistral AI’s March 2026 text-to-speech checkpoint for speech generation and reference-voice adaptation.
- Preserve this model-scoped fact: The BF16 weights and reference-voice package use CC BY-NC 4.0. Mistral documents nine languages, 24 kHz audio and streaming or batch inference. [Voxtral TTS weights and reference-voice license](https://huggingface.co/mistralai/Voxtral-4B-TTS-2603)
- Preserve this model-scoped fact: The model page lists the March 23, 2026 TTS release as GA. This is speech generation, distinct from Voxtral transcription models. [Voxtral TTS model card](https://docs.mistral.ai/models/voxtral-tts-26-03)

## Operational and interpretation boundaries

- Explain this boundary: The released weights are noncommercial; access through a hosted commercial service has its own terms. A voice sample’s availability does not establish permission to imitate its speaker. [Voxtral TTS weights and reference-voice license](https://huggingface.co/mistralai/Voxtral-4B-TTS-2603)
- Explain this boundary: Reference audio is an input used to condition generated speech. Voice similarity is not speaker authentication, and measured time to first audio is configuration-dependent. [Text-to-speech input and voice prompting](https://docs.mistral.ai/studio/audio/text_to_speech)

- Keep source-reported capabilities distinct from application-level correctness, authorization and measured deployment performance.
