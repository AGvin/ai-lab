# Autonomy Levels

The degree of independent decision-making and action granted to an AI system.

## Core idea

The degree of independent decision-making and action granted to an AI system. In practical AI work, the term is useful because it names a specific part of the system rather than treating the model as a single opaque component. Understanding where it appears in the workflow makes configuration choices and failure analysis more precise.

## How it works

- Autonomy level describes how much the system can decide and execute without human intervention.
- A spectrum can range from suggestion-only, through approval-gated actions, to bounded autonomous operation.
- Permissions, budgets, tool allowlists, and escalation rules should match the chosen level.

The exact implementation varies by model family, provider, and runtime. The important distinction is the role the concept plays in the end-to-end system and which inputs, state, or resources it changes.

## Why it matters

Autonomy Levels affects how an AI system should be selected, configured, tested, or operated. It can influence output quality, resource requirements, reliability, or the amount of control available to the surrounding application.

## Practical uses

- Choose appropriate control for low-risk versus high-risk tasks.
- Communicate what an agent is allowed to do rather than using the vague label “autonomous.”

## Example

A repository assistant may autonomously read and analyze, require approval to commit, and never merge without an explicit owner instruction.

## Trade-offs and limitations

- Autonomy labels are meaningless without concrete permissions and boundaries.
- A low-risk task can become high-risk when connected to broader credentials or data.

Do not evaluate this concept in isolation. Test it together with the actual model, data, runtime, tools, and workload that will be used in production or local experiments.

## Practical checklist

- What problem is Autonomy Levels expected to solve in this workflow?
- Which inputs, settings, or resources does it depend on?
- How will success and failure be measured?
- What changes when the model, runtime, dataset, or context size changes?

## Related concepts

- [Agents and Automation](../../)
- [Retries](../retries/)
- [Multi-Agent Systems](../multi-agent-systems/)
