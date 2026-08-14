# Documentation Requirements

## Requirements

- Identify Playwright as Microsoft's open-source framework/tooling family for web testing and browser automation across Chromium, Firefox, and WebKit.
- Keep the primary canonical identity under Development Tools / Testing. Playwright CLI and MCP can expose browser automation to coding/AI agents, but those integration surfaces do not make Playwright itself a standalone AI agent.
- Preserve durable surfaces at a high level: Playwright Test, browser automation library, CLI, CI execution, VS Code extension, and current agent-facing CLI/MCP tooling.
- Preserve useful legacy trust boundaries around browser/session permissions, network access, authentication state/cookies, downloaded browser runtimes, test secrets, CI credentials, target-environment isolation, destructive browser actions, and reuse of existing logged-in browser profiles.
- Distinguish isolated test browser contexts from explicit integrations that connect to an existing user browser/profile; do not generalize one privacy/security boundary to all modes.
- Keep exact browser versions, language bindings, command names, AI-agent integrations, release behavior, and other mutable compatibility details source-backed when expanded.
- Link the canonical Microsoft producer profile.
- Include current official Playwright site, docs, and repository.

## Validation

- Playwright is not classified as generic workflow automation or as an AI-agent product.
- Agent/MCP integration is represented as an interface to Playwright browser tooling.
- Existing-browser/profile access is treated as a higher-trust boundary when enabled.
- The producer relation resolves to Microsoft.
