# Replit Agent

AI app-building agent for turning natural-language prompts into apps and websites inside Replit.

## Metadata

```text
Resource type: App-building agent
Primary use case: Build, iterate, debug, deploy, and publish apps or websites from natural-language prompts in the Replit environment
Access model: Proprietary Replit product with account, plan, and workspace access
License: Proprietary
Source model: Closed source product with generated application code inside Replit workspaces
Operational requirement: Replit account, Replit Agent access, project workspace, generated app environment, deployment or publishing configuration, and optional GitHub import or integration workflows
Integration modes: Replit workspace, chat interface, app generation, website generation, deployment, publishing, database and integrations, screenshots or multimodal inputs, GitHub import, Replit hosting
Source: https://replit.com/ai
Risk notes: High-trust app-building agent with workspace, generated code, deployment, database, integration, and hosting access; review generated dependencies, secrets, project permissions, public visibility, deployment controls, and human review before operating production applications.
```

## Overview

Replit Agent is Replit's AI app-building agent for creating apps and websites from natural-language prompts.

It operates inside the Replit environment and is aimed at quickly moving from idea to working prototype or deployed application, with support for iteration, debugging, and publishing workflows.

## Fit for AI Lab

Replit Agent belongs under `agents/` because its main documented role is an agent-like app builder that performs software-creation tasks from user instructions.

Use it as a reference point for:

- natural-language app-building agents;
- hosted development environments with built-in AI agents;
- prototype-to-deployment workflows;
- non-developer and developer app-generation experiences;
- comparison with Lovable and Bolt.

## Evaluation notes

Evaluate before adoption:

- Replit account, plan, and workspace model;
- generated code ownership and export path;
- workspace and project permissions;
- GitHub import or sync boundaries;
- database, integration, and hosting access;
- deployment visibility and public sharing controls;
- generated dependency and security review.

## References

- Replit Agent product page: https://replit.com/ai
- Replit documentation: https://docs.replit.com/
