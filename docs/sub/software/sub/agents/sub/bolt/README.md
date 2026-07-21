# Bolt

AI app and website builder for creating software by chatting with an agent.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Metadata

```text
Resource type: App-building agent platform
Primary use case: Build, iterate, refactor, test, and publish apps or websites from natural-language prompts and design inputs
Access model: Proprietary hosted platform with individual, team, and enterprise plans
License: Proprietary
Source model: Closed source product with generated application code and platform services
Operational requirement: Bolt account, project workspace, generated application environment, token budget, optional GitHub, Figma, Supabase, hosting, MCP, and team configuration
Integration modes: Web app builder, Bolt Agent, design-system import, Figma, GitHub, Supabase, hosting, databases, authentication, MCP servers, team workspaces, Bolt Cloud
Source: https://bolt.new/
Risk notes: High-trust app-building platform with generated code, hosted project state, GitHub, design-system, database, hosting, MCP, and team access; review generated dependencies, secrets, workspace roles, deployment controls, external integrations, and human review before production use.
```

## Overview

Bolt is an AI app and website builder from StackBlitz for creating software by chatting with an agent.

It is aimed at moving from idea or design input to working application, with support for project planning, generation, iteration, refactoring, testing, hosting, and integrations such as GitHub, Figma, Supabase, and MCP servers.

## Fit for AI Lab

Bolt belongs under `agents/` because its main documented role is an agent-like app-building system.

Use it as a reference point for:

- chat-driven app and website generation;
- app-building agents with hosting and backend services;
- design-system and Figma-assisted generation;
- GitHub-connected generated-code workflows;
- comparison with Lovable and Replit Agent.

## Evaluation notes

Evaluate before adoption:

- generated code ownership and export model;
- GitHub integration and repository boundaries;
- token budget and model-routing behavior;
- database, hosting, authentication, and MCP integration access;
- workspace and team permissions;
- generated dependency and vulnerability review;
- suitability for prototypes versus production applications.

## References

- Bolt website: https://bolt.new/
- Bolt help center: https://support.bolt.new/
