# Documentation Requirements

## Requirements

- Present `decision-guides/` as the model-selection index for choosing exact models or model portfolios by a concrete task, need, operating constraint, or portfolio decision.
- Render the standard child-navigation block from the validated direct-child projection so every materialized decision guide appears exactly once.
- Keep broad user-context scenarios that combine persona, tasks, hardware, budget, skills, privacy/data boundaries, and deployment preferences outside this node; those belong to the sibling `user-scenarios/` journey when materialized.
- Keep canonical model identity and intrinsic technical facts in Model Reference; decision guides link to those facts instead of duplicating full model profiles.
- Keep the index concise and navigational; detailed methodology, evidence boundaries, trade-offs, and recommendations remain owned by the applicable child guide.

## Validation

- The child-navigation block matches the validated materialized direct-child projection.
- Every child is a bounded model-selection guide rather than a canonical model profile or broad user scenario.
- The page does not duplicate the complete content of child guides or present a universal best-model ranking.
