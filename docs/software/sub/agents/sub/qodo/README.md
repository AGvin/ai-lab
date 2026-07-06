# Qodo

AI code-review agent suite integrated into Git pull-request workflows.

## Metadata

```text
Resource type: Code review agent
Primary use case: Review pull requests with repository context, specialized review agents, rules, and organization standards
Access model: Proprietary Qodo product with hosted, team, enterprise, and deployment-model options
License: Proprietary
Source model: Closed source product with public documentation and integrations
Operational requirement: Qodo access, Git provider integration, repository permissions, organization rules or standards, and optional deployment-model configuration
Integration modes: Git workflows, pull requests, review agents, rule system, repository context, organizational standards, ticketing integrations, CI feedback, compliance configuration
Source: https://docs.qodo.ai/qodo-documentation/code-review
Risk notes: High-trust review agent with repository, pull-request, organization-standard, and compliance context access; review repository permissions, rule sources, false positives and false negatives, generated suggestions, secrets exposure, and required human review before merge.
```

## Overview

Qodo is an AI code-review experience integrated into Git workflows.

Its documented focus is pull-request review, repository-context analysis, rule enforcement, and surfacing bugs or issues with lower review noise. It is best treated as a code-review agent rather than a general coding assistant.

## Fit for AI Lab

Qodo belongs under `agents/` because its primary documented behavior is agent-like code review using repository context and specialized review agents.

Use it as a reference point for:

- AI pull-request review agents;
- repository-context-aware review workflows;
- rule-based and organization-standard review systems;
- comparison with CodeRabbit and other review-focused agents;
- evaluating review quality for AI-generated code.

## Evaluation notes

Evaluate before adoption:

- Git provider and deployment model;
- repository and organization permission scopes;
- rule source and standards governance;
- signal-to-noise ratio and review accuracy;
- handling of secrets and private code;
- integration with CI and ticketing systems;
- required human review gates before merge.

## References

- Qodo code review documentation: https://docs.qodo.ai/qodo-documentation/code-review
- Qodo website: https://www.qodo.ai/
