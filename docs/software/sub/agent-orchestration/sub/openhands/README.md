# OpenHands

Self-hosted developer control center for coding agents and automations.

## Metadata

```text
Resource type: Agent orchestration platform and coding-agent control center
Primary use case: Run and coordinate coding agents across local, remote, cloud, and enterprise backends for repository and engineering automation tasks
Access model: Open-source core with self-hosted deployment options, OpenHands Cloud, and OpenHands Enterprise
License: MIT for core OpenHands and agent-server Docker images; enterprise directory uses a separate enterprise license
Source model: Open source core with source-available enterprise components
Use rights signal: Permissive core; OpenHands Cloud, OpenHands Enterprise, enterprise directory, managed infrastructure, and third-party coding-agent/provider terms must be reviewed separately
Cost model signal: Open core; self-hosted core is MIT-licensed, while cloud, enterprise, hosted infrastructure, model providers, and third-party agents may introduce paid terms
Deployment model: Hybrid; runs locally by default and can connect to local, Docker, VM, company infrastructure, OpenHands Cloud, or OpenHands Enterprise backends
Adoption signal: Mainstream; GitHub-visible adoption is high, but production use must review backend isolation, licensing, and operational controls
Operational requirement: Runtime for OpenHands plus selected agent/model/provider credentials and configured local, remote, cloud, or enterprise backends or integrations
Integration modes: Agent Canvas, local backends, remote backends, cloud backends, GitHub, Slack, Linear, Jira, Notion, ACP-compatible agents, coding agents, automations, OpenHands Cloud, OpenHands Enterprise
Source: https://github.com/OpenHands/OpenHands
Risk notes: High-trust coding-agent control center. Review workspace isolation, filesystem access, shell access, repository permissions, integration scopes, backend isolation, automation triggers, cloud/enterprise boundaries, and approval gates before use on sensitive repositories.
Last verified: 2026-07-06
```

## Overview

OpenHands is a self-hosted control center for coding agents and engineering automations.

It is useful when the goal is not just to run one standalone agent, but to coordinate developer agents, tasks, tools, repository workflows, automations, and execution backends from a shared control plane.

## Fit for AI Lab

OpenHands belongs under `agent-orchestration/` because its main documented role is coordinating and running coding agents rather than acting as a single standalone personal agent.

Use it as a reference point for:

- self-hosted coding-agent control planes;
- repository automation with human approval gates;
- agent execution across local, remote, cloud, and enterprise backends;
- engineering workflows connected to GitHub, Slack, Linear, Jira, Notion, or similar systems;
- comparison with standalone agents and multi-agent frameworks.

## Verification snapshot

As of 2026-07-06, the official documentation describes Agent Canvas as a browser-based UI and backend server for running agents and automations. It can run locally, be self-hosted on a VM, or connect to OpenHands Cloud.

The official documentation distinguishes OpenHands Cloud and OpenHands Enterprise. It states that Enterprise can be self-hosted in a customer's VPC via Kubernetes and requires a license beyond one month. It also states that all work is available under MIT except the `enterprise/` directory, while the core `openhands` and `agent-server` Docker images are fully MIT-licensed.

## Evaluation notes

Evaluate before adoption:

- deployment and upgrade model;
- core versus cloud versus enterprise license boundaries;
- supported backends and their isolation properties;
- filesystem and shell permission boundaries;
- GitHub and repository access scopes;
- Slack, Linear, Jira, Notion, and other integration scopes;
- human approval and review gates;
- behavior on private or sensitive repositories;
- compatibility with existing automation workflows;
- whether agents run locally, in Docker, on VMs, in company infrastructure, or in OpenHands-hosted infrastructure.

## References

- OpenHands website: https://openhands.dev
- OpenHands GitHub: https://github.com/OpenHands/OpenHands
- OpenHands documentation: https://docs.openhands.dev
- OpenHands introduction: https://docs.openhands.dev/overview/introduction
