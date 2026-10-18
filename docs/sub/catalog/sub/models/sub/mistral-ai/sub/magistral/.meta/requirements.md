# Documentation Requirements

## Requirements

- Render the standard entity-relations block from the validated current-entity projection.

- Identify Magistral as Mistral AI's reasoning-specialized model family.
- Retain Magistral Small 2509 as a concrete lifecycle-relevant open checkpoint, but reflect Mistral's current model index: Magistral Small 1.2 (`magistral-small-2509`) is deprecated rather than a current recommended release.
- Keep reasoning prompts, language support, benchmarks, context, license, API aliases, deprecation/retirement state, and deployment support freshness-sensitive.

## Validation

- Producer provenance resolves to Mistral AI.
- Magistral remains distinct from general Mistral Small despite the `Small` size/name token in the checkpoint.
- Deprecated Magistral checkpoints are not presented as current GA recommendations.

## Source-backed profile

- Required reader orientation: Magistral is Mistral AI’s reasoning-specialized model family.
- Preserve this model-scoped fact: The represented Small 2509 checkpoint is called Small 1.2 in the API catalog. Its hosted release is deprecated, while its open weights retain their model identity. [Magistral Small 1.2 lifecycle and model card](https://docs.mistral.ai/models/magistral-small-1-2-25-09)

## Operational and interpretation boundaries

- Explain this boundary: Reasoning traces, special-token formatting and effective context are release-specific. A model-generated chain of reasoning is not formal verification. [Magistral Small 2509 weights and prompting](https://huggingface.co/mistralai/Magistral-Small-2509)

- Keep source-reported capabilities distinct from application-level correctness, authorization and measured deployment performance.
