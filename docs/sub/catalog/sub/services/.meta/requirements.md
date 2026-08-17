# Documentation Requirements

## Requirements

- Present `services/` as the canonical catalog owner for hosted or externally operated products whose primary identity is a service.
- Keep the ownership boundary with installable or self-managed software explicit; those products belong under `catalog/software/`.
- Keep underlying model identity and durable model facts with Model Reference rather than duplicating them as service facts.
- Render the standard child-navigation block from the validated direct-child projection so every currently materialized direct service category appears exactly once.
- Keep the page concise; detailed provider/product facts and mutable hosted-state claims belong to concrete child nodes and must be source-verified there.

## Validation

- The page contains no temporary-placeholder wording.
- The child-navigation block matches the validated materialized direct-child projection and every destination resolves to a direct child of `services/`.
- The page does not classify installable/self-managed software as a service solely because hosted access also exists.
- The page does not duplicate concrete service profiles.
