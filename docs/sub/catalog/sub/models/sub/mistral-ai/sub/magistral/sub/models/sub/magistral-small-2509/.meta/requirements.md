# Documentation Requirements

## Requirements

- Render the standard entity-relations block from the validated current-entity projection.

- Identify Magistral Small 2509 as the Apache-2.0 open reasoning checkpoint in the Magistral family.
- Preserve reasoning-mode/system-prompt, language, multimodal, benchmark, context, and runtime claims only at exact model-card scope.

## Validation

- Membership resolves to Magistral.

## Source-backed profile

- Required reader orientation: Magistral Small 2509 is the open reasoning checkpoint named Magistral Small 1.2 in Mistral’s September 2025 API documentation.
- Preserve this model-scoped fact: The Apache 2.0 checkpoint accepts text and images and supports 128K tokens; Mistral warns that performance may degrade beyond 40K. [Magistral Small 2509 weights and prompting](https://huggingface.co/mistralai/Magistral-Small-2509)
- Preserve this model-scoped fact: The hosted `magistral-small-2509` release is deprecated from April 30, 2026, with Mistral Small 4 identified for new integrations. [Magistral Small 1.2 lifecycle and model card](https://docs.mistral.ai/models/magistral-small-1-2-25-09)

## Operational and interpretation boundaries

- Explain this boundary: Use the release’s reasoning system prompt and tokenizer support for the special `[THINK]` / `[/THINK]` tokens. Plain text that resembles these tokens is not equivalent to their encoded control tokens. [Magistral Small 2509 weights and prompting](https://huggingface.co/mistralai/Magistral-Small-2509)
- Explain this boundary: Reasoning traces are generated content, not proof that an answer is correct; downstream verification remains separate from the model’s reasoning format.

- Keep source-reported capabilities distinct from application-level correctness, authorization and measured deployment performance.
