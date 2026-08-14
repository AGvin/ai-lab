# Documentation Requirements

## Requirements

- Identify Replit Agent as Replit, Inc.'s hosted AI builder/development agent operating inside Replit's managed project and app environment.
- Preserve the hosted execution boundary: Replit Apps/projects are cloud-hosted and Agent works through Replit's Project Editor and managed runtime rather than as a primarily local installable coding agent.
- Preserve the current build loop at a stable high level: Agent can plan, create or modify code, run/debug/test project behavior, use project context, and participate in preview/publishing workflows.
- Preserve useful legacy trust boundaries around project/workspace access, generated code and dependencies, Secrets, databases and storage, integrations, GitHub import/sync or other connected services, deployment/publishing configuration, public visibility, and production changes.
- Preserve checkpoints/review as an operational boundary: generated output and successful Agent execution do not remove the need to test, inspect changes, and control publishing/deployment.
- Keep Agent Skills and other integration mechanisms as configurable product surfaces rather than separate canonical Replit Agent identities.
- Keep plan eligibility, usage limits, pricing, model choice, exact artifact types, feature inventories, deployment products, and other mutable platform-state claims source-backed and time-scoped when expanded.
- Link the canonical Replit, Inc. producer profile.
- Include current official Replit Agent/product documentation and Replit legal reference.

## Validation

- Replit Agent is represented as a hosted development service, not as local software merely because users can import/export code or access it from development clients.
- Replit project/runtime, Agent, deployment, database, and integration surfaces are not collapsed into one entity.
- Generated code and successful previews are not described as a production-readiness guarantee.
- Secrets, external integrations, publishing, and production data remain explicit trust boundaries.
- The producer relation resolves to Replit, Inc.
