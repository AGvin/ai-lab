# GitHub Copilot Coding Agent

GitHub-native cloud coding agent for issue-driven software changes and pull-request workflows.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Metadata

```text
Resource type: Cloud coding agent
Primary use case: Assign repository tasks or issues to Copilot so it can create code changes, run checks, and open or update pull requests for review
Access model: Proprietary GitHub Copilot feature with subscription, organization, or enterprise access
License: Proprietary
Source model: Closed source product with GitHub platform integrations
Operational requirement: GitHub Copilot coding-agent access, repository permissions, GitHub Actions-backed cloud development environment, issue or task context, and organization policy configuration
Integration modes: GitHub issues, pull requests, GitHub Actions, repository instructions, GitHub web, GitHub Mobile, GitHub CLI, Copilot plans and policies
Source: https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent
Risk notes: High-trust cloud coding agent with repository, issue, pull-request, and GitHub Actions environment access; review repository permissions, action secrets, generated commits, draft PRs, organization policies, review gates, and branch protection before use with sensitive repositories.
```

## Overview

GitHub Copilot coding agent is a GitHub-native cloud coding agent for repository tasks.

It is designed for issue-driven or task-driven workflows where Copilot can work in a cloud development environment, make repository changes, and return work through pull requests for human review.

## Fit for AI Lab

GitHub Copilot coding agent belongs under `agents/` because its main documented role is an autonomous or semi-autonomous coding agent operating inside GitHub workflows.

Use it as a reference point for:

- GitHub-native coding-agent workflows;
- issue-to-pull-request automation;
- cloud development environments backed by GitHub platform features;
- policy-controlled enterprise coding-agent adoption;
- comparison with OpenAI Codex, Claude Code, Devin, Jules, and Cursor.

## Evaluation notes

Evaluate before adoption:

- Copilot subscription and organization access model;
- repository and organization policy controls;
- GitHub Actions environment and secret boundaries;
- generated commit and draft PR review workflow;
- branch protection and merge approval requirements;
- repository instruction trust boundaries;
- auditability of agent decisions and generated changes.

## References

- GitHub Copilot cloud agent documentation: https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent
- GitHub Copilot: https://github.com/features/copilot
