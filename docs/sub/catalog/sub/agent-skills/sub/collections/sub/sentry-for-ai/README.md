# Sentry for AI

**Sentry for AI** is [Sentry](../../../../../producers/sub/s/sub/sentry/)'s first-party collection of Agent Skills for coding assistants that instrument applications, investigate errors, configure alerts and support application observability. It is a **source repository, not an installable plugin**. Its built distributions are separate from the internal engineering collection [Sentry Skills](../sentry-skills/).

## What the collection provides

The upstream library's core workflows include `sentry-get-started` (orient to an existing Sentry setup), `sentry-instrument` (SDK installation and monitoring signals), and `sentry-debug-issue` (triage issues and investigate errors). Additional workflows cover alerts, OpenTelemetry exporters and other supported products. Shared SDK- and signal-specific references are incorporated into generated client packages. These bundled skills are not separate accepted AI Lab catalog entries.

## Use the generated distribution

The [first-party README](https://github.com/getsentry/sentry-for-ai/blob/80642456253f2fcd529a38d9ac82f299e80dc89c/README.md) explicitly instructs users **not to install this source repository directly**. Instead, the build pipeline generates the portable [Agent Plugin](https://github.com/getsentry/agent-plugin) and client-specific plugins for Claude Code, Cursor, Codex, Copilot, Google Antigravity and Grok. Each distribution has its own installation instructions. The skill library is also available through [skills.sentry.dev](https://skills.sentry.dev).

Source-managed client packages can configure the hosted [Sentry MCP service](https://mcp.sentry.dev) and authenticated Sentry project operations. Some workflows additionally require the GitHub CLI. Confirm exact client support and permissions from the chosen distribution; installing a plugin does not authenticate a Sentry account automatically or authorize edits to unrelated repositories.

## Data, safety and licensing

Instrumented events, traces, logs and issue details may contain confidential or personal data. Use approved projects, scrub sensitive event attributes, restrict credentials and access, and review proposed fixes or alert changes before execution. Client-specific MCP source attribution and installer diagnostics are documented upstream, but do not imply that all clients send identical telemetry. Validate the applicable data-processing terms and organization controls.

The source repository is released under the [MIT license](https://github.com/getsentry/sentry-for-ai/blob/80642456253f2fcd529a38d9ac82f299e80dc89c/LICENSE); Sentry service accounts and third-party project content have separate rights and privacy requirements. No plugin, MCP connection, issue investigation or code modification was executed for this entry.

## Relations

- Produced by: [Sentry](../../../../../producers/sub/s/sub/sentry/)
- Separate collection: [Sentry Skills](../sentry-skills/)

## Official resources

- [Sentry for AI source](https://github.com/getsentry/sentry-for-ai)
- [Pinned source and distribution guide](https://github.com/getsentry/sentry-for-ai/blob/80642456253f2fcd529a38d9ac82f299e80dc89c/README.md)
- [Generated Agent Plugin](https://github.com/getsentry/agent-plugin)
- [Source telemetry documentation](https://github.com/getsentry/sentry-for-ai/blob/80642456253f2fcd529a38d9ac82f299e80dc89c/TELEMETRY.md)
- [MIT license](https://github.com/getsentry/sentry-for-ai/blob/80642456253f2fcd529a38d9ac82f299e80dc89c/LICENSE)
