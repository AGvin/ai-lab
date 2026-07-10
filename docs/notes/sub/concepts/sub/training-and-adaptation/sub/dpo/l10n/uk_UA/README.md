<!--
l10n:
  locale: uk_UA
  source_locale: default
  source_path: ../../README.md
  source_hash: gitblob:e5dfdf988046a63e042327dc40aa01de7b95a01e
  mode: copy-through
-->

# DPO

Direct Preference Optimization trains directly on preferred and rejected response pairs.

## Переклади

- [English](../../../../l10n/uk_UA/)
- Українська — поточна

## Core idea

Direct Preference Optimization trains directly on preferred and rejected response pairs. In practical AI work, the term is useful because it names a specific part of the system rather than treating the model as a single opaque component. Understanding where it appears in the workflow makes configuration choices and failure analysis more precise.

## How it works

- DPO trains directly from preferred and rejected response pairs without a separately trained reward model and online RL loop.
- The objective increases the relative likelihood of preferred responses compared with a reference policy.
- A temperature-like parameter controls preference strength.

The exact implementation varies by model family, provider, and runtime. The important distinction is the role the concept plays in the end-to-end system and which inputs, state, or resources it changes.

## Why it matters

DPO affects how an AI system should be selected, configured, tested, or operated. It can influence output quality, resource requirements, reliability, or the amount of control available to the surrounding application.

## Practical uses

- Apply preference learning with a simpler pipeline than classical RLHF.
- Tune assistant behavior from comparison datasets.

## Example

For each prompt, training data marks one response as preferred and another as rejected.

## Trade-offs and limitations

- Quality still depends on representative preference pairs and reference-model choice.
- It may overfit stylistic preferences or degrade capabilities not represented in the data.

Do not evaluate this concept in isolation. Test it together with the actual model, data, runtime, tools, and workload that will be used in production or local experiments.

## Practical checklist

- What problem is DPO expected to solve in this workflow?
- Which inputs, settings, or resources does it depend on?
- How will success and failure be measured?
- What changes when the model, runtime, dataset, or context size changes?

## Related concepts

- [Training and Adaptation](../../../../l10n/uk_UA/)
- [RLHF](../../../rlhf/l10n/uk_UA/)
- [Distillation](../../../distillation/l10n/uk_UA/)
