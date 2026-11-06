# Documentation Requirements

## Requirements

- Identify Browser Use Cloud as the separately operated **fully hosted** Browser Use agent/browser task-execution service with API-driven remote browser/agent sessions, task results, live inspection and account-based billing; distinguish it from the open-source Browser Use framework and self-managed browser servers.
- Preserve current Cloud API V4 hosted agent runs and browser session creation, authenticated API-key access, browser lifetime, asynchronous results, profiles and supported SDK interfaces only where documented in current first-party references. Earlier V3/V2 SDK and API examples are version-scoped, not universal paths, defaults or quotas.
- Distinguish Browser Use Cloud's managed agent/task completion from Browserbase's managed raw browser-session infrastructure, Cloudflare Browser Rendering's account-scoped CDP/data-extraction service and browser automation libraries. A service integration may use another browser backend without becoming the same independently operated product.
- Keep cloud pricing, free/paid quotas, task/session timeouts, concurrency, model provider, security/data retention, region availability, auth, network/proxy behavior and production SLA time-scoped and sourced. Do not embed real API keys or credentials in documentation.
- Keep the Browser Use vendor/brand as producer and preserve inverse producer links without equating source-code authorship with ownership of unrelated downstream browser agents.

## Validation

- Browser Use Cloud and open-source Browser Use software remain separately identifiable deployment/operation boundaries.
- Current API endpoint and operational quota details are explicitly version-dependent.
- The Browser Use producer record reciprocates this exact managed-service identity.

## Scoped original-source qualification — 2026-11-06

- Browser Use Cloud's current first-party quickstart documents API V4 at api.browser-use.com with X-Browser-Use-API-Key, including /api/v4/runs for hosted agent tasks and /api/v4/browsers for managed CDP browser sessions. This supersedes earlier documentation centering API V3; older v2/v3 client examples and resources must not be presented as current defaults.
- The cloud service combines agent-task execution and remotely managed browser infrastructure, but is separate from installable browser-use open-source software and from Browserbase raw browser hosting. Asynchronous agent workflows, session limits, live views, key scopes, billing, proxy controls and data retention depend on the current API and account plan.
- Sessions may expose authentication context, tokens, confidential page data and traces. User intent and access rights for each target website remain essential; neither hosting nor browser automation bypasses target terms or authorization.
- Verified first-party source 1: https://docs.browser-use.com/cloud/quickstart
- Verified first-party source 2: https://docs.browser-use.com/
- Source acceptance covers service identity and publisher-scoped limits, not full lifecycle freshness, authenticated provider execution, independent security/legal assurance, root-wide schema/cache/CI/render, reader repairs, clean passes or final delivery.
