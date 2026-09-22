# Documentation Requirements

## Requirements

- Identify OpenAI Agents API as OpenAI's producer-operated managed cloud-agent service, introduced in public beta on September 10, 2026.
- Preserve its primary boundary as a hosted agent harness/session/orchestration service for long-running agents, with OpenAI-operated harness infrastructure and selectable OpenAI-hosted, self-hosted, or partner sandbox environments.
- Keep OpenAI Agents SDK as a separate installable software identity; do not collapse the managed Agents API into the SDK merely because both share agent concepts and tooling.
- Keep Codex, ChatGPT Work, underlying models, MCP servers, plugins, skills, tools, vaults, and sandbox-provider services with their canonical owners.
- Treat beta/GA lifecycle, API shape, session semantics, tool inventory, multi-agent behavior, sandbox integrations, quotas, pricing, regions, retention, and operational limits as freshness-sensitive service state.
- Do not generalize customer-reported performance improvements from launch material into independent AI Lab evaluation claims.

## Validation

- Agents API remains a hosted infrastructure/service identity rather than an SDK or model.
- Public-beta status is not misreported as general availability.
- OpenAI provenance resolves bidirectionally.
- Hosted and self-hosted sandbox choices do not transfer ownership of the Agents API service itself.
