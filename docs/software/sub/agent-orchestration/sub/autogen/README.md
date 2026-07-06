# AutoGen

Multi-agent conversation framework for building agent systems with conversable agents, tools, code execution, and human-in-the-loop workflows.

## Metadata

```text
Resource type: Agent orchestration framework
Primary use case: Build and coordinate multi-agent systems through conversable agents, tool use, code execution, and human participation
Access model: Open-source project with local framework usage and related Microsoft research tooling
License: MIT for code; CC-BY-4.0 for documentation and other repository content
Source model: Open source
Use rights signal: Permissive core; Microsoft trademarks, cloud services, model providers, and third-party integrations must be reviewed separately
Cost model signal: BYO cost; framework use is open-source, but useful operation depends on selected model providers, execution environments, tools, and optional infrastructure
Deployment model: Hybrid; local framework usage with optional tools, code execution environments, providers, and Studio/ecosystem tooling
Adoption signal: Popular; GitHub-visible adoption is high, but package-line maturity and migration path still need project-specific review
Operational requirement: AutoGen framework plus selected model providers, tools, credentials, code execution environment, and optional Studio or ecosystem tooling
Integration modes: Python, conversable agents, multi-agent conversations, tool execution, code execution, human-in-the-loop workflows, model providers, AutoGen Studio
Source: https://github.com/microsoft/autogen
Risk notes: Multi-agent and code-execution framework. Review sandboxing, browser access, localhost exposure, tool permissions, generated code execution, provider credentials, data passed to model APIs, and human approval gates before use with sensitive repositories or data.
Last verified: 2026-07-06
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

## Verification snapshot

As of 2026-07-06, the upstream GitHub repository describes AutoGen as a programming framework for agentic AI. The repository legal notice says code is licensed under MIT and documentation/other content under CC-BY-4.0.

The current upstream repository still points to AutoGen documentation and AutoGen Studio-related material, but adoption should include a package-line and migration-path review because AutoGen has gone through multiple package and API phases.

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
- AutoGen Studio paper: https://arxiv.org/abs/2408.15247
