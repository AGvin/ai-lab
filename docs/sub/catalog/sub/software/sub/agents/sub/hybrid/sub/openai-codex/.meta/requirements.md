# Documentation Requirements

## Requirements

- Identify OpenAI Codex as OpenAI's coding agent for writing, reviewing, testing, and shipping software across the Codex app, ChatGPT, editor, terminal, automation, and cloud surfaces.
- Preserve the product boundary across the Codex app, ChatGPT workflows, IDE integration, CLI use, SDK or automation entry points, reusable skills/plugins, MCP-connected tools, and delegated cloud tasks without turning the catalog page into feature-by-feature product documentation.
- Distinguish local Codex execution surfaces such as CLI, IDE, and local app workflows from Codex Cloud tasks running on OpenAI-managed computers. Cloud tasks use published project environments and isolated per-task workspaces; new tasks do not recover another task's uncommitted files. Local tool execution does not imply that inference or relevant task context remains local.
- Preserve useful legacy trust boundaries around repository/worktree access, shell and external-tool approvals, generated diffs, repository instructions and rules, skills/plugins, MCP servers, browser or Computer Use surfaces, connected services, scheduled/background tasks, secrets, and external actions such as commit, push, deployment, or merge.
- Keep training/data-use behavior surface- and workspace-sensitive: personal-workspace content can be eligible for model improvement according to applicable data controls, business-product inputs/outputs are excluded from training by default subject to documented opt-in exceptions, and Codex full-environment training has a separate `Include environments` setting that the ChatGPT training toggle does not change.
- Keep model selection, plan eligibility, limits, credits, Memories, Scheduled Tasks, browser/Computer Use availability, retention, residency, workspace controls, and other mutable product-state claims source-backed and time-scoped when expanded.
- Distinguish the current Codex Cloud task experience from Codex Cloud (Legacy) integrations, including existing Code Review, Security Review, and some GitHub/Linear workflows; do not mislabel all cloud executions as the same environment generation.
- Record cloud environment repository authorization, sharing of prepared files/credentials, task-specific workspace isolation, network/secret exposure and saved-VM recovery windows as separate operational boundaries; do not confuse VM recovery with conversation retention.
- Render the standard `entity-relations` block from the validated current-entity relation projection.
- Include current official OpenAI Codex product/developer documentation and current Codex/data-controls documentation.

## Validation

- The page does not describe every Codex task as cloud-hosted or every Codex workflow as local.
- Local execution and hosted inference/data paths are not conflated.
- Published cloud environments, per-task workspace state, legacy cloud integrations, and local tasks are not presented as interchangeable execution or retention scopes.
- Skills, plugins, MCP, browser/Computer Use, connected services, and automations are represented as extensibility or workflow surfaces, not separate Codex product identities.
- Security wording treats sandboxing, approvals, and review gates as explicit trust controls rather than universal guarantees.
- Codex data-control wording distinguishes general account/workspace controls from the separate full-environment Codex training setting where applicable.
- The profile does not substitute historical Codex model identities for the current Codex coding-agent product.
- The `entity-relations` block matches the validated current-entity relation projection and every rendered destination resolves to a canonical node.
