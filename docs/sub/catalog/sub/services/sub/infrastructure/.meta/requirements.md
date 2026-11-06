# Documentation Requirements

## Requirements

- Present `infrastructure/` as the services catalog index for hosted compute, deployment, sandbox, managed browser, and application-running services used to operate models or AI applications.
- Render child navigation from the validated materialized direct-child projection so every current infrastructure service appears exactly once; do not hard-code a fixed child count or stale enumerated inventory in this contract.
- Keep concrete service identity and source-backed facts with each child profile.
- Keep self-managed infrastructure software and hardware identities with their respective canonical owners.
- Classify by primary product identity rather than incidental features: a web-data service does not become infrastructure solely because it exposes browser execution, while a managed browser/session platform belongs here when remote browser infrastructure is its primary product boundary.

## Validation

- The page contains no temporary-summary or RC wording.
- Navigation matches the current materialized direct-child projection and every destination resolves.
- Hosted-service ownership is not conflated with self-managed software or hardware.
- Adding or removing a materialized child does not require manually changing a hard-coded child count in this requirements contract.
