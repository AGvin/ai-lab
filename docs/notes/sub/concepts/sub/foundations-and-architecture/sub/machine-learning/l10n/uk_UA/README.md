<!--
l10n:
  locale: uk_UA
  source_locale: default
  source_path: ../../README.md
  source_hash: gitblob:bee61bfd35f92cfa5f4c578c79fb74be4990ded3
  mode: copy-through
-->

# Machine Learning

Methods that learn patterns from data instead of relying only on explicitly programmed rules.

## Переклади

- [English](../../../../l10n/uk_UA/)
- Українська — поточна

## Core idea

Methods that learn patterns from data instead of relying only on explicitly programmed rules. In practical AI work, the term is useful because it names a specific part of the system rather than treating the model as a single opaque component. Understanding where it appears in the workflow makes configuration choices and failure analysis more precise.

## How it works

- A machine-learning model estimates patterns from examples instead of relying only on manually written rules.
- Training adjusts model parameters to reduce an objective or improve a measured task, while inference applies the learned parameters to new input.
- Supervised, unsupervised, self-supervised, and reinforcement-learning methods differ in where the learning signal comes from.

The exact implementation varies by model family, provider, and runtime. The important distinction is the role the concept plays in the end-to-end system and which inputs, state, or resources it changes.

## Why it matters

Machine Learning affects how an AI system should be selected, configured, tested, or operated. It can influence output quality, resource requirements, reliability, or the amount of control available to the surrounding application.

## Practical uses

- Recognize when behavior depends on learned data rather than deterministic code.
- Evaluate the importance of training data, validation data, drift, and retraining.

## Example

A spam classifier learns from labeled messages and predicts whether a new message resembles previously observed spam patterns.

## Trade-offs and limitations

- A learned correlation is not automatically causal or reliable outside the training distribution.
- Performance can degrade when real-world data changes or differs from evaluation data.

Do not evaluate this concept in isolation. Test it together with the actual model, data, runtime, tools, and workload that will be used in production or local experiments.

## Practical checklist

- What problem is Machine Learning expected to solve in this workflow?
- Which inputs, settings, or resources does it depend on?
- How will success and failure be measured?
- What changes when the model, runtime, dataset, or context size changes?

## Related concepts

- [Foundations and Architecture](../../../../l10n/uk_UA/)
- [Artificial Intelligence](../../../artificial-intelligence/l10n/uk_UA/)
- [Deep Learning](../../../deep-learning/l10n/uk_UA/)
