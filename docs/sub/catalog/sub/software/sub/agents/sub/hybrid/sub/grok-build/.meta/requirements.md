# Documentation Requirements

## Requirements

- Present Grok Build as SpaceXAI's coding-agent product spanning an installable terminal/TUI agent and current hosted web/mobile Build surfaces.
- Preserve the Hybrid Agent classification because the open-source terminal harness can run on user-controlled machines and can be compiled/configured for local-first inference, while the current product also has hosted Grok web/mobile execution and subscription-backed model/service surfaces.
- Keep the `grok-build-0.1` trained coding model separate from the Grok Build agent product/harness; model availability inside Grok Build does not make the harness a model identity.
- Keep the open-source agent loop, terminal UI, plan/diff review, subagents, worktrees, skills, plugins, hooks, MCP servers, ACP support, headless mode, workflows, and plugin marketplace as product capabilities/extension surfaces unless a later lifecycle establishes an independently durable product owner.
- Preserve trust boundaries around repository/worktree access, shell/tool approvals, plugin/skill installation, hooks, MCP servers, local configuration, cloud model access, publishing, GitHub export, secrets, and external side effects.
- Treat exact model defaults, plans, hosted web/mobile capabilities, marketplace inventory, workflow limits, release versions, local-inference compatibility, pricing, quotas, and subscription eligibility as freshness-sensitive.
- Render the standard `entity-relations` block from validated current-entity relations.

## Validation

- Grok Build remains distinct from the Grok Build 0.1 trained model.
- The product is not described as purely local or purely hosted when current first-party surfaces support both.
- Plugin/skill marketplace entries are not automatically materialized as peer catalog products.
- Producer provenance resolves to SpaceXAI.
