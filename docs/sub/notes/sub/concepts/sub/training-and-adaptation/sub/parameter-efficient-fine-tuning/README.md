# Parameter-Efficient Fine-Tuning

Parameter-Efficient Fine-Tuning, or PEFT, adapts a model by training a small subset of parameters or additional modules while keeping most base weights frozen.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Core idea

Full fine-tuning stores gradients and optimizer state for the entire model. PEFT reduces training memory and produces smaller adaptation artifacts. Methods include LoRA, adapters, prefix tuning, prompt tuning, and selective parameter updates.

## Practical use

- Adapt large models on limited hardware.
- Maintain several task-specific adapters for one base model.
- Distribute small adaptation files instead of complete checkpoints.
- Experiment with domain or style changes at lower cost.

## Trade-offs and limitations

PEFT can approach full fine-tuning quality for many tasks but is not universally equivalent. The adapter depends on a specific base model and often a specific architecture or module naming scheme. Serving several adapters may add runtime complexity.

## Common mistakes

- Loading an adapter on the wrong base-model revision.
- Assuming a small trainable parameter count prevents overfitting.
- Comparing methods without matching data and evaluation.
- Forgetting that adapter and base-model licenses both matter.

## Related concepts

- [Training and Adaptation](../../)
- [LoRA](../lora/)
- [QLoRA](../qlora/)
- [Adapters](../adapters/)
