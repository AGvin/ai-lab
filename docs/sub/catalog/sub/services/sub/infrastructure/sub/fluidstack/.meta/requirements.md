# Documentation Requirements

## Requirements

- Present Fluidstack as a producer-operated AI cloud focused on large-scale GPU infrastructure for AI training and inference.
- Cover managed bare-metal Kubernetes and managed Slurm as current orchestration surfaces where supported by first-party documentation.
- Keep Fluidstack distinct from commodity self-service GPU marketplaces when describing its large-scale managed-cluster product boundary.
- Treat accelerator inventory, cluster scale, locations, commercial availability, networking specifications, prices, and operational limits as freshness-sensitive.
- Do not split managed Kubernetes and managed Slurm into separate service identities solely because they expose different orchestration interfaces.
- Render the standard `entity-relations` block from validated current-entity relations.

## Validation

- Classification remains hosted infrastructure.
- Mutable capacity and hardware claims are source-backed and time-scoped.
- Producer provenance resolves to FLUIDSTACK LTD.

## Scoped original-source qualification — 2026-11-06

- Fluidstack describes a managed large-scale AI cloud with distinct managed bare-metal Kubernetes and managed Slurm orchestration surfaces. The official documentation names GPU/Network Operator support and cluster health/observability for Kubernetes, plus Slurm scheduling, Pyxis/Enroot, user administration and health checks for Slurm.
- Kubernetes and Slurm are different managed workload/orchestration modes of the same provider-operated GPU infrastructure service, not guaranteed independent catalog products or interchangeable APIs. Fleet scale, topology, regions, accelerator mix, isolation, operational SLAs, pricing, security and commercial access must be checked for the actual contract.
- Verified first-party source 1: https://docs.fluidstack.io/
- Verified first-party source 2: https://fluidstack.io/
- Acceptance scope: present provider documentation of the existing service identity and deployment-specific conditions only; not new metadata, reader repair, independent hardware execution, complete freshness/legal/security audit, root-wide schema/cache/CI/render, clean pass, final-delivery gate or merge.
