# OpenAI Codex

OpenAI coding agent for software-engineering workflows across app, IDE, CLI, web, and automation surfaces.

## Translations

- English
- [Українська](./l10n/uk_UA/)

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

## Skills, plugins, and MCP

Codex supports reusable Agent Skills and platform-specific plugins, and it can connect to MCP servers. Keep general explanations and tutorials centralized:

- [Agent Skills](../../../../../notes/sub/concepts/sub/agents-and-automation/sub/agent-skills/)
- [Codex skill installation and invocation](../../../../../notes/sub/concepts/sub/agents-and-automation/sub/agent-skills/sub/platform-support/#openai-codex)
- [Plugins](../../../../../notes/sub/concepts/sub/agents-and-automation/sub/plugins/)
- [Model Context Protocol](../../../../../notes/sub/concepts/sub/agents-and-automation/sub/model-context-protocol/)

Use this product page for Codex-specific evaluation notes rather than duplicating the full learning guides.

<!-- Stable cross-locale anchor; do not translate or remove. -->
<a id="codex-data-safety"></a>

## Data path and privacy

Verified on 2026-07-26.

Codex has several surfaces with different execution boundaries. CLI and IDE workflows can read files and run approved commands in a local environment, while hosted model requests still send the task and relevant context to OpenAI. Codex cloud tasks run in OpenAI-managed environments and can access the repositories and environment configuration connected to the task.

Local file or command execution therefore does not mean that inference or task context remains local.

For data use:

- individual ChatGPT plans can allow Codex content to be used for model improvement unless the applicable data controls are disabled;
- Codex full-environment training controls are separate and must be reviewed in Codex settings;
- Business, Enterprise, Edu, and API inputs and outputs are excluded from training by default unless an eligible organization explicitly opts in;
- retention, residency, connected-repository permissions, and contractual controls still require separate review.

For sensitive repositories, use the approved organization account, restrict repository and environment access, remove secrets from available context, use sandboxing and least privilege, and require review before commit, push, deployment, or other external action.

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
- Using Codex with a ChatGPT plan: https://help.openai.com/en/articles/11369540
- OpenAI data-use controls: https://help.openai.com/en/articles/5722486
- Enterprise admin guide for Codex: https://help.openai.com/en/articles/11390924
