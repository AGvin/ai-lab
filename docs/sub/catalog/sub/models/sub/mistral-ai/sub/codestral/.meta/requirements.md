# Documentation Requirements

## Requirements

- Render the standard entity-relations block from the validated current-entity projection.

- Identify Codestral as Mistral AI's code-specialized model line and keep generation/completion and code-embedding checkpoints as distinct concrete members.
- Materialize the current Codestral 2508 code-generation/FIM release and Codestral Embed 2505 code-embedding release.
- Keep retired earlier Codestral checkpoints, Codestral Mamba, hosted aliases, API pricing, Vibe presets, and third-party routes outside current concrete ownership unless separately required.
- Treat context, FIM behavior, embedding dimensions/options, pricing, lifecycle, and API aliases as freshness-sensitive.

## Validation

- Producer provenance resolves to Mistral AI.
- Code generation and code embedding are not conflated as one interchangeable model checkpoint.

## Source-backed profile

- Required reader orientation: Codestral is Mistral AI’s model line for code completion and code embeddings.
- Preserve this model-scoped fact: Code-generation checkpoints return source text; code-embedding checkpoints return vectors. Those interfaces and their evaluation criteria are different. [Codestral 2508 model card](https://docs.mistral.ai/models/codestral-25-08) [Codestral Embed 2505 model card](https://docs.mistral.ai/models/codestral-embed-25-05)

## Operational and interpretation boundaries

- Explain this boundary: Use concrete member documentation for context, model identifiers and licensing. A shared family name does not make a completion model and an embedding model interchangeable.

- Keep source-reported capabilities distinct from application-level correctness, authorization and measured deployment performance.
