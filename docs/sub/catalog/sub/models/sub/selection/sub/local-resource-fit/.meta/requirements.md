# Documentation Requirements

## Requirements

- Treat local resource fit as a cross-cutting model-selection lens, not as a standalone task category or a proxy for model quality.
- Start from an exact model, version, artifact, or materially distinct quantization and evaluate whether it is a credible candidate under a stated local memory constraint.
- Link intrinsic model and artifact facts from `../../../reference/` instead of duplicating canonical model profiles or maintaining a second source of artifact identity.
- Preserve useful artifact-specific fit judgments from the legacy `local-models-by-vram` guide when their evidence boundary remains clear and their canonical model identity is available.
- Treat Z-Image-Turbo as a current validation candidate for a 16-GB-class local image-generation route because Tongyi-MAI currently claims comfortable operation within 16 GB consumer VRAM; keep the fit state `Unknown` until the exact checkpoint, runtime, precision, resolution, batch, offload policy, auxiliary components, and measured peak memory are pinned and tested.
- Do not infer a practical local Kimi K3 route from open-weight availability or the 104B activated-parameter figure. Its 2.8T total scale and exact distributed artifacts/runtime requirements must be evaluated directly before any local-fit label is assigned.
- Distinguish published artifact or weight size from measured peak runtime VRAM. Include required auxiliary files such as multimodal projectors when they materially affect the evaluated route.
- Bind material local-fit conclusions to the relevant runtime, quantization or precision, context, batch/concurrency, auxiliary-file, offload, and measured-memory conditions when those conditions affect the conclusion.
- Treat a successful model load as insufficient evidence of useful context headroom, target latency, concurrency, or accepted task quality.
- Use bounded planning labels only when their meaning is explicit. Mark unmeasured model/resource combinations as `Unknown` rather than inferring fit from nominal file size or available VRAM.
- Do not infer multi-GPU fit by summing device memory without evidence for the actual serving strategy.
- Keep GPU purchasing, concrete GPU inventories, VRAM capacity-class design, sharding topology, runtime selection, resident-service scheduling, host-memory architecture, and broader deployment design outside this subtree.
- Allow hardware/runtime details here only as frozen evidence conditions for a model-selection conclusion, not as recommendations about infrastructure design.
- Keep task quality and recommendation state on the applicable task-selection page; local fit establishes an operating constraint, not a universal model rank.
- Preserve mixed legacy material that belongs outside model selection until its separate canonical owner is migrated; do not delete the legacy source page while doing so would discard out-of-scope hardware or deployment guidance.

## Validation

- The page answers whether an exact local model artifact is a credible candidate under a stated resource constraint.
- Canonical model identity and artifact facts remain owned by Model Reference.
- Published artifact size is not presented as measured peak VRAM.
- Z-Image-Turbo's provider 16 GB claim remains a validation hypothesis rather than a confirmed AI Lab fit result until measured under pinned runtime conditions.
- Kimi K3's active-parameter count is not treated as memory-residency or practical self-hosting evidence.
- No GPU buying guide, hardware catalog, capacity-class taxonomy, sharding design, runtime architecture, or service-residency plan is migrated into this node.
- Unmeasured combinations are not promoted to confident fit labels.
- The legacy mixed page is not removed until all still-valid non-model residual content has another verified owner or an explicitly approved disposition.
