# Documentation Requirements

## Requirements

- Present Microsoft Entra Agent ID as an agent-specific managed identity/access product for creating, authenticating, authorizing, and governing AI-agent identities.
- Keep delegated/autonomous access, agent identity lifecycle, token/credential controls, Conditional Access, and identity protection as capabilities of the same identity-first service.
- Distinguish Entra Agent ID from general Entra workforce/CIAM identities and from broad AI-management or AI-security control planes.
- Treat availability, licensing, supported identity flows, limits, and integration coverage as freshness-sensitive.
- Render the standard `entity-relations` block from validated current-entity relations.

## Validation

- The entity remains agent identity/access-first rather than tool-integration or generic IAM ownership.
- Producer provenance resolves to Microsoft.

## Scoped original-source qualification — 2026-11-06

- Microsoft Entra Agent ID adds agent identities and agent-identity blueprints to Microsoft's identity platform, including authentication, delegated/autonomous authorization, lifecycle governance and logging. It integrates with third-party agent frameworks using Microsoft identity federation and compatible SDKs, but is not Microsoft Agent 365's entire governance product.
- Microsoft's current original documentation differentiates basic Agent ID availability for Entra customers from additional protection/governance feature licensing that requires Microsoft Agent 365. Enterprise Conditional Access, risk protection, sign-in policy and audit cannot be assumed fully enabled just because an agent identity exists.
- OAuth 2.0, MCP and agent-to-agent protocol support describes identity/integration mechanisms, not permission to access tenant data or a universal zero-trust guarantee. Tenant, role, delegation, licensing, quotas and regulatory requirements need separate validation.
- Verified first-party source 1: https://learn.microsoft.com/en-us/entra/agent-id/what-is-microsoft-entra-agent-id
- Verified first-party source 2: https://learn.microsoft.com/en-us/entra/agent-id/
- Source acceptance credits the existing identity and provider-scoped capability boundaries only; no new entity or metadata, independently tested OAuth/IAM behavior, full freshness/privacy/legal/security audit, whole-repository schema/cache/CI/render, reader repair, clean pass, final gate or merge.
