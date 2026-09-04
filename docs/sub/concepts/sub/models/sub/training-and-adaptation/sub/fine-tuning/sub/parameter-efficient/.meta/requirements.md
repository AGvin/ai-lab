# Documentation Requirements

## Requirements

- Use the reader-facing title `Parameter-Efficient Fine-Tuning (PEFT)`.
- Define PEFT as a family of fine-tuning/adaptation methods that modify model behavior while training materially fewer parameters than full-parameter fine-tuning, commonly by freezing most or all base-model weights and training selected existing parameters, added modules, low-rank/reparameterized updates, soft/prefix prompt parameters, scale/shift terms, or related compact adaptation state.
- Do not define PEFT as synonymous with adapters or LoRA. Adapters are one additive-module family; LoRA is a low-rank reparameterization method; other PEFT strategies can update selected existing parameters or introduce different compact trainable structures.
- Distinguish trainable-parameter efficiency from complete training-resource efficiency. Fewer trainable parameters can reduce optimizer state, gradient storage, checkpoint size, and some training memory/communication, but activations, frozen weights, forward/backward computation, sequence length, batch size, precision, and runtime kernels can still dominate memory or time.
- Make clear that PEFT does not guarantee faster training, faster inference, lower total cost, or equal quality relative to full fine-tuning. Benefits depend on the method, model, target modules, task, hardware/runtime, and evaluation conditions.
- Explain that PEFT artifacts usually remain coupled to a compatible base model/checkpoint and adaptation contract. Base revision, architecture/module names, tokenizer/processor, target layers, adapter configuration, and runtime support can affect compatibility.
- Distinguish PEFT artifacts from complete model checkpoints and from model/container formats. A small adapter file is learned delta/adaptation state, not an independent model unless it is explicitly merged/materialized into a standalone derivative.
- Explain that some PEFT methods can be merged algebraically or structurally into base weights for deployment while others require active modules/prefixes or runtime support; mergeability is method-specific rather than a universal PEFT property.
- Distinguish PEFT from quantization. Quantization changes numerical representation; PEFT changes which learned parameters/updates are trained. QLoRA combines both concerns but does not make quantization intrinsic to PEFT.
- Explain that parameter-efficient adaptation can still overfit, regress capabilities, memorize training data, alter safety/calibration, or interact poorly with other adapters; reduced trainable parameter count is not a quality or safety guarantee.
- Keep `adapters/`, `lora/`, and `qlora/` as selected descendants. Do not materialize `ia3/` or another PEFT child merely because it exists in the logical architecture when no active legacy source/content package authorizes it.
- Keep concrete PEFT libraries, adapter formats, base-model compatibility matrices, rank/module recipes, training hyperparameters, benchmark results, and deployment/model-selection recommendations with their applicable catalog, runtime, evidence, learning, or decision owners.
- Use the canonical entity references as research inputs for PEFT taxonomy and low-rank/adaptation boundaries when reader-facing rendering is activated.

## Validation

- PEFT is not equated with adapters, LoRA, QLoRA, quantization, or prompt engineering alone.
- Trainable-parameter count is not presented as a complete training-memory, runtime, or cost model.
- Small adapter artifacts are not treated as independent models without a compatible base/merge contract.
- Mergeability and inference overhead are not generalized across all PEFT methods.
- Reduced trainable parameters are not presented as proof of equal quality, safety, or generalization.
- `ia3/` or any other unactivated selected descendant is not materialized by this legacy package.
