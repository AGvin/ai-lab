# Orchestrator-Worker Architecture

An orchestrator-worker architecture uses a coordinating agent to plan and delegate work to specialized worker agents, then combine and validate their results.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Status

Established multi-agent pattern.

## Core idea

The orchestrator owns the overall objective, task decomposition, delegation, dependency tracking, and final synthesis. Workers receive bounded assignments and return results or artifacts.

The orchestrator does not need to be the strongest model for every worker task. Its main requirements are reliable planning, routing, state management, verification, and termination decisions.

## Typical responsibilities

### Orchestrator

- interpret the user goal and acceptance criteria;
- decompose work into tasks;
- select workers, tools, and models;
- decide whether tasks may run in parallel;
- track dependencies, budgets, and progress;
- verify worker outputs rather than trusting completion claims;
- request corrections or escalation;
- synthesize the final result.

### Worker

- execute one bounded task;
- use only the tools and permissions required for that task;
- preserve artifacts in the agreed location;
- report evidence, limitations, and unresolved failures;
- avoid modifying unrelated shared state.

## Parallel and sequential work

Independent tasks may run concurrently. Tasks that consume another task's output or modify the same state should normally run sequentially or in isolated workspaces with an explicit merge plan.

The orchestrator should build a dependency graph rather than assuming that all subtasks are either fully parallel or fully sequential.

## Strengths

- separates planning from execution;
- supports specialized prompts, tools, and models;
- enables parallel work on independent tasks;
- reduces context pressure on the coordinating agent;
- permits stronger review and escalation policies.

## Limitations

- delegation can omit requirements or duplicate work;
- worker reports can be incomplete or misleading;
- coordination and synthesis consume additional tokens;
- shared-state conflicts require explicit controls;
- a weak orchestrator can waste capable workers.

## Evidence and established usage

Anthropic describes an orchestrator-worker pattern in its multi-agent research system, where a lead agent creates specialized subagents that work in parallel and return findings for synthesis. LangChain documents a comparable subagents pattern in which a main agent coordinates specialized agents and routes work through itself.

Sources:

- [Anthropic: How we built our multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system)
- [LangChain multi-agent patterns](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/multi-agent-collaboration/)

## Related concepts

- [Multi-Agent Systems](../../)
- [Hierarchical Orchestration](../hierarchical-orchestration/)
- [Task Decomposition](../../../task-decomposition/)
- [Agent State](../../../agent-state/)
- [Verification and Reflection](../../../verification-and-reflection/)
