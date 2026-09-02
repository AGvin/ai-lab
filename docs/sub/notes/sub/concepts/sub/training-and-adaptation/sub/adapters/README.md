# Adapters

Legacy residual retained for adapter-fleet versioning, runtime switching/composition, compatibility validation, rollback, evaluation, and licensing guidance that are intentionally outside the canonical Adapters concept owner.

> **Migration note:** Adapter identity, bottleneck/module-family semantics, PEFT/LoRA/prefix distinctions, placement/configuration variability, base-coupled artifact identity, runtime overhead/composition limits, and behavioral-regression risks are already preserved in `docs/sub/concepts/sub/models/sub/training-and-adaptation/sub/fine-tuning/sub/parameter-efficient/sub/adapters/`. The remaining material below stays here until its exact learning, training-engineering, runtime, evaluation, artifact-management, or decision-support owner is verified.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Adapter-fleet residual

When one base model supports several adapters, version the base and every adapter as one compatibility matrix rather than as independent files. Record the insertion/configuration contract, processor/tokenizer assumptions, runtime/library support, and evaluation evidence needed to activate each variant safely.

Do not infer compatibility from matching dimensions or similar model-family names. Revalidate adapters after base-revision, architecture/module, runtime, processor, or quantization changes.

## Runtime and composition residual

Measure load/switch latency, memory overhead, inference throughput, batching/cache behavior, and concurrency on the intended serving path. Runtime support for hot switching, stacking, fusion, routing, or merging is method- and implementation-specific.

Test multi-adapter composition explicitly. Individually useful adapters can interfere, override one another, amplify undesirable behavior, or create performance regressions when stacked or fused.

## Rollback and evaluation residual

Keep the unchanged base and known-good adapter versions available for rollback. Evaluate each adapter against the base and against other production variants on both its target behavior and capabilities that must remain stable.

If adapter routing is dynamic, verify the routing decision separately from the adapter's own quality so incorrect selection is not misdiagnosed as adaptation failure.

## Licensing and distribution residual

Publish or distribute the required base identity, compatible runtime/configuration assumptions, artifact license, and any material base-model or dataset obligations together with the adapter. A small adaptation artifact does not become legally or operationally independent from its required base.

These fleet, runtime, composition, rollback, evaluation, and licensing practices remain migration source material until their exact learning, training-engineering, runtime, evaluation, artifact-management, or decision-support owners are verified.
