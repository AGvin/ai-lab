# Documentation Requirements

## Requirements

- Present Vercel Connect as Vercel's generally available managed integration/authentication platform for giving AI apps and agents scoped runtime access to external tools, data, APIs, OAuth providers, MCP servers, and event triggers.
- Preserve its primary managed-connector job: connector registration, short-lived runtime credentials, delegated/user authorization, scoped resource access, and verified trigger forwarding.
- Keep individual third-party connectors, provider APIs, generic OAuth/API-key credentials, the Vercel AI SDK, AI Gateway, Chat SDK, eve, and provider-specific skills/plugins as integrations or adjacent products rather than peer identities within Connect.
- Do not create one catalog entity per Vercel Connect connector merely because the directory exposes separately addressable integrations.
- Treat connector inventory, managed-vs-preset distinction, supported auth types, triggers, SDK/CLI commands, pricing, plan limits, and availability as freshness-sensitive.
- Render the standard `entity-relations` block from validated current-entity relations.

## Validation

- Vercel Connect remains agent-integration/authentication-first rather than a generic workflow engine or model gateway.
- General availability remains source-backed to Vercel's current launch material.
- Producer provenance resolves bidirectionally to Vercel Inc.
