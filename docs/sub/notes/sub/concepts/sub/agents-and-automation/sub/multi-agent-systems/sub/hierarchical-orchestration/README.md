# Hierarchical Agent Orchestration

Hierarchical agent orchestration organizes multiple agents into management levels, where supervisors coordinate specialist teams and may themselves report to higher-level supervisors.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Status

Established multi-agent architecture pattern.

## Core idea

A hierarchy is useful when one coordinator would otherwise need to retain too much domain context, manage too many workers, or enforce several distinct policies. Each manager owns a bounded scope and reports structured results to the manager above it.

Typical levels may include:

- a top-level orchestrator responsible for the global objective, budget, dependencies, and final acceptance;
- domain or department managers responsible for coherent workstreams such as software, localization, design, research, or operations;
- team leads responsible for smaller units such as frontend, UX, testing, or image evaluation;
- worker agents responsible for bounded execution tasks.

## Management contract

Every manager should receive:

- an explicit scope and objective;
- authority and permission boundaries;
- budget and resource constraints;
- quality and completion criteria;
- the agents, models, and tools it may use;
- a reporting schema for progress, evidence, risks, and unresolved work;
- escalation conditions.

Managers should summarize subordinate work without hiding evidence required for validation.

## When hierarchy helps

Use hierarchy when it:

- reduces context overload;
- separates specialized policies and toolsets;
- enables meaningful parallel execution;
- isolates permissions or infrastructure;
- provides clear ownership for large project areas;
- allows local decisions without losing global coordination.

Do not add management layers when a simple workflow graph or one orchestrator-worker loop is easier to inspect and operate.

## Cross-team dependencies

The top-level orchestrator should own dependencies between units. Lower-level managers should not silently modify another unit's state or assumptions.

For shared resources, define:

- the owning unit;
- read and write boundaries;
- handoff artifacts;
- version or snapshot rules;
- merge and conflict-resolution responsibility;
- escalation paths.

## Trade-offs

- additional managers consume tokens and execution time;
- summaries may lose important detail;
- errors can propagate upward through trusted reports;
- unclear scopes create duplicated or abandoned work;
- excessive hierarchy can obscure accountability;
- local optimization may conflict with the global objective.

## Established usage

LangGraph documents multi-level supervisor systems in which a top-level supervisor manages subordinate supervisor teams. AutoGen documents teams with planning agents and model-selected participants, demonstrating related manager-and-specialist coordination patterns.

Sources:

- [LangGraph Multi-Agent Supervisor](https://langchain-ai.github.io/langgraphjs/reference/modules/langgraph-supervisor.html)
- [AutoGen Selector Group Chat](https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/selector-group-chat.html)

## Related concepts

- [Multi-Agent Systems](../../)
- [Orchestrator-Worker Architecture](../orchestrator-worker/)
- [Task Decomposition](../../../task-decomposition/)
- [Agent State](../../../agent-state/)
