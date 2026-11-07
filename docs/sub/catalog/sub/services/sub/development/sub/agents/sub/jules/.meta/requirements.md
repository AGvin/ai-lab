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
- Render the standard `entity-relations` block from the validated current-entity relation projection.

## Validation

- The page describes Jules as a hosted development-agent service rather than local agent software.
- CLI and API access are described as control/integration surfaces for managed Jules sessions, not as evidence of local Jules execution.
- API keys, repository permissions, and plan/merge approvals remain explicit trust boundaries.
- Official resource links match canonical entity metadata.
- The `entity-relations` block matches the validated current-entity relation projection and every rendered destination resolves to a canonical node.

## Scoped original-source and lifecycle qualification — 2026-11-07

- Google announced on **2026-10-29** that Jules will wind down on **2026-12-31** as part of consolidating agentic coding. Customers may finish existing sessions until **2026-11-11**; after that date, the service is read-only through shutdown. Previously documented hosted session/API/CLI capabilities are historical/product capabilities, not an assurance of new task availability after cutoff or a sustainable future production integration.
- Google provides a local export path for settings, connected repositories, environment variables, scheduled tasks, memories, session activities and code patches. Exported files may contain credentials/secrets: protect them and rotate keys when warranted. GitHub branches, commits and PRs remain with GitHub and are not equivalent to exporting Jules task context.
- Verified first-party source: https://jules.google/docs/changelog/
- Existing distinct service identity and currently official retirement notice accepted as source-qualification only; no authenticated export, account audit, API execution, security/privacy/compliance verification, full repository clean pass or final gate.
