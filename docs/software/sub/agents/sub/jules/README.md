# Jules

Google autonomous coding agent for asynchronous software-development tasks.

## Metadata

```text
Resource type: Coding agent
Primary use case: Work on coding tasks asynchronously, including implementation, bug fixes, tests, and pull-request-style review workflows
Access model: Proprietary Google product with account and plan-based access
License: Proprietary
Source model: Closed source product with public documentation and Google ecosystem integrations
Operational requirement: Jules access, Google account or plan entitlement, connected repository or task workspace, configured permissions, and optional CLI or API integrations
Integration modes: Web app, repositories, GitHub workflows, asynchronous tasks, task plans, tests, pull requests, CLI, API, Gemini models
Source: https://jules.google/
Risk notes: High-trust asynchronous coding agent with repository, task, test, and pull-request workflow access; review repository permissions, generated diffs, test logs, account permissions, task scope, CLI or API credentials, and human review gates before use with sensitive repositories.
```

## Overview

Jules is Google's autonomous coding agent for asynchronous software-development tasks.

It is positioned as an agent that can work on assigned coding tasks in the background, produce code changes, run or reason about tests, and return work for developer review.

## Fit for AI Lab

Jules belongs under `agents/` because its main documented role is an agent-like coding system rather than a code editor or orchestration framework.

Use it as a reference point for:

- Google-managed coding agents;
- asynchronous task execution for software development;
- repository-connected implementation, bug-fix, and test workflows;
- CLI and API expansion around coding-agent products;
- comparison with GitHub Copilot coding agent, OpenAI Codex, Claude Code, and Devin.

## Evaluation notes

Evaluate before adoption:

- account, plan, and availability model;
- repository connection and permission boundaries;
- task planning and review workflow;
- generated code and test result inspection;
- CLI and API credential handling;
- privacy and training-data controls;
- merge, deployment, and release approval gates.

## References

- Jules website: https://jules.google/
- Google Labs Jules: https://labs.google/jules
