# LoRA

<!--
ai_content:
  managed: true
  l10n: true
-->

Low-Rank Adaptation trains compact low-rank updates instead of all base model weights.

## Translations

- English — current
- [Українська](./l10n/uk_UA/)

## Core idea

Low-Rank Adaptation trains compact low-rank updates instead of all base model weights. In practical AI work, the term is useful because it names a specific part of the system rather than treating the model as a single opaque component. Understanding where it appears in the workflow makes configuration choices and failure analysis more precise.

## How it works

- LoRA freezes the original weight matrix and learns a low-rank update represented by two smaller matrices.
- The update can remain as a separate adapter or be merged into compatible base weights for deployment.
- Rank, target modules, scaling, learning rate, and training data determine capacity and behavior.

The exact implementation varies by model family, provider, and runtime. The important distinction is the role the concept plays in the end-to-end system and which inputs, state, or resources it changes.

## Why it matters

LoRA affects how an AI system should be selected, configured, tested, or operated. It can influence output quality, resource requirements, reliability, or the amount of control available to the surrounding application.

## Practical uses

- Adapt language or image models to a task, style, character, or domain.
- Share compact reusable adapters for a known base model.

## Example

A diffusion-model LoRA can add a consistent visual style while leaving the original checkpoint unchanged.

## Trade-offs and limitations

- An adapter can behave incorrectly with the wrong base model or architecture revision.
- Low-rank capacity may be insufficient for large behavioral changes.

Do not evaluate this concept in isolation. Test it together with the actual model, data, runtime, tools, and workload that will be used in production or local experiments.

## Practical checklist

- What problem is LoRA expected to solve in this workflow?
- Which inputs, settings, or resources does it depend on?
- How will success and failure be measured?
- What changes when the model, runtime, dataset, or context size changes?

## Related concepts

- [Training and Adaptation](../../)
- [Parameter-Efficient Fine-Tuning](../parameter-efficient-fine-tuning/)
- [QLoRA](../qlora/)
