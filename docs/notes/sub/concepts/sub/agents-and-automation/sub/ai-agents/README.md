# AI Agents

An AI agent is a system that uses a model to pursue a goal through observations, decisions, tool calls, state changes, and repeated actions.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Core idea

A model becomes part of an agent when it can do more than produce a single response. The surrounding application gives it tools, working state, control flow, stopping rules, permissions, and feedback from previous actions. The agent is therefore the complete system, not only the language model.

## Typical components

- A goal or task description.
- A model that selects or proposes actions.
- Tools such as APIs, search, code execution, or file operations.
- State that records progress and intermediate results.
- A loop that observes results and decides what to do next.
- Policies for approval, failure handling, and termination.

## Practical use

Agents are useful for tasks where the next action depends on earlier results: repository maintenance, research, multi-system administration, data processing, or customer-support workflows. Keep deterministic steps outside the model when possible and use the model where interpretation or flexible decisions are needed.

## Trade-offs and limitations

More autonomy increases flexibility but also cost, latency, and the possibility of incorrect or unsafe actions. Agent behavior can be difficult to reproduce because every tool result changes subsequent decisions.

## Common mistakes

- Calling a single model request an agent.
- Granting broad credentials without least-privilege controls.
- Omitting stop conditions or maximum action budgets.
- Treating model-generated plans as trusted instructions.

## Related concepts

- [Agents and Automation](../../)
- [Agentic Workflows](../agentic-workflows/)
- [Tool Calling](../tool-calling/)
- [Autonomy Levels](../autonomy-levels/)