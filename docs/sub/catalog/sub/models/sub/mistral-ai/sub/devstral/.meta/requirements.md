# Documentation Requirements

## Requirements

- Render the standard entity-relations block from the validated current-entity projection.

- Identify Devstral as Mistral AI's code-agent model family for software-engineering and repository-scale agent work.
- Retain Devstral 2 123B and Devstral Small 2 24B as distinct lifecycle-relevant trained-model identities, but reflect Mistral's current model index: both 25.12 API releases are deprecated and are no longer current recommended models.
- Keep Mistral Vibe as a separate software/agent product surface rather than part of model identity.
- Treat replacement guidance, deprecation/retirement dates, SWE-bench results, API pricing, context, tool format, deployment support, license terms, and provider availability as freshness-sensitive.

## Validation

- Producer provenance resolves to Mistral AI.
- The family is not collapsed into Mistral Small solely because one smaller checkpoint exists.
- Deprecated Devstral checkpoints remain historical identities without being presented as current GA recommendations.

## Source-backed profile

- Required reader orientation: Devstral is Mistral AI’s code-agent family for repository-scale software-engineering work.
- Preserve this model-scoped fact: The represented December 2025 checkpoints remain distinct historical model identities. Their hosted releases are deprecated, while their released weights have separate license terms. [Devstral 2 lifecycle and API model card](https://docs.mistral.ai/models/devstral-2-25-12) [Devstral Small 2 lifecycle and API model card](https://docs.mistral.ai/models/devstral-small-2-25-12)

## Operational and interpretation boundaries

- Explain this boundary: The 123B Modified MIT checkpoint and Apache 2.0 Small checkpoint do not share one license. Agent software controls tool permissions and command execution; the model is not the agent harness. [Devstral 2 Modified MIT license](https://huggingface.co/mistralai/Devstral-2-123B-Instruct-2512/blob/main/LICENSE) [Devstral Small 2 released weights](https://huggingface.co/mistralai/Devstral-Small-2-24B-Instruct-2512)

- Keep source-reported capabilities distinct from application-level correctness, authorization and measured deployment performance.
