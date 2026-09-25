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
