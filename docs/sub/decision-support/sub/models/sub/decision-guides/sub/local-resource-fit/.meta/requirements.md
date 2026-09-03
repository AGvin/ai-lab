# Documentation Requirements

## Requirements

- Treat local resource fit as a **model-first** cross-cutting selection lens: start from an exact model/version/artifact and ask whether it is credible under stated local resources.
- Keep the sibling `../../hardware/` journey as the inverse **device-first** route: when the reader starts from owned/fixed hardware and asks which models are practical, link that owner rather than duplicating its ecosystem taxonomy here.
- Link intrinsic model/artifact facts from `../../../../../reference/` instead of duplicating canonical profiles.
- Preserve useful artifact-specific fit judgments from the legacy `local-models-by-vram` guide when evidence boundaries remain clear and canonical model identity is available.
- Treat Z-Image-Turbo as a validation candidate for a 16-GB-class local image-generation route because Tongyi-MAI currently documents a 16 GB consumer-VRAM target; keep fit `Unknown` until exact checkpoint, runtime, precision, resolution, batch, offload, auxiliary components, and measured peak memory are pinned/tested.
- Do not infer a practical local Kimi K3 route from open-weight availability or activated-parameter figures; evaluate exact distributed artifacts/runtime directly.
- Distinguish published artifact/weight size from measured peak runtime memory and include required auxiliary files/projectors when material.
- Bind material fit conclusions to runtime, quantization/precision, context, batch/concurrency, auxiliary files, offload, and measured-memory conditions.
- Treat successful model loading as insufficient evidence of useful context headroom, target latency, concurrency, sustained behavior, or accepted task quality.
- Use bounded planning labels only when explicit; mark unmeasured combinations `Unknown` rather than inferring fit from nominal file size or memory.
- Do not infer multi-GPU fit by summing device memory without evidence for the actual serving/sharding strategy.
- Keep hardware purchasing, concrete hardware inventories, capacity-class buying guidance, sharding architecture, runtime product selection, resident-service scheduling, and broader deployment design outside this node.
- Allow hardware/runtime details only as frozen evidence conditions for a model-selection conclusion.
- Keep task quality/recommendation state on the applicable task-selection page; local fit establishes an operating constraint, not a universal model rank.

## Validation

- The page answers whether an exact model artifact is credible under stated resources; `hardware/` answers which models are credible for a fixed device.
- Canonical identity/artifact facts remain in Model Reference.
- Published artifact size is not presented as measured peak memory.
- Unmeasured combinations are not promoted to confident fit labels.
- No hardware buying guide, hardware catalog, sharding design, runtime architecture, or service-residency plan is migrated into this node.
