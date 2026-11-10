# NVIDIA RTX A6000

**PROVENANCE/OWNERSHIP REVIEW PENDING.** Manufacturer attribution does not complete ownership/control-chain review or establish adoption clearance. See the [provenance policy](../../../../../project/sub/policies/sub/russia-linked-ai/).

NVIDIA RTX A6000 is an Ampere professional workstation GPU with 48 GB ECC GDDR6 memory. NVIDIA lists PCIe Gen4 x16, a dual-slot active cooling design and 300 W maximum power. Its AI compute role is separate from the card’s graphics, rendering and virtual-workstation uses.

## Deployment boundaries

RTX A6000 is distinct from RTX 6000 Ada Generation and RTX PRO 6000 Blackwell despite similar names. The published two-way NVLink bridge option connects compatible cards but does not automatically give every application one 96 GB allocation; software parallelism, topology and runtime support determine memory use.

Validate board clearance, bridge spacing where applicable, power delivery, cooling and the exact driver/runtime combination. Ampere does not inherit newer Ada/Blackwell numeric-format acceleration. Model weights share memory with cache, activations and runtime allocations, so physical capacity alone does not establish model fit. Compare measured workloads at matched precision and software versions. vGPU or enterprise software entitlements, current hardware supply, warranty and support are separate mutable facts.

## Producer

- Produced by [NVIDIA](../../../producers/sub/n/sub/nvidia/README.md).

## Source interpretation

NVIDIA identifies Ampere RTX A6000 with 48 GB ECC GDDR6 and a two-way NVLink option. It is not RTX 6000 Ada or RTX PRO 6000 Blackwell. Two connected devices do not automatically provide every application one 96 GB allocation; topology and software parallelism determine usable memory. Check board and software entitlement requirements separately.

This bounded source review does not establish current pricing, local availability, full specification freshness, software entitlements or measured performance. No hardware or runtime validation was performed.

## Official resources

- [Product, NVLink and specifications](https://www.nvidia.com/en-us/products/workstations/rtx-a6000/)
