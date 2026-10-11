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
