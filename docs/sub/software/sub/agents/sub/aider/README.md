# Aider

Terminal-based AI pair programming tool and coding agent for working directly with local Git repositories.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Metadata

```text
Resource type: Coding agent
Primary use case: Edit, refactor, and maintain code in a local Git repository through a terminal chat workflow
Access model: Open-source CLI tool with local usage and external model provider credentials
License: Apache-2.0
Source model: Open source
Operational requirement: Aider CLI, local Git repository, selected model provider credentials, and local filesystem access to the target codebase
Integration modes: Terminal, Git repositories, model providers, local files, editor workflows, command-line development workflows
Source: https://github.com/Aider-AI/aider
Risk notes: High-trust coding agent with local repository write access; review generated diffs before commit or push, protect secrets in the codebase, constrain provider credentials, and avoid running untrusted generated code without sandboxing.
```

## Overview

Aider is a terminal-based AI pair programming tool that works directly with local Git repositories.

It lets a developer chat with a model about a codebase, add files to the working context, request changes, review diffs, and integrate those changes into the normal Git workflow.

## Fit for AI Lab

Aider belongs under `agents/` because its main documented role is an agent-like coding assistant that directly edits repository files.

It is not an agent orchestration framework. Use `agent-orchestration/` for frameworks, runtimes, or control planes that coordinate multiple agents or agent workflows.

Use Aider as a reference point for:

- terminal-first coding-agent workflows;
- local repository editing with Git integration;
- comparison with coding agents such as Pi, Cline, Goose, Claude Code, and Codex CLI;
- evaluating low-overhead AI pair programming workflows;
- understanding repository-write safety requirements for coding agents.

## Evaluation notes

Evaluate before adoption:

- supported model providers and credential handling;
- Git workflow behavior and commit boundaries;
- diff review workflow before committing or pushing;
- handling of large repositories and multi-file edits;
- exposure of source code and secrets to model providers;
- local command execution and generated-code safety;
- fit with existing editor, terminal, and repository workflows.

## References

- Aider website: https://aider.chat
- Aider documentation: https://aider.chat/docs/
- Aider GitHub: https://github.com/Aider-AI/aider
