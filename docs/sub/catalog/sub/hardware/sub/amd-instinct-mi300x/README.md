# AMD Instinct MI300X

**PROVENANCE/OWNERSHIP REVIEW PENDING.** See the [provenance policy](../../../../../project/sub/policies/sub/russia-linked-ai/).

AMD's MI300X is a discrete CDNA 3 accelerator with 192 GB HBM3 per module. The documented eight-module Universal Baseboard is a system configuration, not one GPU's capacity; OAM and platform power/cooling requirements preclude assuming ordinary workstation-card compatibility. Model fit, measured performance, current availability and software entitlements require separate validation. Ownership/control-chain review remains pending; source attribution is not adoption clearance.

## Deployment boundary

Use the manufacturer's system acceptance criteria for firmware, Linux/ROCm support, power, cooling and topology. Inspect the intended framework and kernel support before deployment. Physical memory also serves workload allocations and cache; vendor peak figures are not measured model throughput. No hardware/runtime tests or complete specification freshness audit were performed.

## Producer

- [AMD](../../../producers/sub/a/sub/advanced-micro-devices-inc/)

## Official resources

- <https://www.amd.com/en/products/accelerators/instinct/mi300/mi300x.html>
- <https://instinct.docs.amd.com/projects/system-acceptance/en/latest/gpus/mi300x.html>
