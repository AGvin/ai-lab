# Documentation Requirements

## Requirements

- Present NVIDIA Brev as NVIDIA's producer-operated GPU development platform that provisions preconfigured GPU virtual machines across multiple cloud providers.
- Explain the multi-provider abstraction: Brev manages discovery, provisioning, configured AI/ML environments, access, and lifecycle while underlying capacity may come from different providers.
- Cover GPU Instances, Environments, Launchables, CLI/web-console access, and Brev Connect only as product surfaces of the canonical Brev service unless a surface develops an independently durable product identity.
- Keep the distinction between Brev-managed cloud instance lifecycle and Brev Connect, where user-owned hardware remains user-managed and Brev provides management/connectivity surfaces.
- Treat provider inventory, GPU types, prices, regions, capacity, and preinstalled version details as freshness-sensitive.
- Render the standard `entity-relations` block from validated current-entity relations.

## Validation

- NVIDIA Brev is not misrepresented as the owner of every underlying cloud provider or physical GPU host.
- Brev CLI is treated as an access surface rather than a duplicate service identity.
- Producer provenance resolves to NVIDIA.

## Scoped original-source qualification — 2026-11-06

- NVIDIA Brev provisions preconfigured GPU development VMs across cloud providers with CUDA/Python/Docker/SSH tooling and separate Launchables/Environments interfaces. Brev Connect registers customer-owned supported machines for access and connectivity while the owner retains host lifecycle responsibility.
- NVIDIA documents a capacity/data-resumption risk for stopped cloud instances: stopping releases GPU capacity while preserving certain workspace data with the original provider/region; a subsequent start may fail if capacity cannot be reprovisioned. Deletion loses instance data, while stopped instances may still incur storage charges; model and workspace backups should be external.
- Brev is an infrastructure management/provisioning identity, not original ownership of every underlying GPU host, trained model or a guarantee that supported GPU inventories, provisioning time, cost and deployment options are identical across regions/providers.
- Verified first-party source 1: https://docs.nvidia.com/brev/getting-started/overview
- Verified first-party source 2: https://docs.nvidia.com/brev/concepts/gpu-instances
- Verified first-party source 3: https://docs.nvidia.com/brev/concepts/brev-connect
- Acceptance scope: present provider documentation of the existing service identity and deployment-specific conditions only; not new metadata, reader repair, independent hardware execution, complete freshness/legal/security audit, root-wide schema/cache/CI/render, clean pass, final-delivery gate or merge.
