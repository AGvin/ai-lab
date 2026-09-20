# Documentation Requirements

## Requirements

- Identify Google Antigravity as Google's current standalone agent-first application represented by the Antigravity 2.0 product surface, with the Antigravity CLI as a supported terminal surface for the same current agent runtime.
- Keep Antigravity 2.0 distinct from the separately shipped Antigravity IDE. Do not silently merge IDE-specific lifecycle or UI facts into the standalone Antigravity 2.0 identity.
- Keep the current execution-boundary classification under Local Agents: the released desktop/CLI product operates against user-selected local folders, repositories, projects, worktrees, tools, skills, MCP servers, hooks, and permissions. Hosted model inference or Google Cloud commercial access alone does not make the agent execution surface hybrid.
- Preserve the current first-party roadmap boundary: Google's 2026 launch material describes cloud-deployed agents as future work. If a material managed agent-execution surface becomes generally available later, re-evaluate Local versus Hybrid ownership rather than pre-classifying roadmap functionality as current.
- Cover the current product's agent orchestration surfaces only at identity level: synchronous/asynchronous agents, dynamic subagents, projects, scheduled tasks, skills, MCP, hooks, CLI, and related runtime controls belong here as product capabilities rather than independent catalog identities unless they later clear the intake gates separately.
- Treat the Antigravity SDK separately as a preview developer surface unless its lifecycle and independent identity later justify its own canonical node.
- Keep model availability, quotas, plans, organization access, release numbers, supported operating systems, and enterprise/GCP terms freshness-sensitive and source-backed when expanded.
- Render producer relation and official resources only during the final render phase.

## Validation

- The profile does not describe future cloud-deployed agents as a currently released managed execution mode.
- The Antigravity IDE is not conflated with the standalone Antigravity 2.0 application.
- Remote model inference or enterprise billing is not used by itself as evidence of Hybrid Agent classification.
- Product capabilities such as Skills, MCP, Scheduled Tasks, hooks, CLI, and subagents are not duplicated as standalone product identities without independent intake evidence.
