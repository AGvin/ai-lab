# Documentation Requirements

## Requirements

- Identify Leanstral 1.5 119B A6B as Mistral's Apache-2.0 code-agent model specialized for Lean 4 theorem proving and formalized software/mathematics workflows.
- Preserve Mistral's explicit upstream boundary that Leanstral 1.5 is built as part of the Mistral Small 4 family; do not create a separate top-level Leanstral family solely because the checkpoint has a specialized product name.
- Preserve its current lifecycle state: the Labs release is deprecated/scheduled for retirement on 2026-09-30, so availability before retirement must not be described as durable GA support.
- Keep its 119B-total/6.5B-active architecture, multimodal support, context guidance, reasoning settings, and Labs/API access source-scoped.
- Treat benchmarks, API routing, Vibe integration, deployment support, retirement/replacement guidance, and future Leanstral revisions as freshness-sensitive.

## Validation

- Membership resolves to Mistral Small.
- The specialized checkpoint is represented once and is not duplicated as a peer family.
- The deprecated pre-retirement state is visible in rendered guidance.
