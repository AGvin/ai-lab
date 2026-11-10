# Documentation Requirements

## Requirements

- Identify omni-moderation as OpenAI's current multimodal moderation model for harmful-content classification over text and image inputs.
- Preserve the current alias/snapshot distinction: `omni-moderation-latest` is the mutable convenience alias and `omni-moderation-2024-09-26` is a pinned snapshot of the same represented model line, not separate peer catalog identities.
- Keep moderation category taxonomy, scores/threshold handling, endpoint schemas, rate limits, safety-policy interpretation, and operational enforcement logic freshness-sensitive and outside intrinsic trained-model identity.
- Do not present provider moderation scores as complete application safety policy or as a substitute for domain-specific safeguards.

## Validation

- The page represents the current trained moderation model line without creating duplicate alias/snapshot nodes.
- Text/image moderation is not generalized to audio.
- Producer provenance resolves bidirectionally to OpenAI.

## Source-scoped operating boundaries

- Categories have different input-type coverage. Use category_applied_input_types when interpreting results: an unsupported category can return zero for image-only input, which is not a finding that the content is safe for that category [Moderation guide](https://developers.openai.com/api/docs/guides/moderation).
- Scores and custom thresholds may need recalibration after model updates. The application defines enforcement, escalation, and review; a model score is not a complete safety policy [Moderation guide](https://developers.openai.com/api/docs/guides/moderation).

## Source evidence

- [omni-moderation-latest model reference](https://developers.openai.com/api/docs/models/omni-moderation-latest).
- [Moderation guide](https://developers.openai.com/api/docs/guides/moderation).
