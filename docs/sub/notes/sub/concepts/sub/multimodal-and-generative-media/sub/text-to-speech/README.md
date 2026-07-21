# Text-to-Speech

Text-to-speech synthesizes spoken audio from written text, optionally conditioned on a selected or reference voice.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Core idea

A TTS system predicts pronunciation, timing, emphasis, and acoustic features, then generates a waveform through a vocoder or end-to-end model. Modern systems can produce highly natural speech and may support style, emotion, speed, and multilingual output.

## Practical use

- Accessibility and screen reading.
- Narration, announcements, and prototypes.
- Voice interfaces.
- Localized audio content.
- Assistive communication.

## Trade-offs and limitations

Names, abbreviations, numbers, and mixed-language text can be pronounced incorrectly. Expressive models may introduce unexpected pauses or emphasis. Voice cloning raises consent, impersonation, and fraud risks.

## Good practice

Use pronunciation dictionaries or phonetic controls where supported. Disclose synthetic speech when context requires it. Obtain explicit permission for cloned or identifiable voices and protect reference recordings.

## Common mistakes

- Cloning a voice without consent.
- Publishing unreviewed pronunciation of critical information.
- Assuming punctuation alone gives precise prosody control.
- Ignoring audio licensing and platform disclosure rules.

## Related concepts

- [Multimodal and Generative Media](../../)
- [Speech-to-Text](../speech-to-text/)
- [Audio Generation](../audio-generation/)
- [Content Moderation](../../../safety-privacy-and-reliability/sub/content-moderation/)
