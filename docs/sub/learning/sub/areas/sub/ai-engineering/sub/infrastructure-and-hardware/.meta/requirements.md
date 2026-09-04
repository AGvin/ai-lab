# Documentation Requirements

## Requirements

- Present Infrastructure and Hardware as the AI Engineering learning group for system-level compute, accelerator, memory/storage, networking, node/cluster topology, and cloud/rented capacity required to run AI workloads.
- Keep intrinsic model execution/training mechanics with Models and concrete hardware/provider identities/specifications with Catalog; this group teaches infrastructure reasoning, topology, lifecycle, and operational consequences.
- Explain that the current materialized subset focuses on `cloud-and-rented-capacity/` because resource-lifecycle legacy material has source-backed teaching about ephemeral/billable compute and control-plane lifecycle ready for migration.
- Do not imply that unmaterialized selected siblings `compute-and-accelerators/`, `memory-and-storage/`, `networking/`, `single-node-systems/`, or `multi-node-systems/` are absent from the logical architecture; standard navigation reflects only physical children.
- Teach infrastructure decisions through workload requirements, capacity, locality/data policy, availability/failure domains, lifecycle, cost exposure, observability, and recovery rather than by naming one preferred provider or instance class.
- Distinguish resource identity/lifecycle from workload readiness. A provisioned host/endpoint/process can be alive while the intended model/artifact/runtime/data path remains unavailable or incorrect.
- Keep provider-specific states, prices, quotas, APIs, SKUs, regions, hardware support matrices, and dated performance results source-backed with catalog/evidence/project owners.

## Validation

- Infrastructure learning remains system-level and does not duplicate model-internal mechanics or hardware catalog facts.
- Resource existence/liveness is not treated as proof of workload readiness.
- Current navigation exposes only materialized selected children.
- Mutable provider facts remain evidence/catalog-owned.
