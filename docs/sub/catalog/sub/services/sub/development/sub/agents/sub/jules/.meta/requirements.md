# Documentation Requirements

## Requirements

- Identify Jules as Google's hosted asynchronous coding-agent service represented by the canonical development-agent service profile at this path.
- Preserve the service boundary: Jules executes coding sessions in Google-managed environments even when controlled through the web app, Jules Tools CLI, REST API, GitHub issue workflows, or external automation.
- Preserve its software-development scope at a high level, including planning, bug fixes, feature work, documentation, tests, code review, and repository-connected tasks.
- Preserve current integration surfaces at a stable high level: GitHub repositories and issues, web sessions, Jules Tools CLI, REST API, and API-driven integrations or CI/CD workflows.
- Preserve current plan/session approval semantics at a high level, including the ability for workflows to require explicit plan approval before execution.
- Preserve useful legacy operational boundaries around GitHub repository permissions, API keys, account access, generated changes and tests, task scope, external workflow integrations, and human review before merge/deploy/release.
- Keep model versions, plan eligibility, quotas, pricing, API versions, integration availability, and other mutable service-state claims source-backed and time-scoped when expanded.
- Include current official Jules site, documentation, CLI/API references.
- Link the canonical Google producer.

## Validation

- The page describes Jules as a hosted development-agent service rather than local agent software.
- CLI and API access are described as control/integration surfaces for managed Jules sessions, not as evidence of local Jules execution.
- API keys, repository permissions, and plan/merge approvals remain explicit trust boundaries.
- Official resource links match canonical entity metadata.
