# Claude Code

Anthropic coding agent for terminal, editor, desktop, browser, and automation workflows.

## Metadata

```text
Resource type: Coding agent
Primary use case: Read, edit, test, and review codebase changes through Anthropic-managed agentic coding workflows
Access model: Proprietary Anthropic product with account, subscription, or organization access
License: Proprietary
Source model: Closed source product with related client tooling and documentation
Operational requirement: Claude Code access, Anthropic account or organization entitlement, local project or remote workspace access, configured tool and shell permissions, and optional IDE, MCP, CI/CD, or automation integrations
Integration modes: Terminal, VS Code, JetBrains IDEs, desktop app, browser, Slack, Git repositories, shell commands, MCP servers, GitHub Actions, GitLab CI, background agents, scheduled tasks, Agent SDK
Source: https://code.claude.com/docs/en/overview
Risk notes: High-trust proprietary coding agent with repository read/write access, shell execution, MCP/tool integration, background or scheduled execution, and cloud/account boundaries; review command approvals, generated diffs, provider account permissions, repository instructions, secrets exposure, remote session behavior, and human review gates before use with sensitive repositories.
```

## Overview

Claude Code is Anthropic's agentic coding tool for software-development workflows.

It can work through terminal, IDE, desktop, browser, and automation surfaces. Its role is broader than inline code completion: it can inspect a codebase, edit files, run commands or tests, assist with Git workflows, use configured tools, and support agentic coding workflows that extend into CI/CD, background work, scheduled tasks, and SDK-based integrations.

## Fit for AI Lab

Claude Code belongs under `agents/` because its main documented role is an agent-like coding system that works directly with repositories, tools, commands, and developer workflows.

It is not an agent orchestration framework. Use `agent-orchestration/` for frameworks, runtimes, or control planes that coordinate multiple agents or agent workflows.

Use Claude Code as a reference point for:

- proprietary agentic coding products;
- terminal and IDE coding-agent workflows;
- repository editing with shell and test execution;
- MCP-enabled coding-agent tool access;
- background, scheduled, CI/CD, and SDK-based agent workflows;
- comparison with open-source coding agents such as Aider, Cline, Goose, and mini-SWE-agent.

## Skills, plugins, and MCP

Claude Code supports standalone Agent Skills, Claude-specific plugins, and MCP servers. Centralized guides:

- [Agent Skills](../../../../../notes/sub/concepts/sub/agents-and-automation/sub/agent-skills/)
- [Claude Code skill installation and invocation](../../../../../notes/sub/concepts/sub/agents-and-automation/sub/agent-skills/sub/platform-support/#claude-code)
- [Plugins](../../../../../notes/sub/concepts/sub/agents-and-automation/sub/plugins/)
- [Model Context Protocol](../../../../../notes/sub/concepts/sub/agents-and-automation/sub/model-context-protocol/)

## Evaluation notes

Evaluate before adoption:

- account, subscription, and organization access model;
- repository and workspace access boundaries;
- shell command approval and execution behavior;
- generated diff review before commit, push, or PR creation;
- repository instruction and memory trust boundaries;
- MCP server permissions and tool scopes;
- background agent, scheduled task, desktop, browser, and cloud session boundaries;
- exposure of source code, credentials, logs, and private project context.

## References

- Claude Code overview: https://code.claude.com/docs/en/overview
- Claude Code quickstart: https://code.claude.com/docs/en/quickstart
- Claude Code web entry point: https://claude.ai/code
