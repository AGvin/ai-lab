# Multimodal Context

Multimodal context is the combined text, image, audio, video, document, and tool information available to a model during a request.

## Core idea

Each modality is converted into tokens or learned features and consumes part of a limited context or compute budget. A high-resolution image, long audio recording, or large PDF may be compressed, sampled, split, or summarized before the model sees it.

## Practical use

- Combine screenshots with technical questions.
- Analyze documents containing text, tables, and diagrams.
- Use audio transcripts together with speaker metadata.
- Ground an agent in browser screenshots and tool results.

## Trade-offs and limitations

Adding modalities does not guarantee that the model integrates them correctly. Important details may be lost during OCR, frame sampling, resizing, or transcription. Conflicting evidence across modalities requires explicit handling.

## Common mistakes

- Assuming uploaded media is processed at full fidelity.
- Providing many irrelevant images and diluting attention.
- Ignoring context-window consumption from media.
- Trusting instructions embedded inside untrusted documents or screenshots.

## Related concepts

- [Multimodal and Generative Media](../../)
- [Vision-Language Models](../vision-language-models/)
- [Context Window](../../../model-usage-and-generation/sub/context-window/)
- [Indirect Prompt Injection](../../../safety-privacy-and-reliability/sub/indirect-prompt-injection/)
