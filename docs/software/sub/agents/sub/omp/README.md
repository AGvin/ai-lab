# OMP (Oh My Pi)

OMP is an open-source terminal coding agent derived from Pi and extended with an integrated development-tool harness.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Metadata

```text
Resource type: Terminal AI coding agent and extensible agent runtime
Primary use case: Perform repository analysis, editing, debugging, research, and delegated coding tasks through a tool-rich terminal agent
Access model: Open-source local application with external, subscription-routed, gateway, or local model providers depending on configuration
Cost model: OMP is free under the MIT License; selected model providers, coding plans, gateways, or hosted services may have separate costs
License: MIT
Source model: Open source
Operational requirement: OMP installation, project access, Bun or a supported installer, and credentials for the selected model providers
Integration modes: Terminal UI, CLI, SDK, RPC, model roles, built-in tools, LSP, DAP, persistent Python and JavaScript execution, browser and research tools, subagents, extensions, skills, and MCP discovery
Source: https://github.com/can1357/oh-my-pi
Risk notes: OMP exposes a broad tool surface that can modify repositories, execute shell and language-runtime code, access debuggers and browsers, delegate to subagents, and call remote providers. Restrict tools and credentials, review approval settings and generated changes, and use isolation for untrusted repositories or tasks.
Last verified: 2026-07-17
```

## Overview

OMP, also branded **Oh My Pi**, is a terminal-first coding agent designed to ship with a broad development environment already connected. It combines a coding-agent session with repository tools, language-server and debugger operations, persistent code execution, browser and research capabilities, and subagent workflows.

The executable and current product name use `omp`, while the source repository and package lineage retain the Oh My Pi and Pi naming.

## Relationship to Pi

OMP is a fork of Pi. Both products provide terminal coding-agent sessions and extensible runtime surfaces, but their design emphasis differs:

- **Pi** keeps the core small and expects users to assemble extensions, skills, prompts, and packages around their workflow.
- **OMP** includes a much larger built-in tool and provider surface, aiming to be complete out of the box.

Document the two products separately because they have independent repositories, packages, releases, configurations, capabilities, and maintenance lifecycles.

## Development-tool surface

OMP integrates development capabilities that are often separate applications or plugins:

- repository read, write, search, and structured edit operations;
- shell execution with terminal and background-process support;
- language-server operations for symbols, references, diagnostics, and code intelligence;
- debugger operations through DAP integrations;
- structural search and editing with syntax-aware tooling;
- persistent Python and JavaScript execution that can call agent tools;
- browser, documentation, research, and vulnerability-data retrieval;
- delegated tasks and configurable subagent roles.

A large built-in tool catalog improves availability but also increases the permission and review surface.

## Models, providers, and roles

OMP supports many direct APIs, gateways, subscription-routed coding plans, and local model servers. Model roles allow different models to handle ordinary work, inexpensive delegated tasks, deeper reasoning, planning, and commit-oriented output.

Provider availability and authentication behavior can change independently of OMP. Verify the exact installed release, provider terms, OAuth flow, local-server compatibility, pricing, and model capabilities before standardizing a configuration.

## SDK, RPC, and MCP

The SDK provides in-process access to agent state, events, sessions, models, tools, and discovery. RPC mode supports cross-process or cross-language control.

OMP can discover MCP servers as part of its extensibility surface. MCP servers should be assessed as independently trusted integrations because they may expose tools, context, credentials, or remote services. See [Model Context Protocol](../../../../../notes/sub/concepts/sub/agents-and-automation/sub/model-context-protocol/) for the protocol architecture.

## Installation and platform support

Official installation paths include shell and PowerShell installers, a Bun package, and release-oriented tooling such as Mise. The project documents macOS, Linux, and Windows support and currently requires a compatible Bun release for package installation.

Pin a known release for repeatable environments. OMP evolves quickly and may introduce changes to tools, provider integrations, settings, edit formats, and approval behavior.

## Safety and operational risks

Review at least these boundaries:

- which tools are visible and executable in each mode;
- approval rules for read, write, shell, debugger, browser, and delegated actions;
- provider credentials and OAuth tokens;
- network access and data sent to external services;
- persistent Python or JavaScript state;
- extensions, skills, prompts, and project instructions;
- subagent scope, concurrency, and cost;
- rollback and diff review after automated edits.

Tool-rich operation should not be confused with sandboxing. Use containers, disposable worktrees, restricted credentials, or operating-system isolation when the task or repository is not fully trusted.

## Fit for AI Lab

OMP belongs under `agents/` because its primary role is an interactive coding agent. LSP, DAP, browser, SDK, RPC, and orchestration-like features extend that agent rather than changing the canonical product category.

Use this page as a reference for:

- batteries-included terminal coding agents;
- comparison with the smaller Pi harness;
- integrated LSP and debugger workflows;
- persistent language runtimes with agent-tool access;
- model-role routing and broad provider support;
- tool-rich subagent and research workflows.

## Evaluation checklist

Before adoption, verify:

- the exact release and supported installation path;
- compatibility with the required operating systems and shells;
- model-provider authentication, pricing, and fallback behavior;
- quality and safety of the edit, shell, LSP, DAP, browser, and evaluation tools;
- approval controls and whether hidden or dynamically discovered tools can become active;
- extension, skill, MCP, and project-instruction trust boundaries;
- SDK or RPC stability if OMP is embedded in another system;
- resource usage, subagent cost, and recovery after partial failure.

## References

- OMP website: https://omp.sh/
- Source repository: https://github.com/can1357/oh-my-pi
- SDK documentation: https://github.com/can1357/oh-my-pi/blob/main/docs/sdk.md
- Model and provider configuration: https://github.com/can1357/oh-my-pi/blob/main/docs/models.md
- Releases: https://github.com/can1357/oh-my-pi/releases
- License: https://github.com/can1357/oh-my-pi/blob/main/LICENSE
