# Documentation Requirements

## Requirements

- Present Vercel Connect as Vercel's generally available managed integration/authentication platform for giving AI apps and agents scoped runtime access to external tools, data, APIs, OAuth providers, MCP servers, and event triggers.
- Preserve its primary managed-connector job: connector registration, short-lived runtime credentials, delegated/user authorization, scoped resource access, and verified trigger forwarding.
- Keep individual third-party connectors, provider APIs, generic OAuth/API-key credentials, the Vercel AI SDK, AI Gateway, Chat SDK, eve, and provider-specific skills/plugins as integrations or adjacent products rather than peer identities within Connect.
- Do not create one catalog entity per Vercel Connect connector merely because the directory exposes separately addressable integrations.
- Treat connector inventory, managed-vs-preset distinction, supported auth types, triggers, SDK/CLI commands, pricing, plan limits, and availability as freshness-sensitive.
- Render the standard `entity-relations` block from validated current-entity relations.

- Preserve the launch material's current general-availability effective date of 2026-08-25; distinguish that update from the original June announcement date.

## Validation

- Vercel Connect remains agent-integration/authentication-first rather than a generic workflow engine or model gateway.
- General availability remains source-backed to Vercel's current launch material.
- Producer provenance resolves bidirectionally to Vercel Inc.

## Scoped original-source qualification — 2026-11-06

- Vercel Connect reached general availability on 2026-08-25, distinct from its June 2026 beta announcement. It manages external service connectors using scoped, short-lived runtime tokens and project/environment attachment; the provider documents revoke capability and verified webhook forwarding. Some trigger integrations were documented as beta even after the overall Connect service GA.
- Validate connector permissions, runtime identity, authorization scope and environment isolation per provider. A managed connector token does not grant unlimited access to every external resource; do not treat individual connector, Vercel AI SDK or AI Gateway as additional Connect identities.
- Verified first-party source 1: https://vercel.com/changelog/vercel-connect-ga
- Verified first-party source 2: https://vercel.com/changelog/vercel-connect-secure-access-to-external-services-for-your-agents
- Verified first-party source 3: https://vercel.com/docs/connect
- This is a bounded identity/source qualification, not live service execution, credential review, security/privacy certification, complete license/ownership clearance, independent benchmarking, full schema/cache/CI/render, clean-group acceptance or final-delivery credit.
