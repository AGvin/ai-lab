# Documentation Requirements

## Requirements

- Identify OpenAI Agents API as OpenAI's producer-operated managed cloud-agent service, introduced in public beta on September 10, 2026.
- Preserve its primary boundary as a hosted agent harness/session/orchestration service for long-running agents, with OpenAI-operated harness infrastructure and selectable OpenAI-hosted, self-hosted, or partner sandbox environments.
- Keep OpenAI Agents SDK as a separate installable software identity; do not collapse the managed Agents API into the SDK merely because both share agent concepts and tooling.
- Keep Codex, ChatGPT Work, underlying models, MCP servers, plugins, skills, tools, vaults, and sandbox-provider services with their canonical owners.
- Treat beta/GA lifecycle, API shape, session semantics, tool inventory, multi-agent behavior, sandbox integrations, quotas, pricing, regions, retention, and operational limits as freshness-sensitive service state.
- Do not generalize customer-reported performance improvements from launch material into independent AI Lab evaluation claims.

## Reader projection

- Render the standard `entity-relations` block from all validated current-entity relations eligible for reader presentation.
- Render the `official-resources` block from canonical references supporting the identity, versioned facts, access context, and stated boundaries of this page.

## Validation

- Agents API remains a hosted infrastructure/service identity rather than an SDK or model.
- Public-beta status is not misreported as general availability.
- OpenAI provenance resolves bidirectionally.
- Hosted and self-hosted sandbox choices do not transfer ownership of the Agents API service itself.

## Scoped original-source qualification — 2026-11-06

- OpenAI introduced the managed Agents API in public beta on 2026-09-10. Current publisher docs describe cloud-hosted agent sessions, long-running harness state, compaction, tool use, multi-agent coordination and environment choices covering OpenAI-hosted, customer-hosted and supported partner sandboxes. This hosted service remains separate from the installable Agents SDK and underlying model identities.
- The public beta API's session configuration, tools, multi-agent limits and sandbox-provider integration are not production GA promises. Published performance examples are customer anecdotes and are not accepted as independent benchmarking; token, tool and sandbox costs, credentials, retention and model/version behavior require exact current service terms.
- Sandbox/agent execution can access files, credentials and network tools, requiring least-privilege capability scoping, auditability and authorized access. OpenAI operating the harness does not make third-party hosted sandboxes OpenAI-owned platforms.
- Verified first-party source 1: https://openai.com/index/introducing-the-agents-api/
- Verified first-party source 2: https://developers.openai.com/api/docs/guides/agents-api/overview
- Gate scope is inherited source identity and current publisher-documented version/rights/operational boundaries, not independent production testing, full freshness/security/legal review, metadata or reader-repair credit, root-wide schema/cache/CI/render, clean pass, final delivery or merge.
