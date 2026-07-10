# Model Routing

<!--
ai_content:
  managed: true
  l10n: true
-->

Selecting among models dynamically according to the request or operating policy.

## Translations

- English — current
- [Українська](./l10n/uk_UA/)

## Core idea

Selecting among models dynamically according to the request or operating policy. In practical AI work, the term is useful because it names a specific part of the system rather than treating the model as a single opaque component. Understanding where it appears in the workflow makes configuration choices and failure analysis more precise.

## How it works

- Model routing applies rules or a classifier to send each request to an appropriate model.
- Signals can include task type, complexity, modality, privacy, budget, latency target, and prior failure.
- Fallback logic handles unavailable or low-confidence results.

The exact implementation varies by model family, provider, and runtime. The important distinction is the role the concept plays in the end-to-end system and which inputs, state, or resources it changes.

## Why it matters

Model Routing affects how an AI system should be selected, configured, tested, or operated. It can influence output quality, resource requirements, reliability, or the amount of control available to the surrounding application.

## Practical uses

- Reduce cost while preserving quality for difficult requests.
- Keep sensitive tasks local and route permitted tasks to hosted models.

## Example

Simple extraction goes to a fast model, while multi-file code analysis goes to a reasoning model.

## Trade-offs and limitations

- Misclassification can send a hard task to a weak model or expose data to the wrong provider.
- Routing adds another component that needs evaluation and observability.

Do not evaluate this concept in isolation. Test it together with the actual model, data, runtime, tools, and workload that will be used in production or local experiments.

## Practical checklist

- What problem is Model Routing expected to solve in this workflow?
- Which inputs, settings, or resources does it depend on?
- How will success and failure be measured?
- What changes when the model, runtime, dataset, or context size changes?

## Related concepts

- [Evaluation and Operations](../../)
- [Model Selection](../model-selection/)
- [Observability](../observability/)
