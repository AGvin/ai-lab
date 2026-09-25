# Documentation Requirements

## Requirements

- Present Agent User Interaction Protocol (AG-UI) as an open, lightweight, event-based protocol for bidirectional communication between agentic backends and user-facing applications.
- Preserve AG-UI's interaction-layer role: it standardizes agent state, UI intent, streamed output, and user interaction flows between frontends and agents.
- Distinguish AG-UI from Model Context Protocol and Agent2Agent Protocol: MCP connects agents/applications to tools and context, A2A coordinates agents with agents, and AG-UI connects agents with user-facing applications; real systems may combine them.
- Treat event types, transport details, SDK bindings, package versions, and framework-specific integrations as version-sensitive implementation details and verify them against current official documentation before making normative claims.
- Keep individual SDK and framework integration behavior separate from the protocol identity.

## Validation

- AG-UI is not described as a replacement for MCP or A2A.
- Event-level or transport-sensitive claims are traceable to current official AG-UI documentation.
- Package release versions are not presented as the protocol identity itself.
