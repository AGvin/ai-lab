# Few-Shot Prompting

Prompting that includes a small number of examples to demonstrate desired behavior.

## Core idea

Prompting that includes a small number of examples to demonstrate desired behavior. In practical AI work, the term is useful because it names a specific part of the system rather than treating the model as a single opaque component. Understanding where it appears in the workflow makes configuration choices and failure analysis more precise.

## How it works

- Few-shot prompting includes a small set of input-output examples before the new task.
- Examples communicate formatting, classification boundaries, terminology, and edge-case behavior more concretely than abstract instructions alone.
- The model infers a temporary pattern from the examples without changing its stored weights.

The exact implementation varies by model family, provider, and runtime. The important distinction is the role the concept plays in the end-to-end system and which inputs, state, or resources it changes.

## Why it matters

Few-Shot Prompting affects how an AI system should be selected, configured, tested, or operated. It can influence output quality, resource requirements, reliability, or the amount of control available to the surrounding application.

## Practical uses

- Stabilize labels, style, or transformations when a schema alone is insufficient.
- Demonstrate how ambiguous or exceptional cases should be handled.

## Example

A support triage prompt can show examples of urgent, normal, and informational messages before asking the model to classify a new email.

## Trade-offs and limitations

- Examples consume context and can accidentally teach unintended patterns.
- A small example set may not cover the real input distribution.

Do not evaluate this concept in isolation. Test it together with the actual model, data, runtime, tools, and workload that will be used in production or local experiments.

## Practical checklist

- What problem is Few-Shot Prompting expected to solve in this workflow?
- Which inputs, settings, or resources does it depend on?
- How will success and failure be measured?
- What changes when the model, runtime, dataset, or context size changes?

## Related concepts

- [Model Usage and Generation](../../)
- [Hallucinations](../hallucinations/)
- [Sampling Parameters](../sampling-parameters/)
