# Documentation Requirements

## Requirements

- Use the reader-facing title `Using AI Plugins` and preserve the source guide's complete operational lifecycle: identify the ecosystem, inspect the package, choose/install with least privilege, verify actual installed behavior, update safely, disable/remove completely, and troubleshoot residual/failed components.
- Begin by requiring the target host/ecosystem to be identified before any command or manifest assumption. Use current examples such as OpenAI/ChatGPT/Codex, Claude Code, Cursor, and OpenCode only as sourced examples; state that similar capabilities do not imply compatible package formats.
- Preserve the pre-install inventory: plugin name, publisher/source/version/commit, host, marketplace, bundled skills, agents/commands, hooks, MCP servers, connectors/OAuth scopes, executable code, network destinations, writable paths, update policy, and uninstall behavior.
- Require review of the complete package rather than marketplace marketing, emphasizing startup/lifecycle hooks, shell/install code, MCP configuration, external assets, telemetry, credential requirements, and any generated configuration.
- Preserve three installation models: host marketplace, direct repository/URL installation, and local-development installation. Explain trade-offs and that a marketplace/installer is distribution, not independent trust review. Exact commands are host-specific and must be freshness-checked against official docs.
- Preserve least-privilege setup: disable unnecessary connectors, read-only credentials where possible, filesystem restriction, approval for shell/write operations, disposable/test workspace first, secrets outside plugin directory, and review/deny optional telemetry until understood.
- Explain that Markdown-only plugins can still change model/agent behavior, while hooks/code expand the executable boundary.
- Preserve platform examples for Claude Code, OpenAI Codex/ChatGPT supported surfaces, Cursor, and OpenCode, but render/update their commands, namespaces, UI surfaces, and availability only from current official sources. Explicitly warn that desktop/CLI/SSH/background or other surfaces may differ.
- Preserve post-install verification: exact reviewed version, expected-only skills/commands/agents/hooks/connectors/MCP, positive capability test, nearby negative test, denied-tool behavior, approval for consequential action, unexpected process/network/file modification checks, and fresh-session consistency. Test bundled skills independently before composition.
- Preserve safe update workflow: record installed version, review release notes/source diff, detect new hooks/connectors/MCP/secrets, reproduce in test environment, rerun activation/permission tests, and retain rollback. Recommend pinned/approved updates for plugins with repository writes, production credentials, messaging, payments, deployment, or equivalent side effects.
- Explain disable versus remove. After removal verify bundled skills/commands, agents, hooks, MCP entries, connector authorizations, cached executables/generated files, environment variables, and plugin-only secrets are gone; revoke external tokens separately when uninstall does not.
- Preserve troubleshooting for: installed but not visible; skills visible but not activating; hook/MCP startup failure; behavior remaining after removal. Include restart/session, host/version/policy, manifest parsing/enabled state, discovery description/namespace/version, runtime/dependency/path/env/secret, sandbox/approval, generated config/caches/connector authorization, and clean-profile comparison checks.
- Preserve the operational checklist: correct ecosystem; source/version/license; package component/telemetry review; minimized permissions; test-environment install; positive/negative/permission/failure tests; update/rollback policy; disable/uninstall/credential-revocation verification.
- Cross-link the Plugins learning root, creating tutorial, Agent Skills/MCP learning roots, and concrete host/platform catalog owners where current instructions are needed.

## Validation

- The guide never presents a host-specific plugin command/manifest as universal.
- Package review includes both instruction-only and executable/integration surfaces.
- Install verification, permission tests, update/rollback, uninstall cleanup, and token revocation remain explicit.
- Current platform behavior is source-backed/freshness-bound.
