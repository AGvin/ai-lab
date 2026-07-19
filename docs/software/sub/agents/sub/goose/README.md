# Goose

Open-source local AI agent for coding, research, automation, writing, and workflow tasks.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Metadata

```text
Resource type: General-purpose local AI agent
Primary use case: Run local agent workflows across coding, research, automation, writing, data analysis, and developer tasks
Access model: Open-source local agent with desktop, CLI, and API usage plus external model provider credentials
License: Apache-2.0
Source model: Open source
Operational requirement: Goose desktop app, CLI, or API; selected model provider credentials; local filesystem and tool access; optional MCP extensions
Integration modes: Desktop app, CLI, API, local files, shell or workflow tasks, model providers, MCP extensions, developer automation workflows
Source: https://github.com/aaif-goose/goose
Risk notes: High-trust local agent with filesystem, tool, extension, and provider access; review local data exposure, shell or workflow permissions, MCP extension scopes, provider credentials, desktop or API attack surface, human approval gates, and sandboxing before use with sensitive repositories or private data.
```

## Overview

Goose is an open-source local AI agent for general-purpose work on a developer machine.

It is broader than a coding-only assistant: it can support coding, workflows, research, writing, automation, and data-analysis tasks through desktop, CLI, and API workflows.

## Fit for AI Lab

Goose belongs under `agents/` because its primary documented role is a local agent-like system that performs tasks through tools, local context, model providers, and extensions.

It is not an agent orchestration framework. Use `agent-orchestration/` for frameworks, runtimes, or control planes that coordinate multiple agents or agent workflows.

Use Goose as a reference point for:

- local general-purpose agent workflows;
- desktop and CLI agent usage;
- MCP extension-driven tool access;
- comparison with coding agents such as Aider, Cline, Pi, Claude Code, and Codex CLI;
- evaluating local agent safety boundaries for private files and repositories;
- understanding trade-offs between coding-specific agents and broader task agents.

## Evaluation notes

Evaluate before adoption:

- desktop, CLI, or API workflow fit;
- model provider support and credential handling;
- local filesystem and shell or workflow permission boundaries;
- MCP extension trust and permission scopes;
- exposure of private source code, documents, and data to providers or tools;
- human approval gates and auditability;
- sandboxing strategy for sensitive repositories and private data.

## References

- Goose GitHub: https://github.com/aaif-goose/goose
- Goose documentation: https://goose-docs.ai
