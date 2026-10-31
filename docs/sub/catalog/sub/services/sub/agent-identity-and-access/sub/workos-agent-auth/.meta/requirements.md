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
