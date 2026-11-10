# Documentation Requirements

## Requirements

- Identify Sentry as the first-party software publisher operating the Sentry debugging/observability platform and owning the `getsentry` source organization; do not invent a legal-entity suffix or conflate the hosted product with its separately published Agent Skills.
- Preserve two independently maintained, frozen-candidate collections: **Sentry Skills** (`getsentry/skills`, largely internal Sentry engineering workflows) and **Sentry for AI** (`getsentry/sentry-for-ai`, source library for assistant plugins helping developers instrument Sentry and debug issues).
- Record exactly two reciprocal `produces` / `produced-by` relationships; neither packaged skill, vendored example, generated client plugin, shared Sentry MCP interface, or installable distribution repo is automatically a third accepted canonical identity.
- Preserve each collection's separate permission, distribution, source and license boundary: Sentry Skills declares Apache-2.0, Sentry for AI declares MIT; vendor-hosted Sentry service agreements, authentication scopes, monitored event content and third-party code remain separate.
- Ground current publishing status in Sentry's official repository and pinned first-party README/manifest snapshots rather than assuming that the different skill collections have identical audiences, dependencies, clients or releases.
- Do not claim that making a skill repository public authorizes use of private Sentry projects, production error data, GitHub writes or monitoring accounts. Credentialed operations and production changes require explicit access control and authorization.

## Validation

- [Sentry source](https://github.com/getsentry/sentry), [Sentry Skills](https://github.com/getsentry/skills/blob/0c464f411bdfb8d4c12314b36264d06cb2f60270/README.md) and [Sentry for AI](https://github.com/getsentry/sentry-for-ai/blob/80642456253f2fcd529a38d9ac82f299e80dc89c/README.md) establish publisher and separate workflows.
- The two collection nodes link back to the same producer identity; the Producers S index lists Sentry once.
- No authenticated Sentry session, plugin installation, data capture, credentialed API call, full dependency audit, full CI or whole-catalog clean pass is claimed.
