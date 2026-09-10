# Documentation Requirements

## Requirements

- Present `software/` as the canonical catalog owner for installable or self-managed software grouped by primary role.
- Keep hosted-only or externally operated service identity under `catalog/services/`; keep models, datasets, hardware, and producers with their separate canonical catalog owners.
- Render the standard child-navigation block from the validated direct-child projection so every currently materialized direct software category appears exactly once.
- Treat category placement as primary-role ownership rather than an assertion that a product has only one capability.
- Keep the page concise; concrete software facts, installation details, operational guidance, and comparisons belong to their appropriate child or non-catalog owners.

## Validation

- The page contains no temporary-placeholder wording.
- The child-navigation block matches the validated materialized direct-child projection and every destination resolves to a direct child of `software/`.
- The page does not absorb hosted-only services, model identity, dataset identity, hardware identity, or producer identity.
- The page does not duplicate concrete software profiles.
