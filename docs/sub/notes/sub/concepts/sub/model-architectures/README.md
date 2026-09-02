# Model Architectures

Legacy residual retained for architecture-reading pedagogy, model-selection interpretation, and temporary legacy child navigation because the selected architectures-and-representations learning owner is not yet materialized on the active branch.

> **Migration note:** The reusable Model Architectures core is already preserved in `docs/sub/concepts/sub/models/sub/architectures/`: architecture describes computational components/connections/activation paths, stays distinct from model scale, training/adaptation, deployment, access/licensing, frontier status, numerical precision, and practical hardware fit, and can affect execution without guaranteeing one performance outcome. The selected `learning/areas/models/architectures-and-representations/` owner is currently absent on the active AI Lab ref. Preserve only the practical interpretation and temporary navigation below until learning/navigation owners are ready.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Architecture-reading pedagogy residual

Keep architecture fields separate from other model properties when comparing concrete models:

- dense does not mean small, and sparse does not mean large;
- MoE does not automatically mean faster, cheaper, locally practical, or frontier;
- quantization changes numerical representation rather than the model's dense/sparse activation architecture;
- pruning can introduce sparsity but is not equivalent to every sparse-activation architecture;
- total parameter count, active parameter count, memory residency, and compute per token are distinct measurements when they affect workload fit.

When a concrete model is MoE, record reliable **total** and **active** parameter counts separately. Comparing an MoE and a dense model using only one of those counts can produce a misleading size/compute conclusion.

Architecture can be a useful explanatory field for hardware fit, inference behavior, throughput, memory/communication patterns, or runtime compatibility, but concrete task-fit conclusions remain model-selection/evidence-owned rather than architecture truth.

## Temporary legacy child navigation

- [`dense-and-sparse-architectures/`](./sub/dense-and-sparse-architectures/)
- [`mixture-of-experts/`](./sub/mixture-of-experts/)

These pedagogical/navigation fragments remain migration source material until the selected architectures-and-representations learning owner and later legacy-navigation/source-removal gates are ready.
