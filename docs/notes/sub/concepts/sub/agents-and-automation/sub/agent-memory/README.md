# Agent Memory

<!--
ai_content:
  managed: true
  l10n: true
-->

Mechanisms that preserve useful information beyond the immediate model request.

## Translations

- English — current
- [Українська](./l10n/uk_UA/)

## Core idea

Mechanisms that preserve useful information beyond the immediate model request. In practical AI work, the term is useful because it names a specific part of the system rather than treating the model as a single opaque component. Understanding where it appears in the workflow makes configuration choices and failure analysis more precise.

## How it works

- Agent memory stores information beyond the immediate context window.
- Short-term memory may summarize the current task, while long-term memory may use databases, vector search, profiles, or event histories.
- Memory retrieval should be scoped, permission-aware, and treated as fallible external data.

The exact implementation varies by model family, provider, and runtime. The important distinction is the role the concept plays in the end-to-end system and which inputs, state, or resources it changes.

## Why it matters

Agent Memory affects how an AI system should be selected, configured, tested, or operated. It can influence output quality, resource requirements, reliability, or the amount of control available to the surrounding application.

## Practical uses

- Remember user preferences, past decisions, or project facts across sessions.
- Reduce repeated discovery work in long-lived assistants.

## Example

An assistant remembers that a repository uses squash merges but rechecks current repository rules before acting.

## Trade-offs and limitations

- Stored memories can become stale, incorrect, or privacy-sensitive.
- Memory is not the same as authoritative knowledge and should not silently override current instructions.

Do not evaluate this concept in isolation. Test it together with the actual model, data, runtime, tools, and workload that will be used in production or local experiments.

## Practical checklist

- What problem is Agent Memory expected to solve in this workflow?
- Which inputs, settings, or resources does it depend on?
- How will success and failure be measured?
- What changes when the model, runtime, dataset, or context size changes?

## Related concepts

- [Agents and Automation](../../)
- [Agent State](../agent-state/)
- [Planning](../planning/)
