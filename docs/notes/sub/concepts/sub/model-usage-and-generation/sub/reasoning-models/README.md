# Reasoning Models

Models optimized to spend additional computation on multi-step problem solving.

## Core idea

Models optimized to spend additional computation on multi-step problem solving. In practical AI work, the term is useful because it names a specific part of the system rather than treating the model as a single opaque component. Understanding where it appears in the workflow makes configuration choices and failure analysis more precise.

## How it works

- Reasoning-oriented models allocate additional inference computation to planning, verification, search, or intermediate internal processing.
- Some expose a reasoning-effort control or separate reasoning-token accounting; implementations differ by provider.
- They are often paired with tools and structured checks for mathematics, coding, and multi-step decisions.

The exact implementation varies by model family, provider, and runtime. The important distinction is the role the concept plays in the end-to-end system and which inputs, state, or resources it changes.

## Why it matters

Reasoning Models affects how an AI system should be selected, configured, tested, or operated. It can influence output quality, resource requirements, reliability, or the amount of control available to the surrounding application.

## Practical uses

- Handle tasks that require decomposition, constraint tracking, or several dependent steps.
- Improve code analysis, planning, and difficult problem solving when latency is acceptable.

## Example

A reasoning model may analyze repository dependencies, propose an ordered migration, and verify the plan against explicit constraints before answering.

## Trade-offs and limitations

- Additional reasoning time does not guarantee correctness.
- They can be slower and more expensive than a smaller direct-response model on simple tasks.

Do not evaluate this concept in isolation. Test it together with the actual model, data, runtime, tools, and workload that will be used in production or local experiments.

## Practical checklist

- What problem is Reasoning Models expected to solve in this workflow?
- Which inputs, settings, or resources does it depend on?
- How will success and failure be measured?
- What changes when the model, runtime, dataset, or context size changes?

## Related concepts

- [Model Usage and Generation](../../)
- [Sampling Parameters](../sampling-parameters/)
- [Model Capabilities and Limitations](../model-capabilities-and-limitations/)
