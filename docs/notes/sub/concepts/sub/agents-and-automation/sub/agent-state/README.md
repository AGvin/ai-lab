# Agent State

The explicit working data that tracks progress, decisions, and intermediate results.

## Translations

- English — current
- [Українська](./l10n/uk_UA/)

## Core idea

The explicit working data that tracks progress, decisions, and intermediate results. In practical AI work, the term is useful because it names a specific part of the system rather than treating the model as a single opaque component. Understanding where it appears in the workflow makes configuration choices and failure analysis more precise.

## How it works

- Agent state is the explicit record of the current task, inputs, completed steps, pending actions, tool results, and errors.
- State can live in memory for short runs or in durable storage for resumable workflows.
- Each workflow step should read and update a defined subset of state rather than relying on an unstructured transcript.

The exact implementation varies by model family, provider, and runtime. The important distinction is the role the concept plays in the end-to-end system and which inputs, state, or resources it changes.

## Why it matters

Agent State affects how an AI system should be selected, configured, tested, or operated. It can influence output quality, resource requirements, reliability, or the amount of control available to the surrounding application.

## Practical uses

- Resume interrupted tasks and inspect how a result was produced.
- Coordinate branches, approvals, retries, and multi-step dependencies.

## Example

A pull-request agent stores the target repository, branch, changed files, validation results, and whether owner approval was received.

## Trade-offs and limitations

- Unbounded state grows context and storage costs.
- Stale or inconsistent state can cause duplicated or unsafe actions.

Do not evaluate this concept in isolation. Test it together with the actual model, data, runtime, tools, and workload that will be used in production or local experiments.

## Practical checklist

- What problem is Agent State expected to solve in this workflow?
- Which inputs, settings, or resources does it depend on?
- How will success and failure be measured?
- What changes when the model, runtime, dataset, or context size changes?

## Related concepts

- [Agents and Automation](../../)
- [Tool Calling](../tool-calling/)
- [Agent Memory](../agent-memory/)
