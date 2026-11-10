# Documentation Requirements

## Requirements

- Present Lambda Cloud as Lambda's externally operated accelerated-compute service rather than as an inference API or an installable runtime.
- Document current self-service GPU instance and cluster capability from first-party Lambda documentation without freezing mutable prices or availability as durable facts.
- Distinguish GPU infrastructure capacity from managed model inference: users provision compute and remain responsible for the workloads and model-serving stack they run on it.
- Treat exact accelerator inventory, regions, instance shapes, capacity, and prices as freshness-sensitive claims that require current verification.
- Keep Lambda-branded physical systems and workstations outside this service identity.
- Render the standard `entity-relations` block from validated current-entity relations.

## Validation

- The page explains why Lambda Cloud belongs under hosted infrastructure.
- Mutable capacity/pricing is not presented as timeless.
- Producer provenance resolves to Lambda, Inc.

## Scoped original-source qualification — 2026-11-06

- Lambda's public cloud provides both on-demand Linux GPU virtual machines and 1-Click Clusters; the cluster product's high-speed internal GPU fabric and management/head nodes are distinct from a single on-demand instance and from Lambda hardware sold for local ownership.
- GPU compute capacity is not a fully managed model API. Users remain responsible for training/inference software, SSH credentials, workload isolation, model provenance and their own data lifecycle. Exact GPU families, cluster sizes, network paths, regions, price and availability are first-party, dated, plan-specific facts rather than transferable performance guarantees.
- Verified first-party source 1: https://docs.lambda.ai/public-cloud/
- Verified first-party source 2: https://docs.lambda.ai/public-cloud/1-click-clusters/
- Acceptance scope: present provider documentation of the existing service identity and deployment-specific conditions only; not new metadata, reader repair, independent hardware execution, complete freshness/legal/security audit, root-wide schema/cache/CI/render, clean pass, final-delivery gate or merge.
