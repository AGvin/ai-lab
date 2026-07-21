# CodeRabbit

AI code-review, planning, and development workflow agent for pull requests, Slack, IDE, and CLI usage.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Metadata

```text
Resource type: Code review and development workflow agent
Primary use case: Review pull requests, plan implementations, provide code feedback, and support development workflows across Git, IDE, CLI, and Slack surfaces
Access model: Proprietary CodeRabbit platform with account, team, and organization access
License: Proprietary
Source model: Closed source product with public documentation and integrations
Operational requirement: CodeRabbit access, connected Git provider, repository permissions, team knowledge configuration, and optional Slack, IDE, CLI, Jira, or Linear integrations
Integration modes: GitHub, GitLab, Azure DevOps, Bitbucket, pull requests, Slack agent, IDE extension, CLI tool, Jira, Linear, planning workflows, code review workflows, scheduled or message-triggered automations
Source: https://docs.coderabbit.ai/
Risk notes: High-trust review and workflow agent with repository, pull-request, Slack, IDE, CLI, issue-tracker, and team-knowledge access; review permission scopes, generated comments and fixes, planning outputs, automation triggers, credentials, secrets exposure, and human review before merge or execution.
```

## Overview

CodeRabbit is an AI-powered platform for code review, planning, and development workflows.

It combines pull-request review with workflow surfaces such as Slack, IDE extensions, CLI usage, issue planning, and integrations with Git and issue-tracking platforms.

## Fit for AI Lab

CodeRabbit belongs under `agents/` because its main documented role is an agent-like system for code review, planning, and development workflow support.

Use it as a reference point for:

- AI pull-request review agents;
- Slack-based planning and coding assistance;
- IDE and CLI review workflows;
- code-quality agents with repository and team context;
- comparison with Qodo and other review-focused agents.

## Evaluation notes

Evaluate before adoption:

- Git provider and issue-tracker support;
- repository and organization permission scopes;
- Slack, IDE, CLI, and automation boundaries;
- generated review accuracy and noise level;
- generated fix or PR behavior;
- team knowledge and external tool data exposure;
- required human review before merge or task execution.

## References

- CodeRabbit documentation: https://docs.coderabbit.ai/
- CodeRabbit website: https://www.coderabbit.ai/
