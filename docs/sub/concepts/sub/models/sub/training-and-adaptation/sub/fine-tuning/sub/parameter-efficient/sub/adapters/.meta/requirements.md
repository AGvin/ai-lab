# Documentation Requirements

## Requirements

- Use the reader-facing title `Adapters`.
- Define adapters here as parameter-efficient fine-tuning modules added to a pretrained model so compact task/domain-specific parameters can be trained while most or all base-model parameters remain frozen.
- Present bottleneck adapters as the canonical historical example: a small down-projection/nonlinear/up-projection-style module or related compact transformation is inserted at selected points in the network and trained for the target adaptation.
- Do not use `adapter` as a universal synonym for every PEFT artifact. Frameworks may use adapter terminology broadly, but this concept owns added trainable module-style adaptation; LoRA is a separate low-rank reparameterization concept even when libraries package LoRA weights as an `adapter` artifact.
- Explain that adapter placement, architecture, hidden/bottleneck size, activation, residual connection, initialization, sharing, routing, composition, and target layers vary by method; the original Houlsby layout is an important example rather than the only valid adapter architecture.
- Distinguish adapters from prefix/prompt tuning and other PEFT methods that add trainable state at the input/attention context level rather than inserting the same kind of network module.
- Explain that an adapter artifact depends on a compatible base model and insertion/configuration contract. A small adapter file does not contain the frozen base weights and is not independently runnable without the expected base/runtime support unless explicitly merged/materialized.
- Explain that adapters can permit storing many task-specific adaptations against one shared base, but switching/composing adapters and inference overhead depend on the method/runtime. Do not claim all adapters have negligible or identical latency cost.
- Make clear that adapters can still overfit, interfere when composed, alter safety/calibration, or fail outside the target distribution; parameter efficiency does not imply behavioral isolation or guaranteed preservation of all base capabilities.
- Distinguish adapter merging/composition from training. Some adapter forms can be fused, stacked, routed, or composed, but these operations have method-specific semantics and are not universal capabilities of every adapter.
- Keep concrete adapter libraries, configuration files, module placement recipes, hidden sizes, composition syntax, base-model compatibility matrices, benchmarks, and deployment recommendations with their applicable catalog, runtime, evidence, learning, or decision owners.
- Use the canonical entity references as research inputs for additive bottleneck-module adapters and their distinction from other PEFT families when reader-facing rendering is activated.

## Validation

- `Adapters` is not used as the canonical synonym for every PEFT method or artifact.
- LoRA is kept conceptually separate from inserted bottleneck/module adapters despite ecosystem packaging terminology.
- One original adapter placement/shape is not universalized.
- Adapter artifacts are not treated as standalone models without a compatible base/configuration.
- Inference overhead, composition, mergeability, and capability preservation are not generalized across all adapter methods.
- Concrete library/configuration recipes remain outside the abstract concept owner.
