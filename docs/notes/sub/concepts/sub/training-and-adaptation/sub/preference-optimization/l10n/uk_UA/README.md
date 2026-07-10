<!--
l10n:
  locale: uk_UA
  source_locale: default
  source_path: ../../README.md
  source_hash: gitblob:5e34a068f2eafb24dbd5cb383da399ce1417d35a
  mode: copy-through
-->

# Preference Optimization

Training methods that favor responses judged better according to preference data.

## Переклади

- [English](../../)
- Українська — поточна

## Core idea

Training methods that favor responses judged better according to preference data. In practical AI work, the term is useful because it names a specific part of the system rather than treating the model as a single opaque component. Understanding where it appears in the workflow makes configuration choices and failure analysis more precise.

## How it works

- Preference optimization uses comparisons or scores indicating which responses are preferred.
- The method adjusts behavior toward preferred outputs while usually constraining divergence from a reference model.
- Implementations include reinforcement-learning and direct optimization approaches.

The exact implementation varies by model family, provider, and runtime. The important distinction is the role the concept plays in the end-to-end system and which inputs, state, or resources it changes.

## Why it matters

Preference Optimization affects how an AI system should be selected, configured, tested, or operated. It can influence output quality, resource requirements, reliability, or the amount of control available to the surrounding application.

## Practical uses

- Improve helpfulness, style, safety, and response ranking after SFT.
- Align model behavior with explicit product criteria.

## Example

Annotators choose the clearer of two support replies and those pairs train the model’s response preference.

## Trade-offs and limitations

- Preference data can encode annotator bias or reward superficial traits.
- Optimizing one preference metric can reduce other useful capabilities.

Do not evaluate this concept in isolation. Test it together with the actual model, data, runtime, tools, and workload that will be used in production or local experiments.

## Practical checklist

- What problem is Preference Optimization expected to solve in this workflow?
- Which inputs, settings, or resources does it depend on?
- How will success and failure be measured?
- What changes when the model, runtime, dataset, or context size changes?

## Related concepts

- [Training and Adaptation](../../../../l10n/uk_UA/)
- [Pretraining](../../../pretraining/l10n/uk_UA/)
- [RLHF](../../../rlhf/l10n/uk_UA/)
