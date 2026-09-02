# Pretraining

Legacy residual retained for training-program readiness, checkpoint/recovery operations, staged evaluation, reproducibility, and compute/data governance guidance that are intentionally outside the canonical Pretraining concept owner.

> **Migration note:** Pretraining identity, lifecycle-role versus scale boundaries, objective/modality variability, continued-pretraining distinction, inference-time mechanism separation, downstream-stage relationships, data-quality/provenance risks, cutoff limits, and design-dimension variability are already preserved in `docs/sub/concepts/sub/models/sub/training-and-adaptation/sub/pretraining/`. The remaining material below stays here until its exact learning, training-engineering, infrastructure, evaluation, governance, or project-operations owner is verified.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Program-readiness residual

Before a long training run, verify the exact data mixture/version, tokenizer or processor, architecture/configuration, objective, optimizer/schedule, precision strategy, distributed topology, checkpoint format, storage capacity, monitoring, and recovery path. Small mismatches discovered late can invalidate expensive compute rather than merely reduce convenience.

Estimate data-loading throughput, checkpoint I/O, network/collective performance, optimizer/model state memory, activation/workspace memory, and expected wall-clock/runtime cost on the actual cluster instead of extrapolating only from parameter count or accelerator peak throughput.

## Checkpoint and recovery residual

Define checkpoint cadence according to restart cost, storage overhead, and failure frequency. Preserve enough state to reproduce or safely resume the run, including model/optimizer/scheduler state, step/sample progress, RNG state where required, dataset/shuffle/version identity, configuration, and code/container/runtime versions.

Test restore/resume before the expensive stage rather than discovering that a nominal checkpoint cannot reconstruct the training state after a node or job failure.

## Staged-evaluation residual

Evaluate during training at meaningful checkpoints for optimization stability, capability trends, contamination/leakage indicators, safety or bias regressions, and data-quality failures. Keep a sufficiently independent acceptance boundary so repeatedly observed benchmark results do not become an uncontrolled training/selection target.

Compare scaling or curriculum changes against matched baselines and record compute/data differences explicitly; more tokens or compute should not be treated as the explanation for quality changes when the data mixture, objective, implementation, or evaluation also changed.

## Governance and reproducibility residual

Record training-data lineage and applicable rights/restrictions, run ownership, compute budget, artifact destinations, incident/restart history, and the exact checkpoint promoted downstream. Keep training logs and model artifacts connected strongly enough that later fine-tuning or evaluation results can be traced to the correct pretrained state.

These program-readiness, recovery, evaluation, reproducibility, and governance practices remain migration source material until their exact learning, training-engineering, infrastructure, evaluation, governance, or project-operations owners are verified.
