# Documentation Requirements

## Requirements

- Identify WorkOS Agent Auth as WorkOS's agent-specific identity and access service within AuthKit, released in early access in September 2026.
- Preserve its primary product boundary around first-class agent identities, reusable blueprints, delegated and autonomous agent instances, revocable sessions, and short-lived scoped credentials.
- Preserve Agent Registration as a related agent-authentication capability for programmatic clients obtaining identity and credentials through WorkOS-managed discovery and registration flows; do not materialize Agent Registration as a peer product unless upstream lifecycle establishes an independently durable product boundary.
- Keep WorkOS Fine-Grained Authorization, generic user OAuth/SSO, M2M applications, AuthKit user authentication, and WorkOS Connect with their own product/capability boundaries.
- Treat early-access availability, supported identity modes, token/refresh behavior, permission semantics, registration identity types, trust levels, API endpoints, limits, and dashboard configuration as freshness-sensitive.
- Keep WorkOS CLI agent mode and generated auth guidance as integration surfaces rather than separate agent-auth products.
- Preserve WorkOS producer provenance through canonical relations.

## Validation

- WorkOS Agent Auth remains identity/access-first rather than an integration platform or generic IAM profile.
- Early-access status is not misreported as GA.
- Producer provenance resolves bidirectionally to WorkOS.
- Generic AuthKit/OAuth capabilities are not duplicated as standalone agent products solely because Agent Auth uses them.

## Scoped original-source qualification — 2026-11-06

- WorkOS's official September 2, 2026 changelog documents Agent Auth as early access, with first-class agent identity inside AuthKit. The current product guide requires that Agent Auth be enabled for a tenant and distinguishes agent Blueprints, Instances (delegated user versus autonomous organization principal), revocable Sessions and short-lived scoped tokens.
- WorkOS's agent-authenticated blueprint and mint APIs are backend operations authenticated by a server-side WorkOS API key; first-party agent identities are not identical to the separate Agent Registration protocol for outside agent clients. Do not expose secret API keys in browser/agent prompts or equate a minted scope with permission beyond organization/user ceilings.
- Refresh tokens, revocation, role permissions, registration trust, API shape and tenant availability are feature/version sensitive; early-access identity services are not to be labeled GA or inferred as unrestricted runtime governance.
- Verified first-party source 1: https://workos.com/docs/authkit/agent-blueprints
- Verified first-party source 2: https://workos.com/changelog/agent-auth
- Verified first-party source 3: https://workos.com/docs/authkit/agent-registration
- Source acceptance credits the existing identity and provider-scoped capability boundaries only; no new entity or metadata, independently tested OAuth/IAM behavior, full freshness/privacy/legal/security audit, whole-repository schema/cache/CI/render, reader repair, clean pass, final gate or merge.
