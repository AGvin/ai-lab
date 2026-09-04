# Documentation Requirements

## Requirements

- Use the reader-facing title `QLoRA` and introduce `Quantized Low-Rank Adaptation` as the common expanded name.
- Define QLoRA as a parameter-efficient fine-tuning method/family that trains LoRA updates while keeping the base model frozen in a low-bit quantized representation during training so base-weight memory is reduced while gradients update the LoRA parameters.
- Preserve the original QLoRA method boundary: Dettmers et al. use a frozen 4-bit base, NormalFloat4 (NF4), double quantization of quantization constants, paged optimizers, and LoRA adapters. Present these as components of the original method rather than claiming every ecosystem use of the `QLoRA` label reproduces the complete original recipe.
- Acknowledge current ecosystem usage in which `QLoRA` is often used more broadly for LoRA fine-tuning over a frozen 4-bit quantized base. When documenting a concrete implementation, state the quantization type, compute/dequantization precision, LoRA configuration, optimizer behavior, and whether original QLoRA components are actually used.
- Explain that the frozen base can be stored in 4-bit form while computation for selected operations/dequantization and LoRA updates uses higher precision. `4-bit model` therefore does not mean every arithmetic operation, activation, gradient, or optimizer state is 4-bit.
- Distinguish QLoRA from post-training quantization of a finished model. QLoRA uses quantization as part of the fine-tuning memory strategy; deployment may later keep, change, dequantize, merge, or requantize the resulting base/adapter according to the runtime and artifact contract.
- Distinguish QLoRA from generic LoRA. LoRA itself does not require a quantized base; QLoRA combines low-rank adaptation with frozen low-bit base storage/training mechanics.
- Explain that QLoRA reduces the frozen base-weight memory footprint but still requires memory for LoRA parameters, gradients/optimizer state for trainable parameters, activations, temporary dequantized/compute values, runtime workspaces, batches/context, and framework overhead. A simple `parameter count × 0.5 bytes` calculation is not a complete training-memory model.
- Explain that quantization error can interact with the adaptation task, model architecture, outliers, target modules, rank, compute precision, and calibration/representation scheme. Original-paper quality results do not guarantee parity with full fine-tuning for every model/task/implementation.
- Make clear that QLoRA can enable fine-tuning on smaller hardware than full-precision full-parameter training, but it does not guarantee one-GPU feasibility, fixed VRAM requirements, faster training, or runtime support for every model.
- Explain artifact compatibility: a QLoRA adapter depends on the expected base/model structure and quantization/runtime contract. Merging into a standalone model can require dequantization or specialized merge/requantization handling, and the final deployed representation must be documented separately.
- Keep concrete bitsandbytes/TorchAO settings, NF4 variants, optimizer/page settings, LoRA ranks/targets, base-model recipes, hardware memory figures, benchmark results, merge procedures, and deployment/model-selection recommendations with their applicable catalog, runtime, evidence, learning, or decision owners.
- Use the canonical entity references as research inputs for original QLoRA mechanics and current ecosystem naming boundaries when reader-facing rendering is activated.

## Validation

- QLoRA is not equated with generic LoRA, arbitrary post-training quantization, or every low-bit fine-tuning method.
- The original NF4/double-quantization/paged-optimizer recipe is distinguished from broader ecosystem shorthand usage.
- A `4-bit` frozen base is not described as meaning all training arithmetic/state is 4-bit.
- Base-weight memory reduction is not treated as a complete training-VRAM/compute model.
- Original QLoRA quality/feasibility results are not generalized as universal parity, speed, or one-GPU guarantees.
- QLoRA adapter artifacts are not treated as standalone deployment models without an explicit base/quantization/merge contract.
