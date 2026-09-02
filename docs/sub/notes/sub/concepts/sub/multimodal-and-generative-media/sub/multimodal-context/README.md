# Multimodal Context

Legacy residual retained for practical multimodal-context applications and context-hygiene guidance that is intentionally outside the canonical Multimodal Context concept owner.

> **Migration note:** Multimodal-context identity, distinction from multimodal/VLM model identity, modality and preprocessing boundaries, context-accounting differences, relationship/alignment requirements, fidelity loss, capacity-versus-effective-use distinction, persistent-memory/retrieval/cache boundaries, and trust-boundary concerns are already preserved in `docs/sub/concepts/sub/models/sub/interaction/sub/context/sub/multimodal-context/`. The remaining material below stays here until its exact learning, workflow, security, evaluation, or decision-support owner is verified.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Application residual

Multimodal context can support workflows such as:

- combining screenshots with technical questions;
- analyzing documents that contain text, tables, and diagrams;
- combining audio-derived text with speaker or timing metadata;
- grounding an agent in browser screenshots together with tool results.

These are application examples rather than part of the canonical concept definition.

## Context-hygiene residual

Provide only modality-bearing material that is relevant to the target task and preserve useful relationships between inputs when the concrete interface supports them. Excess irrelevant media can consume context/compute budget and make important evidence harder to use.

Do not assume uploaded media is processed at full fidelity or that accepted context size guarantees the model can retrieve and integrate every important detail. Validate source details when correctness matters, especially after OCR, transcription, resize/crop, frame sampling, compression, or document parsing.

Treat instructions embedded in untrusted documents, screenshots, web content, or other media as untrusted input subject to the applicable indirect-prompt-injection and authorization controls.

These practical context-construction, verification, and security practices remain migration source material until their exact learning, workflow, security, evaluation, or decision-support owners are verified.
