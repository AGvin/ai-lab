# NVIDIA RTX 6000 Ada Generation

NVIDIA RTX 6000 Ada Generation is a professional Ada Lovelace workstation GPU with 48 GB ECC GDDR6 memory. NVIDIA specifies PCIe Gen4 x16, a dual-slot active cooling design and 300 W maximum power. AI development and inference share the device with its visualization and rendering roles.

## Deployment boundaries

The product is distinct from the Ampere RTX A6000, the 96 GB RTX PRO 6000 Blackwell and the 24 GB GeForce RTX 4090. Similar naming or memory size does not make their architecture, power or support boundaries equivalent.

Validate the chassis, PSU, cooling and supported driver/runtime combination. The 48 GB specification is physical memory, not an assured 48 GB model-weight budget; cache, activations and runtime allocations also count. Measured performance requires a named workload, precision and software version. Enterprise AI subscriptions and vGPU software have their own entitlement and compatibility requirements; they should not be assumed to follow from owning a card or using ordinary local CUDA. Current availability, pricing and support must be checked separately.

## Producer

- Produced by [NVIDIA](../../../producers/sub/n/sub/nvidia/README.md).

## Official resources

- [Product, specifications and software licensing links](https://www.nvidia.com/en-us/products/workstations/rtx-6000/)
