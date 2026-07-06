# CrewAI

Multi-agent orchestration framework and platform for collaborative AI agents and controlled workflows.

## Metadata

```text
Resource type: Agent orchestration framework and platform
Primary use case: Build and coordinate role-based agent crews, tasks, tools, and controlled flows for multi-agent automation workflows
Access model: Open-source framework with optional cloud, enterprise, and platform services
License: MIT for the open-source framework
Source model: Open source core with commercial platform services
Use rights signal: Permissive core; cloud, enterprise console, managed deployment, connectors, support, and commercial platform terms must be reviewed separately
Cost model signal: Open core; framework use is open-source, while cloud, enterprise, hosted, or managed features may require paid service terms
Deployment model: Hybrid; local framework and CLI development with optional enterprise console, deployment, triggers, integrations, and platform services
Adoption signal: Popular; GitHub-visible adoption is high and docs present production-oriented capabilities, but production maturity still needs project-specific review
Operational requirement: CrewAI framework plus selected model providers, tools, credentials, runtime environment, and optional platform services
Integration modes: Python, crews, agents, tasks, tools, flows, knowledge sources, model providers, external APIs, observability and deployment services, triggers, enterprise console, RBAC
Source: https://github.com/crewAIInc/crewAI
Risk notes: Multi-agent orchestration framework and platform for tool-using automations. Review tool permissions, delegated task boundaries, provider credentials, memory or knowledge-source data exposure, platform service dependencies, hosted deployment model, RBAC, and human approval gates before use with sensitive workflows.
Last verified: 2026-07-06
```

## Overview

CrewAI is a framework and platform for creating collaborative AI agent systems.

Its core abstraction is a crew: a group of role-based agents that can be assigned goals, tasks, tools, and process rules. CrewAI also supports flows for more controlled, event-driven workflows where deterministic application logic and agent steps need to be combined.

## Fit for AI Lab

CrewAI belongs under `agent-orchestration/` because its primary documented role is coordinating multiple agents, tasks, tools, and workflows rather than acting as a single standalone agent.

Use it as a reference point for:

- role-based multi-agent coordination;
- task delegation across agent crews;
- workflow designs that mix autonomous collaboration with controlled flows;
- comparison with graph-based runtimes such as LangGraph;
- comparison with standalone coding agents and assistant products;
- evaluation of business-process automation built on agent teams.

## Verification snapshot

As of 2026-07-06, the upstream GitHub repository describes CrewAI as an open-source Python framework for production-ready multi-agent workflows and states that CrewAI is released under the MIT License.

The official documentation also presents cloud and enterprise-oriented capabilities, including deployment, triggers, team management, RBAC, integrations, and an enterprise console. Treat the open-source framework and the hosted or enterprise platform as separate adoption surfaces.

## Evaluation notes

Evaluate before adoption:

- clarity of crew, agent, task, and flow boundaries;
- amount of deterministic control needed versus autonomous delegation;
- supported model providers and tool integrations;
- memory, knowledge-source, and credential exposure;
- observability and debugging model for multi-agent runs;
- production deployment and upgrade path;
- optional hosted, cloud, or enterprise service dependencies;
- RBAC, auditability, and operational controls for business use.

## References

- CrewAI documentation: https://docs.crewai.com
- CrewAI GitHub: https://github.com/crewAIInc/crewAI
- CrewAI website: https://crewai.com
