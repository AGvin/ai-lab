# Overfitting

When a model fits training data too closely and performs poorly on new examples.

## Translations

- English — current
- [Українська](./l10n/uk_UA/)

## Core idea

When a model fits training data too closely and performs poorly on new examples. In practical AI work, the term is useful because it names a specific part of the system rather than treating the model as a single opaque component. Understanding where it appears in the workflow makes configuration choices and failure analysis more precise.

## How it works

- Overfitting occurs when training performance improves while generalization to unseen data stagnates or worsens.
- It can result from excessive capacity, too little data, leakage, repeated epochs, or narrow examples.
- Validation curves and held-out tasks help detect it.

The exact implementation varies by model family, provider, and runtime. The important distinction is the role the concept plays in the end-to-end system and which inputs, state, or resources it changes.

## Why it matters

Overfitting affects how an AI system should be selected, configured, tested, or operated. It can influence output quality, resource requirements, reliability, or the amount of control available to the surrounding application.

## Practical uses

- Decide when to stop training or add regularization and data diversity.
- Interpret why an adapter performs well on demonstrations but poorly in production.

## Example

A LoRA memorizes exact product descriptions but fails when customers ask equivalent questions in new wording.

## Trade-offs and limitations

- A single test set can hide overfitting when it resembles training data.
- Reducing training loss is not the same as improving useful behavior.

Do not evaluate this concept in isolation. Test it together with the actual model, data, runtime, tools, and workload that will be used in production or local experiments.

## Practical checklist

- What problem is Overfitting expected to solve in this workflow?
- Which inputs, settings, or resources does it depend on?
- How will success and failure be measured?
- What changes when the model, runtime, dataset, or context size changes?

## Related concepts

- [Training and Adaptation](../../)
- [Datasets](../datasets/)
- [Pretraining](../pretraining/)
