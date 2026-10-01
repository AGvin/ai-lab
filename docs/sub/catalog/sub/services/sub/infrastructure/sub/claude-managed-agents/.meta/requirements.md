# Documentation Requirements

## Requirements

- Present Claude Managed Agents as Anthropic's beta managed agent harness and infrastructure for long-running/asynchronous autonomous-agent sessions.
- Preserve the managed execution boundary: Anthropic provides the agent harness, session lifecycle, sandbox state, files/outputs, prompt caching/compaction, built-in execution surfaces, and optional multi-agent orchestration.
- Keep Claude model identities, Messages API, Claude Code, Anthropic Agent Skills, and self-hosted/custom agent loops separate from this managed-service identity.
- Preserve current beta lifecycle and `managed-agents-2026-04-01` access contract; do not imply GA.
- Treat built-in tools, sandbox/environment options, MCP tunnels, dreaming, memory stores, data-retention eligibility, rate limits, pricing, CLI commands, and beta headers as freshness-sensitive.
- Render the standard `entity-relations` block from validated current-entity relations.

## Validation

- Claude Managed Agents remains a producer-hosted managed infrastructure/service identity rather than an installable agent framework.
- Beta status and data-retention boundaries remain explicit.
- Producer provenance resolves bidirectionally to Anthropic.
