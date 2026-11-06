# Documentation Requirements

## Requirements

- Identify Sentry for AI as Sentry's separately maintained Agent Skills **source library** for assistant-driven Sentry instrumentation, error triage, alert creation and related observability workflows; not the distinct internal `getsentry/skills` collection or a standalone hosted monitoring service.
- Pin first-party `getsentry/sentry-for-ai` source commit `80642456253f2fcd529a38d9ac82f299e80dc89c` (2026-10-30), including README, MIT LICENSE, `mcp.json`, `TELEMETRY.md` and package/build layout. Do not infer the latest published plugin binary or runtime behavior from one source commit.
- Explain the explicit source/distribution split: this repository is **not directly installed**; builds from `src/plugins/<client>/build.sh` generate portable `getsentry/agent-plugin` and client-specific distribution repositories (Claude Code, Cursor, Codex, Copilot, Google Antigravity and Grok). Refer readers to the relevant generated plugin's own instructions. Hosted `skills.sentry.dev` supplies another source-backed distribution path.
- Keep the bundled core skills `sentry-get-started`, `sentry-instrument`, and `sentry-debug-issue` as collection-owned examples. The generated plugins can hydrate shared SDK/signal reference material; individual skills and generated distributions are not additional accepted canonical collection identities.
- Explain dependency boundaries: the source configuration uses hosted Sentry MCP over HTTP and some workflows require GitHub CLI or authenticated Sentry API access. Installing a client plugin does not grant account permissions or execute monitoring operations for this documentation entry.
- Address security and privacy: Sentry event data, error traces, user identifiers, code snapshots and tool output can be sensitive; use authorized projects, scoped credentials, privacy controls and explicit approval for GitHub writes, alert changes or code fixes.
- Note telemetry's source-backed attribution: MCP traffic may contain plugin-specific source tagging for supported clients and installer diagnostics; attribution differs by client, so do not promise complete or uniform telemetry. Check organizational privacy/security settings and applicable service data-processing terms before enabling monitoring.
- Distinguish MIT-licensed source code from vendor service terms, private customer incident data, SDK dependencies and third-party plugin distribution rights. Never claim complete data deletion, guaranteed privacy or full network-offline operation.
- Preserve reciprocal Sentry producer relation and one parent collection index entry, with a concise cross-reference to the independent Sentry Skills collection.

## Validation

- [Pinned upstream README](https://github.com/getsentry/sentry-for-ai/blob/80642456253f2fcd529a38d9ac82f299e80dc89c/README.md), [MIT license](https://github.com/getsentry/sentry-for-ai/blob/80642456253f2fcd529a38d9ac82f299e80dc89c/LICENSE), [MCP source config](https://github.com/getsentry/sentry-for-ai/blob/80642456253f2fcd529a38d9ac82f299e80dc89c/mcp.json) and [telemetry notes](https://github.com/getsentry/sentry-for-ai/blob/80642456253f2fcd529a38d9ac82f299e80dc89c/TELEMETRY.md) support installation and risk boundaries.
- [Generated Agent Plugin distribution](https://github.com/getsentry/agent-plugin) independently confirms build provenance.
- Reciprocal producer and local collection links resolve. The collection is indexed once and no generated distribution or bundled skill is counted as another accepted candidate.
- No authenticated Sentry account, plugin installation, API call, monitored event access, telemetry inspection, full source audit, runtime validation, full CI or whole-catalog clean pass was performed.
