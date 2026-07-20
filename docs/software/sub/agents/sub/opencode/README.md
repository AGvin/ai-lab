# OpenCode

OpenCode is an open-source AI coding-agent application and runtime available through terminal, desktop, and IDE interfaces.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Metadata

```text
Resource type: AI coding-agent application and runtime
Primary use case: Inspect, plan, edit, and validate codebase changes with configurable models, agents, tools, and approval policies
Access model: Open-source local application with external model providers or OpenCode-operated model access
Cost model: OpenCode is free under the MIT License; model providers and hosted model access may have separate usage or subscription costs
License: MIT
Source model: Open source
Operational requirement: OpenCode installation, project access, and credentials for the selected model provider
Integration modes: Terminal UI, non-interactive CLI, desktop app, IDE extension, project instructions, custom agents, skills, custom tools, and MCP servers
Source: https://github.com/anomalyco/opencode
Risk notes: OpenCode can read and modify files, execute shell commands, access external tools, and use network-backed services. Its permission system provides approval controls but the agent is not sandboxed; review permissions, diffs, commands, MCP servers, provider credentials, and repository instructions before use with sensitive projects.
Last verified: 2026-07-17
```

## Overview

OpenCode is a coding-agent product rather than a conventional code editor. It can analyze a project, use model-driven tools, modify files, execute commands, and maintain project-specific instructions while the user works through a terminal, desktop client, or IDE integration.

Running `/init` analyzes the current project and creates an `AGENTS.md` file. Committing that file allows repository-specific structure, conventions, and workflow guidance to travel with the codebase.

## Agents and operating modes

OpenCode supports configurable primary agents and subagents. Built-in or custom agents can use different models, prompts, descriptions, tools, and permission rules.

Typical roles include:

- a build agent allowed to edit files and run approved commands;
- a plan or review agent that can inspect the repository but cannot modify it;
- specialized subagents for exploration, review, research, or bounded tasks.

Agents can be configured in `opencode.json` or as Markdown files in global or project-local agent directories.

## Tools, skills, plugins, and MCP

OpenCode includes tools for repository inspection, file editing, search, shell execution, language-server queries, and related coding operations. It can also load reusable skills, custom tools, OpenCode-specific plugins, and Model Context Protocol servers.

Use the centralized guides for concepts and cross-platform workflows:

- [Agent Skills](../../../../../notes/sub/concepts/sub/agents-and-automation/sub/agent-skills/)
- [OpenCode skill installation, invocation, and permissions](../../../../../notes/sub/concepts/sub/agents-and-automation/sub/agent-skills/sub/platform-support/#opencode)
- [Plugins](../../../../../notes/sub/concepts/sub/agents-and-automation/sub/plugins/)
- [Model Context Protocol](../../../../../notes/sub/concepts/sub/agents-and-automation/sub/model-context-protocol/)

OpenCode plugins are executable JavaScript or TypeScript extensions and are not interchangeable with Agent Skills or another platform's plugin packages. Prefer a neutral skill directory when no OpenCode-specific lifecycle or runtime extension is needed.

MCP support allows external servers to expose additional tools to OpenCode. Tool availability does not imply trust: each MCP server and its credentials, network access, data exposure, and command surface should be reviewed independently.

## Permissions and safety boundary

Permissions can resolve an action to:

- `allow` — execute without another approval prompt;
- `ask` — require user approval;
- `deny` — block the action.

Rules can be global, tool-specific, command-pattern-specific, path-specific, or overridden per agent. This makes it possible to allow read-only analysis, require approval for edits, or deny commands such as `git push`.

Permissions are an operational control, not a security sandbox. A permitted agent action runs with the access available to the OpenCode process. Use operating-system isolation, containers, disposable worktrees, restricted credentials, or another sandbox when stronger containment is required.

## Models and providers

OpenCode can connect to multiple model providers and supports model selection per agent. Provider credentials may be configured directly, while OpenCode Zen offers a curated hosted model catalog operated by the OpenCode project.

Evaluate provider choice separately from the client:

- data retention and training policy;
- regional and organizational availability;
- authentication and secret storage;
- model context limits and tool-calling quality;
- pricing, rate limits, and fallback behavior.

## Installation and Windows use

Official installation options include the project install script, package managers, release binaries, and a container image. Windows installation is available through Chocolatey and Scoop; the official documentation notes that Bun-based Windows installation support is still evolving.

For Windows development, compare native installation with WSL according to repository location, shell tooling, filesystem performance, credential handling, and parity with the production environment. Do not assume WSL is required when the native workflow already supports the necessary tools.

## Fit for AI Lab

OpenCode belongs under `agents/` because its canonical role is running coding-agent workflows. Its desktop and IDE surfaces are clients of the same agent product rather than independent code editors.

Use this page as a reference for:

- terminal-first and multi-surface coding-agent workflows;
- repository-local `AGENTS.md` instructions;
- configurable primary agents and subagents;
- granular command, path, tool, and agent permissions;
- skills, plugins, and MCP-enabled development tools;
- comparison with Pi, OMP, Cline, Claude Code, and OpenAI Codex.

## Evaluation checklist

Before adopting OpenCode, verify:

- installation and update behavior on the target operating system;
- support and quality for the selected models and providers;
- repository instruction precedence and trust boundaries;
- approval behavior for file edits, shell commands, external directories, skills, plugins, and MCP tools;
- diff review and rollback workflow;
- behavior in non-interactive or automated execution;
- credential storage and network-data exposure;
- whether additional sandboxing is required for the repository.

## References

- OpenCode website: https://opencode.ai/
- OpenCode documentation: https://opencode.ai/docs/
- Agents: https://opencode.ai/docs/agents/
- Skills: https://opencode.ai/docs/skills/
- Plugins: https://opencode.ai/docs/plugins/
- Permissions: https://opencode.ai/docs/permissions/
- Tools: https://opencode.ai/docs/tools/
- Source repository: https://github.com/anomalyco/opencode
- Security model: https://github.com/anomalyco/opencode/security
