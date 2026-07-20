# Task Decomposition

Task decomposition divides a large objective into smaller units that can be executed, validated, and recombined.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Core idea

Decomposition reduces cognitive and context load by isolating responsibilities. A useful subtask has a clear input, expected output, dependencies, and completion criterion. Subtasks may run sequentially or in parallel when they do not share mutable state.

## Practical use

- Split research into source discovery, evidence extraction, comparison, and synthesis.
- Separate code changes by component or responsibility.
- Divide document processing into independent files or sections.
- Assign specialized subtasks to different tools or agents.

## Design guidance

Decompose around meaningful boundaries, not arbitrary token sizes. Preserve enough context for each subtask to make correct decisions. Define how conflicts and duplicate work will be reconciled before running subtasks in parallel.

## Trade-offs and limitations

Excessive decomposition creates coordination overhead and loses global context. Poorly separated tasks can produce incompatible outputs or repeat the same work.

## Common mistakes

- Creating subtasks with vague completion criteria.
- Splitting work that depends on shared hidden assumptions.
- Merging outputs without validation.
- Using multiple agents when a deterministic loop would be simpler.

## Related concepts

- [Agents and Automation](../../)
- [Planning](../planning/)
- [Multi-Agent Systems](../multi-agent-systems/)
- [Agentic Workflows](../agentic-workflows/)
