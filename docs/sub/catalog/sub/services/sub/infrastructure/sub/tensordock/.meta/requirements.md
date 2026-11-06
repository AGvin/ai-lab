# Documentation Requirements

## Requirements

- Present TensorDock as a producer-operated GPU cloud marketplace/service that connects customers to GPU-backed virtual machines supplied across an independent hosting network.
- Explain the marketplace/decentralized-host distinction from direct single-provider GPU clouds without overstating host consistency or global availability.
- Cover root-access virtual machines, GPU selection, API access, and pay-as-you-go operation only where current first-party sources support those claims.
- Treat GPU inventory, host locations, prices, availability, and instance-product lifecycle labels as freshness-sensitive.
- Keep individual host/operator identity out of the canonical TensorDock producer relation unless independently materialized for another reason.
- Render the standard `entity-relations` block from validated current-entity relations.

## Validation

- TensorDock is classified as hosted infrastructure, not a model API.
- Marketplace ownership is not confused with ownership of every physical host.
- Mutable inventory and pricing claims are time-scoped when stated.

## Scoped original-source qualification — 2026-11-06

- TensorDock's original provider documentation describes a marketplace/API for GPU-backed virtual machines supplied through an aggregated network of independent hosts. VM root access and machine provisioning are infrastructure features; TensorDock does not become the manufacturer of rented GPUs or producer of the models running there.
- Provider-hosted FAQ distinguishes host quality tiers and warns that instance storage is local and not replicated; off-site backups and checkpointing are therefore the customer's responsibility. Host security, physical redundancy, uptime, actual capacity and reliability differ by offer; publisher promotional claims are not independently certified.
- Advertised hourly GPU prices may exclude configured CPU, RAM and storage charges and vary by host, region and offer. Do not freeze any observed price, availability, stock count or performance-versus-cost claim as timeless catalog data.
- Verified first-party source 1: https://docs.tensordock.com/
- Verified first-party source 2: https://www.tensordock.com/cloud-gpus.html
- Verified first-party source 3: https://production.dashboard.tensordock.com/faq
- Acceptance scope: present provider documentation of the existing service identity and deployment-specific conditions only; not new metadata, reader repair, independent hardware execution, complete freshness/legal/security audit, root-wide schema/cache/CI/render, clean pass, final-delivery gate or merge.
