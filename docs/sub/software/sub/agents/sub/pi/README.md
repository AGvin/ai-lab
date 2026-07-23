# Pi

Pi is a small terminal runtime for building and running a customized coding agent.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Metadata

```text
Resource type: AI coding agent harness
Primary use case: Build a project-local terminal coding agent around repository files, shell tools, model providers, and custom workflow extensions
Access model: Open-source package and hosted/subscription or API-key model providers depending on configuration
License: MIT
Source model: Open source
Operational requirement: Node.js package installation and provider authentication or API keys
Integration modes: Terminal UI, print/JSON mode, SDK, RPC mode, JSON event stream mode, TypeScript extensions, skills, prompt templates, themes, and Pi packages
Source: pi.dev documentation
Risk notes: Pi can become as powerful as the tools, extensions, skills, shell access, provider credentials, and project permissions connected to it. Review all local and third-party components before using it on sensitive repositories.
```

## What it is

Pi is best understood as a **coding-agent workbench for the terminal**.

It is not only a chat window and not a full IDE. It is a thin agent runtime that runs inside a project directory and lets a model work with project context, instructions, files, commands, and custom tools.

A simpler mental model:

```text
Pi = terminal AI agent core + project instructions + tools + optional custom extensions/skills/packages
```

The important part is that Pi is meant to be shaped around a workflow. Instead of accepting one fixed agent product, a user can keep the core small and add only the behavior they need.

It is not the `pi.ai` conversational assistant product. This page tracks the software documented at `pi.dev`.

## Practical examples

Pi may be useful for workflows such as:

- running a repository-local coding assistant in the terminal;
- loading project rules from files such as `AGENTS.md` and using them during code or documentation changes;
- asking an agent to inspect files, propose changes, and edit repository content;
- creating a repeatable documentation-maintenance workflow for a repository;
- building a custom command such as `/prepare-pr`, `/audit-docs`, or `/summarize-branch`;
- wrapping a common workflow into a reusable skill;
- creating a TypeScript extension that adds a custom tool, command, keyboard shortcut, event hook, or terminal UI element;
- exposing Pi through SDK, RPC, or JSON event streams so another local tool can drive the agent;
- packaging a team-specific set of extensions, skills, prompt templates, and themes as a Pi package.

## Why it belongs under agents

Pi belongs under `agents/` because the primary object is an agent harness: it exists to run and customize an AI agent workflow.

It should not be documented as a code editor because it does not replace an editor UI. It also should not be documented only as a library because its normal use is an interactive terminal coding-agent session.

## How it differs from a typical coding assistant

A typical coding assistant is often a fixed product with a predefined interface and feature set.

Pi is closer to an agent construction kit:

- the terminal session is the default interface;
- the project can provide its own instructions;
- extensions can add tools and behavior;
- skills can provide reusable task-specific knowledge;
- prompt templates can turn repeated prompts into commands;
- packages can distribute a complete set of custom behavior;
- programmatic modes can let other tools embed or control the agent.

## What to evaluate

Before using Pi as part of a regular workflow, evaluate:

- install and update flow;
- supported providers and model switching;
- how it loads project instructions and context;
- how safely it handles shell access and file edits;
- whether it has enough guardrails for private repositories;
- how extension, skill, and package permissions work;
- whether custom workflows are easier to maintain in Pi than in standalone scripts, GitHub Actions, or another coding agent.

## References

- https://pi.dev/
- https://pi.dev/docs/latest
- https://pi.dev/docs/latest/sdk
- https://pi.dev/docs/latest/extensions
- https://pi.dev/docs/latest/skills
- https://pi.dev/docs/latest/packages
