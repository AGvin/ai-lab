# AutoGen

Multi-agent conversation framework for building agent systems with conversable agents, tools, code execution, and human-in-the-loop workflows.

## Metadata

```text
Resource type: Agent orchestration framework
Primary use case: Build and coordinate multi-agent systems through conversable agents, tool use, code execution, and human participation
Access model: Open-source project with local framework usage and related Microsoft research tooling
License: MIT
Source model: Open source
Operational requirement: AutoGen framework plus selected model providers, tools, credentials, code execution environment, and optional Studio or ecosystem tooling
Integration modes: Python, conversable agents, multi-agent conversations, tool execution, code execution, human-in-the-loop workflows, model providers, AutoGen Studio
Source: https://github.com/microsoft/autogen
Risk notes: Multi-agent and code-execution framework; review sandboxing, browser access, localhost exposure, tool permissions, generated code execution, provider credentials, and human approval gates before use with sensitive repositories or data.
```

## Overview

AutoGen is a framework for building multi-agent AI applications around conversations between agents.

Its core idea is that agents can be made conversable: they exchange messages, call tools, execute code, ask for human input, and coordinate toward a task through structured interaction patterns.

## Fit for AI Lab

AutoGen belongs under `agent-orchestration/` because its primary documented role is coordinating multiple agents and interaction protocols rather than acting as a single standalone agent.

Use it as a reference point for:

- multi-agent conversation patterns;
- agent collaboration through message passing;
- workflows that combine LLM agents, tools, code execution, and human checkpoints;
- comparison with graph-based runtimes such as LangGraph;
- comparison with crew/task abstractions such as CrewAI;
- evaluating development tools such as AutoGen Studio.

## Evaluation notes

Evaluate before adoption:

- maturity of the current AutoGen package line and migration path;
- supported model providers and tool integrations;
- code execution sandboxing and filesystem boundaries;
- browser, localhost, and network exposure in development tools;
- human-in-the-loop approval semantics;
- observability and debugging workflow for multi-agent runs;
- handling of sensitive prompts, credentials, source code, and execution artifacts.

## References

- AutoGen GitHub: https://github.com/microsoft/autogen
- AutoGen documentation: https://microsoft.github.io/autogen
- AutoGen paper: https://arxiv.org/abs/2308.08155
