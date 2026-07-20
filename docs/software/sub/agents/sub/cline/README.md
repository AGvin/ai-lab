# Cline

Open-source coding agent and agent runtime for editor, terminal, SDK, and automation workflows.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Metadata

```text
Resource type: Coding agent
Primary use case: Plan, edit, run, and review codebase changes through an agent workflow integrated with developer tools
Access model: Open-source agent runtime with local usage and external model provider credentials
License: Apache-2.0
Source model: Open source
Operational requirement: Cline extension, CLI, SDK, or runtime; selected model provider credentials; repository access; configured tool, shell, MCP, and automation permissions
Integration modes: VS Code, JetBrains, terminal, SDK, Git repositories, shell commands, MCP servers, model providers, browser and network-capable tools, automation workflows
Source: https://github.com/cline/cline
Risk notes: High-trust coding agent with repository write access, shell execution, MCP/tool integration, and optional automation workflows; review command approvals, generated diffs, provider credentials, MCP server permissions, repository instructions, secrets exposure, browser or network access, and sandboxing before use with sensitive repositories.
```

## Overview

Cline is an open-source coding agent and agent runtime for developer workflows.

It can operate through editor integrations, terminal workflows, and SDK-based usage. Its role is broader than a simple chat assistant: it can inspect a codebase, plan changes, edit files, invoke tools, run commands, and integrate with agent-related workflows such as MCP-backed tools and automation.

## Fit for AI Lab

Cline belongs under `agents/` because its main documented role is an agent-like coding assistant and runtime that works directly with developer repositories and tools.

It is adjacent to agent orchestration because it exposes runtime, SDK, automation, and multi-agent-oriented capabilities, but the canonical documented object is still a coding agent rather than a general-purpose orchestration framework.

Use Cline as a reference point for:

- editor-integrated coding-agent workflows;
- repository editing with human approval gates;
- tool and shell execution from an AI coding agent;
- MCP-enabled developer automation;
- comparison with Aider, Pi, Goose, Claude Code, and Codex CLI;
- evaluating agent runtimes that span editor, terminal, SDK, and automation use cases.

## Evaluation notes

Evaluate before adoption:

- editor, terminal, or SDK workflow fit;
- model provider support and credential handling;
- repository instruction and rules trust boundaries;
- shell command approval and execution model;
- generated diff review workflow;
- MCP server permissions and tool scopes;
- browser, network, and filesystem access boundaries;
- behavior in headless, CI, scheduled, or multi-agent automation modes.

## References

- Cline website: https://cline.bot
- Cline documentation: https://docs.cline.bot
- Cline GitHub: https://github.com/cline/cline
