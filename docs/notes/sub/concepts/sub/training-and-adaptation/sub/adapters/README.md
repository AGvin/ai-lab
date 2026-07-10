# Adapters

Adapters are small trainable components attached to a frozen or mostly frozen base model to provide reusable specialization.

## Core idea

An adapter inserts additional parameters into selected model layers or modifies their computation. Different adapters can be loaded for different tasks without storing a complete model copy. LoRA is one widely used adapter-style technique, but adapter methods can use other architectures.

## Practical use

- Maintain task-specific model variants.
- Switch domain behavior at runtime.
- Distribute small adaptation artifacts.
- Combine a stable base model with tenant or product specialization.

## Trade-offs and limitations

Adapters remain coupled to the base-model architecture and revision. Runtime support for loading, merging, stacking, or switching adapters varies. Combining several adapters may produce interference rather than additive capabilities.

## Common mistakes

- Treating adapters as independent of the base model.
- Loading incompatible module names or dimensions.
- Stacking adapters without evaluating interactions.
- Publishing an adapter without documenting required base weights and license.

## Related concepts

- [Training and Adaptation](../../)
- [Parameter-Efficient Fine-Tuning](../parameter-efficient-fine-tuning/)
- [LoRA](../lora/)
- [Model Formats](../../../inference-and-serving/sub/model-formats/)
