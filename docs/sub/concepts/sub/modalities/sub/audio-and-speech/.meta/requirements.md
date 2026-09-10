# Documentation Requirements

## Requirements

- Use the reader-facing title `Audio and Speech`.
- Present this node as the canonical modality owner for reusable AI concepts whose primary information domain is acoustic/audio signals, including speech and non-speech audio, while recognizing that spoken language also relates to the selected `language/` modality.
- Distinguish physical audio signals from model representations. Waveforms, spectrograms, codec tokens, acoustic features, embeddings, symbolic music representations, and latent codes can represent audio-related information without becoming separate modalities by themselves.
- Distinguish speech from general audio. Speech is structured acoustic communication carrying linguistic and paralinguistic information, while audio also includes music, environmental sounds, effects, ambience, non-speech vocalizations, and other acoustic signals.
- Keep `speech-to-text/`, `text-to-speech/`, and `audio-generation/` as distinct selected descendants. Speech recognition/transcription maps speech-bearing audio toward linguistic output; TTS synthesizes speech from linguistic conditioning; audio generation owns broader generative synthesis of acoustic content.
- Explain that speech/audio systems can also perform language identification, translation, diarization, speaker recognition, source separation, enhancement, restoration, event detection, music analysis, or other tasks, but do not infer unlisted child nodes from those legitimate capabilities.
- Distinguish modality semantics from codecs and file formats. PCM, WAV, FLAC, MP3, AAC, Opus, spectrogram images, token streams, and container formats are representations/encodings and have separate specification/runtime ownership where applicable.
- Explain that sampling rate, bit depth, channel layout, microphone characteristics, compression, noise, reverberation, clipping, and preprocessing can affect model-usable audio information without defining the modality itself.
- Make clear that speech content can carry sensitive biometric, identity, health, location, or private conversational information, while detailed privacy/security/consent requirements remain with their trustworthy-AI/governance owners.
- Render the standard direct-child navigation from the validated materialized child set when reader-facing rendering is activated.
- Keep concrete model/service modality support, codecs/formats, voice identities, accepted durations/sampling rates, runtime preprocessing, benchmark results, prices, and model-selection guidance with their applicable catalog, specification, runtime/service, evidence, governance, or decision owners.

## Validation

- Audio/speech is not equated with one waveform representation, codec, model architecture, or provider API.
- Speech and non-speech audio are distinguished without duplicating the separate language modality.
- STT, TTS, and general audio generation remain separate selected descendants.
- Unlisted audio tasks are not materialized implicitly.
- Concrete codecs, service limits, voice/model identities, and benchmark outcomes remain outside the modality owner.
- Direct-child navigation contains only currently materialized selected descendants.
