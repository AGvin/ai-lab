# Documentation Requirements

## Requirements

- Identify OpenAI Codex as OpenAI's coding agent for writing, reviewing, testing, and shipping software across the Codex app, ChatGPT, editor, terminal, automation, and cloud surfaces.
- Preserve the product boundary across the Codex app, ChatGPT workflows, IDE integration, CLI use, SDK or automation entry points, reusable skills/plugins, MCP-connected tools, and delegated cloud tasks without turning the catalog page into feature-by-feature product documentation.
- Distinguish local Codex execution surfaces such as CLI, IDE, and local app workflows from Codex cloud tasks running in OpenAI-managed environments; local tool execution does not imply that model inference or relevant task context remains local.
- Preserve useful legacy trust boundaries around repository/worktree access, shell and external-tool approvals, generated diffs, repository instructions and rules, skills/plugins, MCP servers, browser or Computer Use surfaces, connected services, scheduled/background tasks, secrets, and external actions such as commit, push, deployment, or merge.
- Keep training/data-use behavior surface- and workspace-sensitive: personal-workspace content can be eligible for model improvement according to applicable data controls, business-product inputs/outputs are excluded from training by default subject to documented opt-in exceptions, and Codex full-environment training has a separate Codex setting that must not be conflated with the general ChatGPT training toggle.
- Keep model selection, plan eligibility, limits, credits, Memories, Scheduled Tasks, browser/Computer Use availability, retention, residency, workspace controls, and other mutable product-state claims source-backed and time-scoped when expanded.
- Preserve OpenAI as the canonical producer through the `produced-by` relation.
- Include current official OpenAI Codex product/developer documentation and current Codex/data-controls documentation.

## Validation

- The page does not describe every Codex task as cloud-hosted or every Codex workflow as local.
- Local execution and hosted inference/data paths are not conflated.
- Skills, plugins, MCP, browser/Computer Use, connected services, and automations are represented as extensibility or workflow surfaces, not separate Codex product identities.
- Security wording treats sandboxing, approvals, and review gates as explicit trust controls rather than universal guarantees.
- Codex data-control wording distinguishes general account/workspace controls from the separate full-environment Codex training setting where applicable.
- The profile does not substitute historical Codex model identities for the current Codex coding-agent product.
