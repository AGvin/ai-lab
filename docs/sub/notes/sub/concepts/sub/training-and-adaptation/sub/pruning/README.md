# Pruning

Legacy residual retained for pruning-experiment design, recovery/retraining workflow, runtime/hardware compatibility, realized deployment benchmarking, and regression/rollback guidance that are intentionally outside the canonical Model Pruning concept owner.

> **Migration note:** Pruning identity, structured-versus-unstructured semantics, one-shot/iterative and training-stage variability, pruning-criterion families, logical sparsity versus physical execution, sparse-activation/MoE separation, quantization/distillation distinctions, optional retraining, nominal-versus-realized acceleration boundaries, and capability-regression risks are already preserved in `docs/sub/concepts/sub/models/sub/optimization-and-compression/sub/pruning/`. The remaining material below stays here until its exact learning, optimization-engineering, runtime, evaluation, artifact-management, or decision-support owner is verified.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Experiment-design residual

Establish an unchanged-model baseline and define the target deployment constraint before selecting a pruning ratio, pattern, criterion, target components, or schedule. Record the exact source model/checkpoint, pruning configuration, masks or structurally removed units, retraining configuration, and resulting artifact identity needed to reproduce the experiment.

Compare several pruning levels when the acceptable quality/resource frontier is not known rather than committing immediately to one aggressive target. Preserve intermediate checkpoints when they can reduce recovery cost or help isolate where capability loss begins.

## Recovery and retraining residual

Evaluate the model immediately after pruning and again after any recovery fine-tuning so the effect of structural removal remains distinguishable from the effect of retraining. Use data and objectives appropriate to the retained capabilities rather than optimizing only the narrow metric used to choose what to prune.

Keep a known-good pre-pruning artifact and rollback path. If the recovered artifact still fails accepted target or regression criteria, prefer a less aggressive pruning level or another optimization route rather than hiding the degradation behind additional tuning.

## Runtime and deployment residual

Verify that the concrete runtime, compiler, sparse kernel, accelerator, or structurally compacted representation can exploit the exact sparsity pattern produced. Measure serialized size, resident memory, latency, throughput, batch behavior, energy/power where relevant, and end-to-end application cost on the target system.

Do not report zero weights, nominal sparsity, or theoretical FLOP reduction as realized acceleration unless the deployed execution path demonstrates the gain. Structured or hardware-supported semi-structured patterns can outperform more flexible sparsity when the runtime cannot exploit arbitrary masks.

## Regression evaluation residual

Evaluate target quality together with long-tail capabilities, calibration, robustness, safety behavior, future fine-tuning headroom, and other retained properties that matter to deployment. Compare against an existing smaller model, quantized model, distilled student, or unpruned baseline when those alternatives could satisfy the same operational goal at lower total cost.

These experiment, recovery, runtime, deployment, regression, and rollback practices remain migration source material until their exact learning, optimization-engineering, runtime, evaluation, artifact-management, or decision-support owners are verified.
