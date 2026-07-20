# LangGraph

Low-level orchestration framework and runtime for long-running, stateful agents.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Metadata

```text
Resource type: Agent orchestration framework and runtime
Primary use case: Build, coordinate, and run graph-structured agent workflows with durable execution, persistence, streaming, memory, and human oversight
Access model: Open-source package with optional LangChain/LangSmith ecosystem services
License: MIT
Source model: Open source core with optional hosted ecosystem services
Use rights signal: Permissive core; LangSmith, deployment, observability, hosted services, and enterprise terms must be reviewed separately
Cost model signal: Open core; local package use is open-source, while hosted observability, deployment, platform, or enterprise services may require paid terms
Deployment model: Hybrid; local package/runtime use with optional LangSmith observability, deployment, Studio, and ecosystem integrations
Adoption signal: Mainstream; GitHub-visible adoption is high and docs cite use by major companies, but production fit still needs project-specific review
Operational requirement: LangGraph package plus selected model providers, tools, runtime state storage, and optional LangSmith observability or deployment services
Integration modes: Python, JavaScript/TypeScript, LangChain components, LangSmith, model providers, tools, persistence backends, human-in-the-loop review points
Source: https://github.com/langchain-ai/langgraph
Risk notes: Agent orchestration runtime for stateful, tool-using workflows. Review tool permissions, persistence storage, checkpoint data exposure, human approval gates, provider credentials, production observability, and hosted service boundaries before use with sensitive repositories or data.
Last verified: 2026-07-06
```

## Overview

LangGraph is a low-level orchestration framework and runtime for building, managing, and deploying long-running, stateful agents.

It focuses on the infrastructure layer behind agent systems rather than a single standalone assistant or coding agent. Its core value is giving developers explicit control over graph-structured execution, agent state, persistence, streaming, and human-in-the-loop intervention.

## Fit for AI Lab

LangGraph belongs under `agent-orchestration/` because its primary documented role is coordinating and running stateful agent workflows.

Use it as a reference point for:

- graph-based agent workflow runtimes;
- durable execution for long-running agents;
- stateful workflows with checkpointing and persistence;
- human-in-the-loop approval or correction points;
- comparison with higher-level agent frameworks and standalone agents;
- production agent architecture that separates orchestration from individual model calls.

## Verification snapshot

As of 2026-07-06, the upstream GitHub repository lists LangGraph under an MIT license, and the official documentation describes it as a low-level orchestration framework and runtime for building, managing, and deploying long-running, stateful agents.

The official documentation positions LangGraph as part of a broader LangChain/LangSmith ecosystem: LangGraph can be used for orchestration, while LangSmith provides tracing, evaluation, prompts, observability, deployment, Studio, and related platform capabilities. Treat the open-source runtime and hosted ecosystem services as separate adoption surfaces.

## Evaluation notes

Evaluate before adoption:

- supported language/runtime path for the planned project;
- state persistence and checkpoint storage model;
- human-in-the-loop interruption and approval semantics;
- model and tool integration boundaries;
- observability and debugging workflow;
- operational dependency on optional LangChain or LangSmith ecosystem services;
- handling of sensitive prompt, tool, state, memory, trace, and checkpoint data;
- deployment path for production workloads.

## References

- LangGraph documentation: https://docs.langchain.com/oss/python/langgraph/overview
- LangGraph GitHub: https://github.com/langchain-ai/langgraph
