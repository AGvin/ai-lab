# Documentation Requirements

## Requirements

- Identify Agno as the canonical software profile for the open-source Python agent framework represented at this path.
- Describe its role in building and running agents and agentic systems without collapsing the separate AgentOS production/runtime surface into a different product identity unless the catalog later models it separately.
- Render the standard `entity-relations` block from the validated current-entity relation projection.
- Include official Agno website and documentation references.
- Keep framework capabilities, supported integrations, deployment behavior, and mutable runtime details source-backed when expanded.
- Preserve the upstream SDK / AgentOS runtime / AgentOS UI boundary: the Python SDK defines agents, teams, tools and workflows; AgentOS serves them as a service; the UI manages the platform. Do not imply that cloud hosting or the UI is required for SDK usage or that the existing framework family requires a duplicate software node.
- Document operational default risks for AgentOS: JWT authorization must be deliberately enabled, JWT audience verification is configurable, per-user JWT data isolation is opt-in, and custom endpoint scopes, shared mutable tool objects and reverse-proxy protections require separate review; source these from current official security documentation.
- For multi-user deployments, configure JWT verification and least-privilege scopes, set user isolation for JWT callers, audit shared resources and database permissions, and explicitly approve sensitive tools with HITL where appropriate. Do not treat advertised RBAC as automatically securing an unconfigured runtime.
- Keep optional telemetry and private data boundaries source-backed: the current upstream README describes an agent-run telemetry event without prompts/messages/outputs and the `AGNO_TELEMETRY=false` opt-out. Verify deployment-specific behavior and retention before promising privacy.

## Validation

- Official resource links match canonical entity metadata.
- The page remains a concrete software profile rather than a generic agent-framework index.
- The page contains no temporary-placeholder wording.
- The `entity-relations` block matches the validated current-entity relation projection and every rendered destination resolves to a canonical node.
