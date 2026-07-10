# QLoRA

<!--
ai_content:
  managed: true
  l10n: true
-->

QLoRA adapts a model with LoRA while keeping the frozen base model in a low-bit quantized representation during training.

## Core idea

The base weights are loaded in a memory-efficient quantized form, while LoRA parameters and selected computations use higher precision. This substantially lowers memory requirements compared with full-precision fine-tuning and can make large-model adaptation possible on a single high-memory GPU.

## Practical use

- Fine-tune models that would not fit in full training precision.
- Create domain or instruction adapters on constrained hardware.
- Compare several task adapters against one frozen base model.

## Important considerations

Training quantization is not identical to distributing a quantized inference file. The resulting LoRA adapter must still be applied to a compatible base model, and the deployed model may be quantized separately. Dataset quality and evaluation remain more important than the memory-saving method.

## Trade-offs and limitations

QLoRA reduces memory but not all compute cost. Training may be slower due to quantization and dequantization overhead. Very aggressive settings, poor learning rates, or incompatible kernels can produce unstable results.

## Common mistakes

- Treating QLoRA as a standalone model format.
- Applying the adapter to a different base checkpoint.
- Assuming low memory requirements eliminate data-quality needs.
- Evaluating only training loss.

## Related concepts

- [Training and Adaptation](../../)
- [LoRA](../lora/)
- [Quantization](../../../inference-and-serving/sub/quantization/)
- [Fine-Tuning](../fine-tuning/)
