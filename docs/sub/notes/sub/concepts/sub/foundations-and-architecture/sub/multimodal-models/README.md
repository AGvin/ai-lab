# Multimodal Models

Legacy residual retained for multimodal application examples and practical evaluation guidance that are intentionally outside the canonical multimodal-model classification owner.

> **Migration note:** Multimodal-model identity, model-versus-system boundaries, modality/representation/fusion variability, input-versus-output-versus-reasoning distinctions, modality-specific information constraints, and classification boundaries are already preserved in `docs/sub/concepts/sub/models/sub/classification/sub/multimodal-models/`. The remaining material below stays here until its exact learning or evaluation owner is verified.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Application examples residual

Common multimodal applications include image and document question answering, screenshot and diagram analysis, speech transcription and synthesis, text-guided image or video generation, and cross-modal search using related representations.

These are pedagogical usage examples rather than part of the canonical classification definition.

## Evaluation and operational residual

Practical evaluation should account for what information actually reaches the model. Image resolution, OCR or compression artifacts, audio duration, frame sampling, and document layout can materially affect results; nominal modality support does not imply that every pixel, frame, token, or signal is processed at full fidelity.

Do not treat a generated description as exact measurement, and do not evaluate only one modality when the target behavior depends on cross-modal interaction. These operational/evaluation points remain migration source material until their exact learning or evaluation owner is verified.
