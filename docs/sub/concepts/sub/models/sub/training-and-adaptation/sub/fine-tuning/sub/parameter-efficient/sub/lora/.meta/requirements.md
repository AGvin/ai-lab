# Documentation Requirements

## Requirements

- Use the reader-facing title `Low-Rank Adaptation (LoRA)`.
- Define LoRA as a parameter-efficient fine-tuning method that freezes a pretrained weight matrix and learns a low-rank update represented through two smaller trainable factor matrices whose product is added to the base weight's effective transformation.
- Explain the low-rank hypothesis operationally: the adaptation update is constrained to rank `r` (or another method-specific low-dimensional factorization), so the number of trainable parameters can be much smaller than updating the complete base matrix.
- Distinguish LoRA from bottleneck/module adapters. LoRA reparameterizes selected weight updates through low-rank factors rather than necessarily inserting a separate nonlinear bottleneck module in the forward path, even though libraries may package LoRA weights under a generic `adapter` interface.
- Explain that target modules/matrices are an implementation and model-family choice. Attention projections are common targets, but feed-forward, convolutional, embedding, or other compatible linear transformations can also be adapted; one fixed target-module list is not part of the definition.
- Explain rank, scaling, initialization, dropout/regularization, target selection, and trainable bias choices as method/configuration dimensions rather than universal defaults. A larger rank increases adaptation capacity/parameters but does not guarantee better quality.
- Distinguish the LoRA adapter/delta artifact from the base model. It depends on a compatible base checkpoint and target-module mapping and cannot be interpreted as a complete standalone model without that relationship or an explicit merge/materialization.
- Explain merge semantics: for compatible linear LoRA updates, the learned low-rank delta can often be added into the base weights for deployment, eliminating the separate LoRA branch during inference; dynamic/unmerged adapters, quantized bases, composition, and specialized variants can have different merge/support behavior.
- Make clear that LoRA reduces trainable parameters and optimizer/gradient state associated with the frozen weights but does not eliminate the need to execute the frozen model's forward/backward path or store activations required for training. Trainable-parameter reduction is not identical to total memory/compute reduction.
- Distinguish LoRA from quantization. LoRA is a low-rank adaptation method; quantization changes numerical representation. LoRA can be trained/applied with full- or reduced-precision bases, while QLoRA is a specific selected combination/family using a quantized frozen base during LoRA training.
- Explain that LoRA can change target-task behavior while also causing regressions, memorization, safety/calibration changes, or interference when several adapters are composed/merged; low-rank structure is not a behavioral-isolation guarantee.
- Keep concrete LoRA ranks, alpha/scaling conventions, target-module recipes, adapter formats, merge commands, base-model compatibility, training hyperparameters, variant algorithms, benchmark results, and deployment/model-selection recommendations with their applicable catalog, runtime, evidence, learning, or decision owners.
- Use the canonical entity references as research inputs for low-rank update semantics and implementation/merge boundaries when reader-facing rendering is activated.

## Validation

- LoRA is not equated with every adapter/PEFT method or with bottleneck adapter modules.
- One target-module set, rank, scaling formula/default, or dropout setting is not universalized.
- A LoRA artifact is not presented as a standalone model without its base/mapping contract or explicit merge.
- Reduced trainable parameter count is not treated as equal to total training-memory/compute reduction.
- LoRA is distinguished from quantization and from QLoRA's quantized-base training method.
- Mergeability is scoped to compatible method/runtime/base conditions rather than asserted for every LoRA variant/artifact.
