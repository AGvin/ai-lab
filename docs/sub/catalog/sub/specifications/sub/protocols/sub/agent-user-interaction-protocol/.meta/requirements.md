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

## Scoped original-source qualification — 2026-11-07

- AG-UI is an open event-based agent-to-user interface interoperability protocol, maintaining ordered run lifecycle, text/tool-call events, state changes and frontend interaction semantics between an agent runtime and user-facing application.
- The first-party event model and repository distinguish frontend streaming from MCP tool/context access and A2A inter-agent delegation. Event types, transport framing (for example SSE or WebSockets), SDK-specific adapters, optional subagent events and versioned capabilities require release-scoped evaluation; a conforming event stream alone does not authorize browser/user tool actions.
- Verified first-party source 1: https://github.com/ag-ui-protocol/ag-ui/blob/main/docs/introduction.mdx
- Verified first-party source 2: https://github.com/ag-ui-protocol/ag-ui/blob/main/docs/concepts/events.mdx
- Verified first-party source 3: https://github.com/ag-ui-protocol/ag-ui
- Existing protocol identity/source qualification only; no frontend, streaming runtime, client interoperability, human consent, delegated tool execution or independent security/privacy/legal audit, root-wide schema/cache/CI/render, clean/final or merge credit.
