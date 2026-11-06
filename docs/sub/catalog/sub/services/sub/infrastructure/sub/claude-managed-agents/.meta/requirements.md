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

## Scoped original-source qualification — 2026-11-06

- Anthropic documents Claude Managed Agents as a Beta prebuilt managed agent harness rather than the direct Messages API or a standalone trained model. Agent configurations, long-running server-side sessions, environments/sandboxes, tools, files and scheduled agent executions require the managed-agents-2026-04-01 beta header, with some sub-features such as MCP tunnels and dreaming in a narrower preview.
- This stateful product retains session transcripts and related persisted state until explicitly deleted; Anthropic marks Managed Agents not eligible for Zero Data Retention or HIPAA BAA coverage. Even custom or self-hosted sandbox options do not make the whole Managed Agents data path automatically ZDR-eligible.
- Security isolation, tool permissions, credentials, MCP endpoints, pricing, supported model set, API capabilities and beta access are mutable original-provider documentation, not independently tested guarantees.
- Verified first-party source 1: https://platform.claude.com/docs/en/managed-agents/overview
- Verified first-party source 2: https://platform.claude.com/docs/en/managed-agents/quickstart
- Source acceptance covers service identity and publisher-scoped limits, not full lifecycle freshness, authenticated provider execution, independent security/legal assurance, root-wide schema/cache/CI/render, reader repairs, clean passes or final delivery.
