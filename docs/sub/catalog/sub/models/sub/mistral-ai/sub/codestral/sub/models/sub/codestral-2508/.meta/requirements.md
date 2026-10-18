# Documentation Requirements

## Requirements

- Render the standard entity-relations block from the validated current-entity projection.

- Identify Codestral 2508 as the current code-generation/completion release exposed as `codestral-2508` and through moving Codestral aliases.
- Preserve fill-in-the-middle, code generation, context, tool/function support, and API behavior only at current first-party model scope.
- Treat pricing, aliases, provider routes, lifecycle state, and replacement guidance as freshness-sensitive.

## Validation

- Membership resolves to Codestral.

## Source-backed profile

- Required reader orientation: Codestral 2508 is Mistral AI’s code-generation and fill-in-the-middle completion model released on July 30, 2025.
- Preserve this model-scoped fact: The model card lists a 128K-token context and GA Premier API release `codestral-2508`. [Codestral 2508 model card](https://docs.mistral.ai/models/codestral-25-08)
- Preserve this model-scoped fact: It supports code completion through `/v1/fim/completions`, alongside chat, function calling and structured outputs. [Codestral 2508 model card](https://docs.mistral.ai/models/codestral-25-08)

## Operational and interpretation boundaries

- Explain this boundary: A function call is a proposed operation: the application receives its arguments and controls execution. Generated code and arguments still require application validation. [Function-calling contract](https://docs.mistral.ai/studio/conversations/function-calling)
- Explain this boundary: The Premier API listing does not establish a downloadable Apache-licensed checkpoint. Do not inherit licensing from earlier Codestral releases. [Codestral 2508 model card](https://docs.mistral.ai/models/codestral-25-08)

- Keep source-reported capabilities distinct from application-level correctness, authorization and measured deployment performance.
