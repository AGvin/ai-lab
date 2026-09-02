# Parameter-Efficient Fine-Tuning

Legacy residual retained for base/artifact compatibility, resource measurement, multi-adapter serving, evaluation, and licensing workflow guidance that are intentionally outside the canonical Parameter-Efficient Fine-Tuning concept owner.

> **Migration note:** PEFT identity, method-family boundaries, trainable-parameter versus total-resource efficiency, base-coupled artifact semantics, mergeability limits, quantization separation, and quality/safety non-guarantees are already preserved in `docs/sub/concepts/sub/models/sub/training-and-adaptation/sub/fine-tuning/sub/parameter-efficient/`. The remaining material below stays here until its exact learning, training-engineering, runtime, evaluation, artifact-management, or decision-support owner is verified.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Compatibility residual

Pin the exact compatible base model/checkpoint, architecture/module mapping, tokenizer or processor, adapter configuration, and runtime/library contract needed to load an adaptation artifact. Do not infer compatibility from a similar model name or family label.

When a base revision, target-module naming, processor, quantization path, or serving runtime changes, revalidate the adapter instead of assuming the compact artifact remains portable unchanged.

## Resource and evaluation residual

Measure actual peak memory, training time, throughput, checkpoint size, communication overhead, and accepted-result quality on the intended hardware/runtime. A small trainable-parameter count can reduce optimizer and gradient state while activations, frozen weights, sequence length, and backward computation still dominate cost.

Compare PEFT and full fine-tuning under matched data and evaluation conditions when the choice matters. Reduced parameter count does not by itself establish equivalent task quality or lower total cost.

## Multi-adapter serving residual

If several task-specific adapters share one base model, define version/compatibility rules, activation and switching behavior, concurrency limits, cache implications, and rollback. Test adapter composition explicitly when multiple adaptations can be active together; do not assume independently trained adapters combine cleanly.

Choose separate versus merged deployment according to the method/runtime contract and operational needs. Merging can simplify some serving paths while reducing independent switching or complicating provenance of the resulting derivative artifact.

## Licensing residual

Track both base-model and adaptation-artifact licenses and any dataset or distribution constraints that materially affect use or redistribution. A compact adapter does not erase obligations attached to the compatible base or training inputs.

These compatibility, resource, serving, evaluation, and licensing practices remain migration source material until their exact learning, training-engineering, runtime, evaluation, artifact-management, or decision-support owners are verified.
