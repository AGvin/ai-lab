# Documentation Requirements

## Requirements

- Identify Hermes Agent as a self-hostable personal AI agent built by Nous Research.
- Preserve its CLI/desktop and messaging-gateway surfaces, persistent memory, agent-managed skills, scheduled/background workflows, subagent delegation, MCP integration, and configurable model/provider support at a high level.
- Preserve that Hermes can run in user-controlled local, containerized, remote, VPS, SSH, or other self-managed execution environments; do not reduce its identity to one backend or to Nous-hosted execution.
- Preserve the distinction between memory and skills at a stable high level: durable facts/context and reusable procedural workflows have different persistence/loading roles.
- Preserve useful legacy operational boundaries around model/provider credentials, messaging-channel credentials, terminal/browser/file access, memory retention, skill creation/update, MCP server trust, scheduled unattended tasks, subagent access, remote execution, and human approval gates.
- Mention that current Hermes provides approval/gating mechanisms for some memory/skill writes without presenting those controls as a universal security guarantee.
- Keep provider lists, platform counts, tool counts, model availability, hosted gateway options, and other mutable product-state claims source-backed when expanded.
- Include current official Hermes Agent site, documentation, and repository references.
- Preserve Nous Research as the canonical producer through the `produced-by` relation.

## Validation

- The page does not imply that Hermes requires Nous-hosted execution.
- The profile remains about Hermes Agent rather than the Hermes model family.
- Memory, skills, scheduled jobs, subagents, and external tools are treated as explicit persistence/execution trust boundaries.
- Mutable capability counts are not frozen into the canonical identity.
- Official resource links match canonical entity metadata.
