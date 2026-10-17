# Documentation Requirements

## Requirements

- Present Claude Agent SDK as Anthropic's installable SDK/runtime for building autonomous Claude agents with an agent loop, tool execution, sessions, built-in tools, hooks, MCP integration, and related runtime primitives in a developer-operated process.
- Preserve the execution boundary: the SDK process and tools are user-operated, while model inference uses Claude through supported provider access paths.
- Keep Claude Code as the coding-agent product, Claude Managed Agents as Anthropic-hosted infrastructure, and ordinary Anthropic client SDKs / Messages API as lower-level API clients.
- Treat supported languages, package versions, session behavior, bundled runtime dependencies, workflow features, tool APIs, telemetry, provider compatibility, and version floors as freshness-sensitive.
- Do not infer that local tool execution means model inference or all agent data remains local.
- Render the standard `entity-relations` block from validated current-entity relations.

## Validation

- Claude Agent SDK remains agent-framework/runtime software rather than Claude Code or Managed Agents.
- User-operated agent execution and hosted model inference are not conflated.
- Producer provenance resolves bidirectionally to Anthropic.
