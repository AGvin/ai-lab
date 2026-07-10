# Parameter-Efficient Fine-Tuning

Adaptation methods that train only a small subset of model parameters or added components.

## Core idea

Adaptation methods that train only a small subset of model parameters or added components. In practical AI work, the term is useful because it names a specific part of the system rather than treating the model as a single opaque component. Understanding where it appears in the workflow makes configuration choices and failure analysis more precise.

## How it works

- PEFT methods train a small parameter subset or added modules while freezing most base weights.
- Adapters, LoRA, prompt tuning, and related methods reduce optimizer state and storage requirements.
- The resulting artifact is normally used together with the exact compatible base model.

The exact implementation varies by model family, provider, and runtime. The important distinction is the role the concept plays in the end-to-end system and which inputs, state, or resources it changes.

## Why it matters

Parameter-Efficient Fine-Tuning affects how an AI system should be selected, configured, tested, or operated. It can influence output quality, resource requirements, reliability, or the amount of control available to the surrounding application.

## Practical uses

- Adapt large models with limited training hardware.
- Maintain several task-specific variants without storing full model copies.

## Example

A project trains a 100 MB adapter instead of publishing another multi-gigabyte copy of the base model.

## Trade-offs and limitations

- Compatibility depends on architecture, layer names, tokenizer, and runtime.
- Parameter efficiency does not guarantee data efficiency or good generalization.

Do not evaluate this concept in isolation. Test it together with the actual model, data, runtime, tools, and workload that will be used in production or local experiments.

## Practical checklist

- What problem is Parameter-Efficient Fine-Tuning expected to solve in this workflow?
- Which inputs, settings, or resources does it depend on?
- How will success and failure be measured?
- What changes when the model, runtime, dataset, or context size changes?

## Related concepts

- [Training and Adaptation](../../)
- [Fine-Tuning](../fine-tuning/)
- [LoRA](../lora/)
