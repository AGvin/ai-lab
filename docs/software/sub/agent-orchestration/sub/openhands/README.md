# OpenHands

Self-hosted developer control center for coding agents and automations.

## Metadata

```text
Resource type: Agent orchestration platform
Primary use case: Run and coordinate coding agents across local, remote, and cloud backends for repository and engineering automation tasks
Access model: Open-source project with self-hosted deployment options
License: MIT
Source model: Open source
Operational requirement: Runtime for OpenHands plus selected agent/model/provider credentials and configured backends or integrations
Integration modes: Agent Canvas, local backends, remote backends, cloud backends, GitHub, Slack, Linear, ACP-compatible agents, coding agents, automations
Source: https://github.com/OpenHands/OpenHands
Risk notes: High-trust coding-agent orchestration platform; review workspace isolation, filesystem access, shell access, repository permissions, integration scopes, backend isolation, and approval gates before use on sensitive repositories.
```

## Overview

OpenHands is a self-hosted control center for coding agents and engineering automations.

It is useful when the goal is not just to run one standalone agent, but to coordinate developer agents, tasks, tools, repository workflows, and execution backends from a shared control plane.

## Fit for AI Lab

OpenHands belongs under `agent-orchestration/` because its main documented role is coordinating and running coding agents rather than acting as a single standalone personal agent.

Use it as a reference point for:

- self-hosted coding-agent control planes;
- repository automation with human approval gates;
- agent execution across local, remote, and cloud backends;
- engineering workflows connected to GitHub, Slack, Linear, or similar systems;
- comparison with standalone agents and multi-agent frameworks.

## Evaluation notes

Evaluate before adoption:

- deployment and upgrade model;
- supported backends and their isolation properties;
- filesystem and shell permission boundaries;
- GitHub and repository access scopes;
- human approval and review gates;
- behavior on private or sensitive repositories;
- compatibility with existing automation workflows.

## References

- OpenHands website: https://openhands.dev
- OpenHands GitHub: https://github.com/OpenHands/OpenHands
- OpenHands documentation: https://docs.all-hands.dev
