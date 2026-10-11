# Documentation Requirements

## Requirements

- Identify MLPerf Training as MLCommons' open, peer-reviewed, versioned benchmark suite for measuring how quickly complete systems train machine-learning models to defined quality targets.
- Preserve MLPerf Training v6.0 as the current published results revision only while supported by current MLCommons material; treat benchmark inventory, datasets, reference implementations, target-quality metrics, rules, submission classes, power measurements, and results as version-sensitive.
- Preserve the current suite boundary across large-language-model pretraining and fine-tuning, recommendation, and image-generation workloads without promoting every version-scoped benchmark workload to an independent canonical identity by default.
- Keep individual training models and datasets, vendor submissions, accelerators, host processors, frameworks, cloud platforms, and optimization recipes separate from the benchmark-suite identity.
- Preserve MLCommons producer provenance through the canonical relation.
- Attribute performance records to the exact submitted system, benchmark revision, workload, target quality, and configuration rather than generalizing them into universal training-system rankings.

## Validation

- The node remains the durable MLPerf Training benchmark-suite identity rather than one release, reference model, dataset, or results table.
- Version-specific workload changes are not generalized across all MLPerf Training revisions.
- MLCommons provenance resolves bidirectionally.
- Results remain scoped to the exact benchmark version and submitted system.
