# Model Selection

Choosing a model based on task quality, capabilities, cost, latency, safety, and deployment constraints.

## Translations

- English — current
- [Українська](./l10n/uk_UA/)

## Core idea

Choosing a model based on task quality, capabilities, cost, latency, safety, and deployment constraints. In practical AI work, the term is useful because it names a specific part of the system rather than treating the model as a single opaque component. Understanding where it appears in the workflow makes configuration choices and failure analysis more precise.

## How it works

- Model selection compares candidate models against task requirements, quality evals, cost, latency, context, modalities, licensing, and deployment constraints.
- The decision may choose different models for different stages rather than one universal model.
- Selection should use current versions and representative inputs.

The exact implementation varies by model family, provider, and runtime. The important distinction is the role the concept plays in the end-to-end system and which inputs, state, or resources it changes.

## Why it matters

Model Selection affects how an AI system should be selected, configured, tested, or operated. It can influence output quality, resource requirements, reliability, or the amount of control available to the surrounding application.

## Practical uses

- Choose hosted or local models for production workflows.
- Avoid paying for capability that a task does not need.

## Example

A small local model handles private classification while a stronger hosted model is reserved for complex analysis.

## Trade-offs and limitations

- Provider models and pricing change, so decisions require periodic review.
- A benchmark winner may fail operational or legal requirements.

Do not evaluate this concept in isolation. Test it together with the actual model, data, runtime, tools, and workload that will be used in production or local experiments.

## Practical checklist

- What problem is Model Selection expected to solve in this workflow?
- Which inputs, settings, or resources does it depend on?
- How will success and failure be measured?
- What changes when the model, runtime, dataset, or context size changes?

## Related concepts

- [Evaluation and Operations](../../)
- [Evals](../evals/)
- [Model Routing](../model-routing/)
