# Devin

Proprietary autonomous software-engineering agent for ticket-driven development workflows.

## Metadata

```text
Resource type: Autonomous software engineering agent
Primary use case: Plan, implement, test, review, and deliver software changes from tickets, issues, or engineering tasks
Access model: Proprietary SaaS product with account, team, or enterprise access
License: Proprietary
Source model: Closed source product with public documentation and integrations
Operational requirement: Devin account or organization access, cloud workspace/session access, repository and issue-tracker permissions, configured secrets and tool permissions, and optional IDE, API, automation, MCP, or collaboration integrations
Integration modes: Cloud sessions, embedded IDE, terminal, browser, GitHub, GitLab, Bitbucket, Linear, Jira, Slack, Microsoft Teams, API, MCP, automations, scheduled sessions, deployments, pull requests, code review workflows
Source: https://docs.devin.ai/
Risk notes: High-trust autonomous engineering agent with cloud workspace, repository, terminal, browser, issue-tracker, secret, and automation access; review repository permissions, ticket and PR scopes, site cookies, secrets handling, tool permissions, scheduled sessions, deployment permissions, human takeover, and merge or release approval gates before use with sensitive repositories.
```

## Overview

Devin is a proprietary autonomous software-engineering agent from Cognition.

It is positioned as an AI software engineer for team workflows rather than a local pair-programming assistant. Devin can work from tickets or engineering tasks, operate in cloud sessions, use development tools, produce code changes, run tests, open or update pull requests, and participate in broader software-delivery workflows through integrations and automation features.

## Fit for AI Lab

Devin belongs under `agents/` because its primary documented role is an agent-like software-engineering system that performs development work across repositories, tools, tickets, and review workflows.

It is not an agent orchestration framework. Use `agent-orchestration/` for frameworks, runtimes, or control planes that coordinate multiple agents or agent workflows.

Use Devin as a reference point for:

- proprietary autonomous software-engineering agents;
- ticket-driven development workflows;
- cloud-session agent execution;
- repository, issue-tracker, and pull-request automation;
- team and enterprise AI engineering products;
- comparison with coding agents such as Claude Code, Cline, Goose, Aider, and mini-SWE-agent.

## Evaluation notes

Evaluate before adoption:

- account, team, enterprise, and data-processing model;
- repository, organization, and issue-tracker permission scopes;
- cloud workspace and session isolation boundaries;
- secrets, site cookies, and environment variable handling;
- terminal, browser, MCP, API, and automation permissions;
- scheduled sessions, deployments, and background execution controls;
- human takeover, review, merge, and release approval gates;
- auditability of generated changes and task decisions.

## References

- Devin documentation: https://docs.devin.ai/
- Devin app: https://app.devin.ai/
- Cognition website: https://cognition.com/
