# Documentation Requirements

## Requirements

- Identify Browser Use Cloud as the separately operated **fully hosted** Browser Use agent/browser task-execution service with API-driven remote browser/agent sessions, task results, live inspection and account-based billing; distinguish it from the open-source Browser Use framework and self-managed browser servers.
- Preserve published API v3 session/task creation, authenticated API-key access, remote browser/session lifetime, asynchronous result/status retrieval, browser profiles and supported SDK interfaces only as documented in current first-party references. Older first-party guides may mention v2; scope those by release rather than treating every API path and task limit as universal.
- Distinguish Browser Use Cloud's managed agent/task completion from Browserbase's managed raw browser-session infrastructure, Cloudflare Browser Rendering's account-scoped CDP/data-extraction service and browser automation libraries. A service integration may use another browser backend without becoming the same independently operated product.
- Keep cloud pricing, free/paid quotas, task/session timeouts, concurrency, model provider, security/data retention, region availability, auth, network/proxy behavior and production SLA time-scoped and sourced. Do not embed real API keys or credentials in documentation.
- Keep the Browser Use vendor/brand as producer and preserve inverse producer links without equating source-code authorship with ownership of unrelated downstream browser agents.

## Validation

- Browser Use Cloud and open-source Browser Use software remain separately identifiable deployment/operation boundaries.
- Current API endpoint and operational quota details are explicitly version-dependent.
- The Browser Use producer record reciprocates this exact managed-service identity.
