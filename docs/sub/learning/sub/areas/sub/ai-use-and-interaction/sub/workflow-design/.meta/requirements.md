# Documentation Requirements

## Requirements

- Present Workflow Design as practical teaching for turning AI-assisted work into repeatable, reviewable sequences with explicit inputs, outputs, checkpoints, validation, human review, and automation boundaries rather than one-off prompting.
- Keep formal planning algorithms with Reasoning and Decision Making and agent runtime orchestration with Agents and Automation; this group teaches practitioner-facing workflow design independent from one implementation framework.
- Explain that the current materialized subset includes `problem-framing-and-work-breakdown/` for source-backed decomposition/verification teaching and `human-review-and-approval/` for source-backed review/approval teaching.
- Do not imply that unmaterialized selected siblings `repeatable-workflows/` or `automation-boundaries/` are absent from the logical architecture; standard navigation reflects only physical children.
- Teach workflow steps through explicit purpose, inputs/source evidence, expected output/effect, verification/review point, and next-state/decision responsibility where material.
- Place manual/review steps where they can still prevent or correct a material error; a review after an irreversible effect is evidence/audit, not preventive approval.
- Keep system-specific runtime gates, tool authorization, idempotency/retries, and live agent intervention with Agents/Engineering owners, and keep project-specific policies with project/governance owners.

## Validation

- Workflow Design is practitioner-facing and does not duplicate formal planning or agent orchestration theory.
- Human review is positioned where it can influence outcomes rather than added decoratively after the effect.
- Current navigation exposes only materialized selected children.
- Project/product-specific commands and policies remain outside the reusable learning owner.
