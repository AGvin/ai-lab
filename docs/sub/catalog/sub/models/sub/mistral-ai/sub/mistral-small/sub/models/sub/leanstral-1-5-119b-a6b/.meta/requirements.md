# Documentation Requirements

## Requirements

- Render the standard entity-relations block from the validated current-entity projection.

- Identify Leanstral 1.5 119B A6B as Mistral's Apache-2.0 code-agent model specialized for Lean 4 theorem proving and formalized software/mathematics workflows.
- Preserve Mistral's explicit upstream boundary that Leanstral 1.5 is built as part of the Mistral Small 4 family; do not create a separate top-level Leanstral family solely because the checkpoint has a specialized product name.
- State that the hosted Labs release retired on 2026-09-30 while the released Apache-2.0 weights remain a distinct distribution.
- Keep its 119B-total/6.5B-active architecture, multimodal support, context guidance, reasoning settings, and Labs/API access source-scoped.
- Treat benchmarks, API routing, Vibe integration, deployment support, retirement/replacement guidance, and future Leanstral revisions as freshness-sensitive.

## Validation

- Membership resolves to Mistral Small.
- The specialized checkpoint is represented once and is not duplicated as a peer family.
- The retired hosted endpoint is not presented as a current or future availability option.

## Source-backed profile

- Required reader orientation: Leanstral 1.5 119B A6B is Mistral AI’s Lean 4 proof-engineering checkpoint built as part of the Mistral Small 4 family.
- Preserve this model-scoped fact: The Apache 2.0 model has 119B total and 6.5B active parameters. It accepts text and images, with a 256K context; its model card recommends at most 200K tokens. [Leanstral 1.5 weights and family lineage](https://huggingface.co/mistralai/Leanstral-1.5-119B-A6B)
- Preserve this model-scoped fact: The experimental hosted `labs-leanstral-1-5` release is retired according to Mistral’s September 30, 2026 retirement schedule. The open checkpoint remains a distinct distribution. [Mistral model changelog](https://docs.mistral.ai/resources/changelogs)

## Operational and interpretation boundaries

- Explain this boundary: The checkpoint produces Lean code and proposed proofs; correctness is established by checking them in the intended Lean environment, including their assumptions. Model-generated reasoning is not the checker.
- Explain this boundary: Keep the upstream `none`/`high` reasoning contract and model-specific serving configuration. A tool harness controls edits and execution; historical Labs setup instructions do not establish present API availability. [Leanstral 1.5 weights and family lineage](https://huggingface.co/mistralai/Leanstral-1.5-119B-A6B)

- Keep source-reported capabilities distinct from application-level correctness, authorization and measured deployment performance.
