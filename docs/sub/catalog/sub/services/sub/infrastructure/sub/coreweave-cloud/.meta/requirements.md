# Documentation Requirements

## Requirements

- Present CoreWeave Cloud as CoreWeave's producer-operated AI cloud/infrastructure service, distinct from software projects to which CoreWeave contributes.
- Cover GPU compute and AI-workload infrastructure from current first-party sources, including its Kubernetes-oriented operating model where relevant.
- Treat accelerator inventory, capacity modes, regions, prices, and availability as freshness-sensitive rather than durable catalog facts.
- Keep `llm-d` as a separate software identity; CoreWeave producing/contributing to both does not collapse the service and software nodes.
- Render the standard `entity-relations` block from validated current-entity relations.

## Validation

- The service/software boundary with `llm-d` is explicit.
- Mutable cloud inventory is not frozen as timeless fact.
- Producer provenance resolves to the existing CoreWeave producer node.

## Scoped original-source qualification — 2026-11-06

- CoreWeave's original documentation identifies a managed GPU/AI infrastructure provider offering CoreWeave Kubernetes Service, Slurm-on-Kubernetes, hosted inference, agent sandboxes, compute-oriented networking and associated storage. These provider service modes do not imply that runnable models or projects such as llm-d are trained or owned by CoreWeave.
- Managed Kubernetes clusters, inference options and underlying GPU/node types have independently documented deployment, networking and data policies. No cross-region capacity, performance, availability, cost, isolation or workload compatibility is accepted without a workload- and account-specific current check.
- The provider's dedicated GPU, storage and cloud-native operating model is one canonical infrastructure identity for this scoped research; no separate acceptance is counted for each platform feature.
- Verified first-party source 1: https://docs.coreweave.com/
- Verified first-party source 2: https://www.coreweave.com/products/gpu-compute
- Acceptance scope: present hosted infrastructure identity and publisher-documented feature/version boundaries only. No model/runtime execution, complete freshness, independent security/legal review, rights clearance, root-wide schema/cache/CI/render, clean pass, final-delivery or merge credit.
