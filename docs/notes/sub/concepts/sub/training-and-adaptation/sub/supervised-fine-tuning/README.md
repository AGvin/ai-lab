# Supervised Fine-Tuning

<!--
ai_content:
  managed: true
  l10n: true
-->

Fine-tuning on labeled examples that pair inputs with desired outputs.

## Translations

- English — current
- [Українська](./l10n/uk_UA/)

## Core idea

Fine-tuning on labeled examples that pair inputs with desired outputs. In practical AI work, the term is useful because it names a specific part of the system rather than treating the model as a single opaque component. Understanding where it appears in the workflow makes configuration choices and failure analysis more precise.

## How it works

- SFT trains on explicit input-output examples and minimizes error against the desired output tokens or labels.
- Data formatting and masking determine which tokens contribute to the loss.
- High-quality examples establish instruction following, style, and task patterns.

The exact implementation varies by model family, provider, and runtime. The important distinction is the role the concept plays in the end-to-end system and which inputs, state, or resources it changes.

## Why it matters

Supervised Fine-Tuning affects how an AI system should be selected, configured, tested, or operated. It can influence output quality, resource requirements, reliability, or the amount of control available to the surrounding application.

## Practical uses

- Teach consistent task responses and domain-specific formats.
- Prepare an instruction-following model before preference optimization.

## Example

A dataset pairs bug reports with concise triage summaries and recommended next actions.

## Trade-offs and limitations

- The model can imitate errors and biases in the demonstrations.
- Coverage gaps remain when deployment inputs differ from training examples.

Do not evaluate this concept in isolation. Test it together with the actual model, data, runtime, tools, and workload that will be used in production or local experiments.

## Practical checklist

- What problem is Supervised Fine-Tuning expected to solve in this workflow?
- Which inputs, settings, or resources does it depend on?
- How will success and failure be measured?
- What changes when the model, runtime, dataset, or context size changes?

## Related concepts

- [Training and Adaptation](../../)
- [QLoRA](../qlora/)
- [Adapters](../adapters/)
