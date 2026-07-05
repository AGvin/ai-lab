# CrewAI

Multi-agent orchestration framework and platform for collaborative AI agents and controlled workflows.

## Metadata

```text
Resource type: Agent orchestration framework and platform
Primary use case: Build and coordinate role-based agent crews, tasks, tools, and controlled flows for multi-agent automation workflows
Access model: Open-source framework with optional hosted or enterprise ecosystem services
License: MIT
Source model: Open source
Operational requirement: CrewAI framework plus selected model providers, tools, credentials, runtime environment, and optional platform services
Integration modes: Python, crews, agents, tasks, tools, flows, knowledge sources, model providers, external APIs, observability and deployment services
Source: https://github.com/crewAIInc/crewAI
Risk notes: Multi-agent orchestration framework for tool-using automations; review tool permissions, delegated task boundaries, provider credentials, memory or knowledge-source data exposure, platform service dependencies, and human approval gates before use with sensitive workflows.
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

## Evaluation notes

Evaluate before adoption:

- clarity of crew, agent, task, and flow boundaries;
- amount of deterministic control needed versus autonomous delegation;
- supported model providers and tool integrations;
- memory, knowledge-source, and credential exposure;
- observability and debugging model for multi-agent runs;
- production deployment and upgrade path;
- optional hosted or enterprise service dependencies.

## References

- CrewAI documentation: https://docs.crewai.com
- CrewAI GitHub: https://github.com/crewAIInc/crewAI
