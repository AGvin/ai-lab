# Documentation Requirements

## Requirements

- Identify Hermes Agent as an open-source personal AI agent built by Nous Research, with both self-managed runtime deployment and first-party managed Hermes Cloud agent execution.
- Preserve its CLI/desktop and messaging-gateway surfaces, persistent memory, agent-managed skills, scheduled/background workflows, subagent delegation, MCP integration, and configurable model/provider support at a high level.
- Preserve local, containerized, SSH, VPS, and other user-operated agent execution alongside Nous Research-operated Hermes Cloud instances, and distinguish cloud model inference from actual vendor-managed agent execution.
- Preserve the distinction between memory and skills at a stable high level: durable facts/context and reusable procedural workflows have different persistence/loading roles.
- Preserve useful legacy operational boundaries around model/provider credentials, messaging-channel credentials, terminal/browser/file access, memory retention, skill creation/update, MCP server trust, scheduled unattended tasks, subagent access, remote execution, and human approval gates.
- Mention the optional memory/skill write gates: `memory.write_approval` and `skills.write_approval` default to false. When enabled, the memory gate uses foreground CLI approval or stages writes from other surfaces, while skill writes are staged for review. Do not present these persistence controls as a universal security guarantee.
- Keep provider lists, platform counts, tool counts, model availability, Hermes Cloud access, terms, and other mutable product-state claims source-backed when expanded.
- Render the standard `entity-relations` block from the validated current-entity relation projection.
- Include current official Hermes Agent site, documentation, and repository references.

## Validation

- The page explicitly distinguishes optional Nous-hosted Hermes Cloud agents from local and operator-managed remote execution without implying either mode is mandatory.
- The profile remains about Hermes Agent rather than the Hermes model family.
- Memory, skills, scheduled jobs, subagents, and external tools are treated as explicit persistence/execution trust boundaries.
- Mutable capability counts are not frozen into the canonical identity.
- Official resource links match canonical entity metadata.
- The `entity-relations` block matches the validated current-entity relation projection and every rendered destination resolves to a canonical node.
