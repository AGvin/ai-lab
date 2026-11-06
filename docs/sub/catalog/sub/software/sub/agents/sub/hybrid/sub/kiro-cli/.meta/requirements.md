# Documentation Requirements

## Requirements

- Identify Kiro CLI as the licensed Kiro terminal AI development agent supporting both local execution and managed Cloud Sessions, including interactive development and headless automation.
- Render the standard `entity-relations` block from the validated current-entity relation projection.
- Preserve current support for custom agents, subagents, tool approvals, MCP integrations, steering, hooks, Skills, headless automation, and optional V3-only features at a high level without promising one feature set across all versions.
- Keep AWS-specific integrations as capabilities rather than redefining Kiro CLI as an AWS-only agent.
- Distinguish default local agent/tool execution from `kiro-cli --cloud` managed cloud-sandbox execution; Cloud Sessions span Kiro CLI, IDE, Web, and mobile surfaces without creating a second CLI identity.
- Keep model, account, authentication, cloud-session eligibility/enterprise controls, configuration sync, sandbox security, pricing, license, availability, CLI release versions, and other mutable state claims source-backed when expanded.
- Include current official Kiro CLI documentation and the first-party Kiro provenance reference identifying Amazon Web Services, Inc. as the Kiro service provider.

## Validation

- The profile remains about the CLI agent rather than the broader Kiro product family.
- Local terminal execution is not conflated with remote model or external-tool services.
- Vendor-operated Cloud Sessions are identified as hosted agent-loop execution, not merely remote model inference, while optional sandbox permissions and configuration sync are treated as trust boundaries rather than security guarantees.
- The `entity-relations` block matches the validated current-entity relation projection and every rendered destination resolves to a canonical node.
