# Documentation Requirements

## Requirements

- Identify Devin as Cognition AI, Inc.'s hosted software-development agent represented by the canonical development-agent service profile at this path.
- Preserve the service boundary: Devin work executes in managed sessions/workspaces and is not a standalone local coding-agent installation.
- Preserve its ticket/task-driven development role across repository access, code changes, testing, pull requests, review, and other software-delivery workflows.
- Preserve current integration classes at a stable high level: GitHub, GitLab, Bitbucket, Azure DevOps, Jira, Linear, Slack, Microsoft Teams, API/CI workflows, MCP-connected tools, and organization secrets.
- Preserve current automation surfaces at a high level, including scheduled sessions and managed parallel Devin sessions, while treating their exact behavior, limits, and availability as mutable.
- Preserve useful legacy operational boundaries around repository and organization permissions, cloud workspace/session isolation, secrets and credentials, terminal/browser/MCP/API access, scheduled/background execution, deployment permissions, human takeover, and merge/release approval gates.
- Keep pricing, plan limits, model/runtime details, exact integration availability, execution limits, and other mutable service-state claims source-backed and time-scoped when expanded.
- Include current official Devin site and documentation references.
- Render the standard `entity-relations` block from the validated current-entity relation projection.

## Validation

- The page describes Devin as a hosted development-agent service rather than local agent software.
- Scheduled/parallel automation does not remove the need for explicit permission, secret, and review boundaries.
- Integrations are described as access surfaces, not as unlimited permissions.
- Official resource links match canonical entity metadata.
- The `entity-relations` block matches the validated current-entity relation projection and every rendered destination resolves to a canonical node.

## Scoped original-source qualification — 2026-11-07

- Devin is Cognition's hosted software-development agent working in managed sessions: it can read authorized repositories, write and run code, test changes and participate in review/PR workflows. Cognition's separate Devin Desktop software is not the same hosted service identity.
- Official Automations documentation describes event-driven and scheduled sessions with repository, issue-tracker, messaging and webhook triggers. Triggered tasks and integration payloads can be untrusted; secrets, service accounts, workspace isolation, permissions, CI actions, automatic edits and release/merge approval remain explicit operational boundaries.
- Verified first-party source 1: https://docs.devin.ai/get-started/devin-intro
- Verified first-party source 2: https://docs.devin.ai/product-guides/automations
- Verified first-party source 3: https://docs.devin.ai/product-guides/scheduled-sessions
- Scoped service/source acceptance only; no logged-in session, task execution, integration authorization, independent code quality/security validation, complete contract review, whole-repository clean pass or final-delivery gate.
