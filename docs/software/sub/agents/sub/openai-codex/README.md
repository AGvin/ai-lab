# OpenAI Codex

OpenAI coding agent for software-engineering workflows across app, IDE, CLI, web, and automation surfaces.

## Metadata

```text
Resource type: Coding agent
Primary use case: Read, edit, test, review, and automate software changes through OpenAI-managed Codex workflows
Access model: Proprietary OpenAI product with account, workspace, or enterprise access
License: Proprietary
Source model: Closed source product with related CLI and integration tooling
Operational requirement: Codex access, OpenAI account or organization entitlement, repository or workspace access, configured tool permissions, and optional IDE, CLI, GitHub, Slack, Linear, MCP, or automation integrations
Integration modes: Codex app, IDE extension, CLI, web, GitHub, Slack, Linear, local environments, worktrees, shell commands, MCP, plugins, GitHub Action, SDK, automations
Source: https://developers.openai.com/codex
Risk notes: High-trust coding agent with repository read/write access, local or remote execution, shell/tool permissions, automation surfaces, and account/workspace boundaries; review sandboxing, generated diffs, provider credentials, repository instructions, secret exposure, and approval gates before use with sensitive repositories.
```

## Overview

OpenAI Codex is a proprietary coding agent for software-development workflows.

It spans multiple product surfaces, including app, IDE, CLI, web, and automation workflows. Its role is broader than code completion: Codex can operate on repositories, propose changes, run commands or checks, use configured tools, and integrate with engineering workflows such as GitHub, Slack, Linear, MCP, plugins, and GitHub Actions.

## Fit for AI Lab

OpenAI Codex belongs under `agents/` because its main documented role is an agent-like coding system for software-engineering tasks.

It is not only a model family entry. Use `models/` for individual OpenAI model families, and use this page for the Codex coding-agent product and workflow surface.

Use OpenAI Codex as a reference point for:

- proprietary coding-agent products;
- app, IDE, CLI, web, and automation coding workflows;
- repository editing and review workflows;
- agent configuration, rules, hooks, skills, MCP, and plugin surfaces;
- comparison with Claude Code, GitHub Copilot coding agent, Devin, Cursor, Cline, and Aider.

## Evaluation notes

Evaluate before adoption:

- account, workspace, and organization access model;
- local versus remote execution boundaries;
- repository and worktree access controls;
- shell command and tool approval behavior;
- generated diff review before commit, push, or PR creation;
- repository instruction, rules, hooks, plugin, MCP, and skill trust boundaries;
- exposure of source code, secrets, logs, and project context.

## References

- OpenAI Codex documentation: https://developers.openai.com/codex
- Codex quickstart: https://developers.openai.com/codex/quickstart
