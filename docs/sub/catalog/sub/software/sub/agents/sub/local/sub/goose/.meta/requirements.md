# Documentation Requirements

## Requirements

- Identify goose as an open-source, local-first general-purpose AI agent with desktop, CLI, and API surfaces.
- Preserve that goose runs on the user's machine and can be used for coding, workflows, research, writing, automation, data analysis, and other tool-driven tasks.
- Preserve provider and extension flexibility at a high level without freezing mutable provider or extension counts.
- Preserve the current protocol boundary at a high level: ACP is used for agent/client interoperability while MCP remains the primary extension/tool integration mechanism.
- Preserve useful legacy operational boundaries around local filesystem and shell access, extension/tool scopes, provider credentials and data flow, desktop/API exposure, prompt-injection risk, human approval controls, and sandboxing for sensitive repositories or private data.
- Record provenance accurately: goose was founded and originally developed by Block and is now stewarded by the Agentic AI Foundation at the Linux Foundation.
- Preserve Block as the producer/origin through the canonical `produced-by` relation.
- Preserve Agentic AI Foundation as the maintainer/steward through the canonical `maintained-by` relation.
- Include the current official goose repository and documentation references.

## Validation

- Block is represented as the producer/origin, not the current steward.
- Agentic AI Foundation is represented as the current maintainer/steward, not the original producer.
- The page does not describe goose as coding-only or as requiring one model provider.
- ACP and MCP are not conflated into the same integration role.
- Local-first execution is not described as eliminating provider, tool, or extension data-exposure risks.
