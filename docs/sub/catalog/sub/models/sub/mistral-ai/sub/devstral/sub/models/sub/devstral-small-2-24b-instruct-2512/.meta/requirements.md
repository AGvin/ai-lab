# Documentation Requirements

## Requirements

- Render the standard entity-relations block from the validated current-entity projection.

- Identify this checkpoint as the Apache-2.0 24B Devstral Small 2 code-agent model.
- Keep consumer/local hardware guidance, benchmarks, API availability, context, deployment, and Vibe defaults freshness-sensitive.

## Validation

- Membership resolves to Devstral.

## Source-backed profile

- Required reader orientation: Devstral Small 2 24B Instruct 2512 is Mistral AI’s December 2025 multimodal code-agent checkpoint.
- Preserve this model-scoped fact: The 24B FP8 instruct release accepts text and images, has a 256K-token context, and uses Apache 2.0. [Devstral Small 2 released weights](https://huggingface.co/mistralai/Devstral-Small-2-24B-Instruct-2512)
- Preserve this model-scoped fact: The hosted `labs-devstral-small-2512` release is deprecated from February 27, 2026; the current model card points new integrations to Mistral Medium 3.5. [Devstral Small 2 lifecycle and API model card](https://docs.mistral.ai/models/devstral-small-2-25-12)

## Operational and interpretation boundaries

- Explain this boundary: The released weights and their license persist independently of the hosted Labs endpoint. Published local-hardware examples do not guarantee a full-context serving configuration. [Devstral Small 2 released weights](https://huggingface.co/mistralai/Devstral-Small-2-24B-Instruct-2512)
- Explain this boundary: Tool execution belongs to the agent application. Validate generated edits and restrict the commands and files that the harness exposes. [Function-calling contract](https://docs.mistral.ai/studio/conversations/function-calling)

- Keep source-reported capabilities distinct from application-level correctness, authorization and measured deployment performance.
