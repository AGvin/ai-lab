# Documentation Requirements

## Requirements

- Present Composio as a producer-operated integration platform that gives AI agents and applications managed access to external applications and tools.
- Cover tool discovery, authentication/connected accounts, tool execution, hosted MCP surfaces, and framework/client integrations only where current first-party documentation supports them.
- Keep individual third-party applications and their APIs with their own owners; availability through Composio does not make them Composio products.
- Keep SDKs, CLI surfaces, and plugins as access mechanisms of the service unless they establish an independently complete self-managed product identity.
- Treat integration counts, supported apps, tool counts, plans, and availability as freshness-sensitive claims.
- Render the standard `entity-relations` block from validated current-entity relations.

## Validation

- The profile is clearly a managed agent-integration service rather than a generic agent framework.
- Third-party integration provenance is not collapsed into Composio ownership.
- Producer provenance resolves to the canonical Composio producer node.

## Scoped original-source qualification — 2026-11-06

- Composio is managed connected-account authentication and agent/tool execution, not the owner of third-party apps. Its documentation explains per-user connected accounts, server-side provider token injection and redacted credential fields. The May-July 2026 migration requires Composio-managed redirectable OAuth connections to use hosted Connect Link authentication; custom OAuth configs and non-OAuth methods remain distinct.
- Agent requests must be scoped to the correct stable user ID, toolkit permissions and active connected account; leaked keys, cross-user access and revoked connections require explicit access checks. Upstream provider tokens should not be copied into agent prompts or repository files; verify actual account entitlements and link flow.
- Verified first-party source 1: https://docs.composio.dev/docs/authentication
- Verified first-party source 2: https://docs.composio.dev/docs/auth-configuration/connected-accounts
- Verified first-party source 3: https://docs.composio.dev/reference/changelog
- This is a bounded identity/source qualification, not live service execution, credential review, security/privacy certification, complete license/ownership clearance, independent benchmarking, full schema/cache/CI/render, clean-group acceptance or final-delivery credit.
