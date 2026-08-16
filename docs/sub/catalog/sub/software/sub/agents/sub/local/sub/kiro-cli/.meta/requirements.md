# Documentation Requirements

## Requirements

- Identify Kiro CLI as a terminal AI development agent for interactive development and automation workflows.
- Preserve Amazon Web Services (AWS) as the canonical producer through the physically materialized `produced-by` relation when the reciprocal AWS `produces` relation resolves successfully.
- Preserve current support for custom agents, subagents, tool approvals, MCP integrations, steering, hooks, and headless use at a high level.
- Keep AWS-specific integrations as capabilities rather than redefining Kiro CLI as an AWS-only agent.
- Keep model, account, authentication, availability, and other mutable service-state claims source-backed when expanded.
- Include current official Kiro CLI documentation and the first-party Kiro provenance reference identifying Amazon Web Services, Inc. as the Kiro service provider.

## Validation

- The AWS/Kiro CLI `produces` / `produced-by` relation pair is physically present at both endpoints and semantically consistent.
- The producer target resolves to the canonical AWS producer node.
- The profile remains about the CLI agent rather than the broader Kiro product family.
- Local terminal execution is not conflated with remote model or external-tool services.
