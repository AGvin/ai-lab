# Documentation Requirements

## Requirements

- Identify NVIDIA RTX A6000 as the released **Ampere-generation professional workstation GPU** with **48 GB ECC-capable GDDR6**, distinct from the later RTX 6000 Ada Generation and NVIDIA RTX PRO 6000 Blackwell products.
- Preserve the PCI Express Gen4 x16, dual-slot actively cooled workstation board with up to **300 W power consumption**, display outputs, enterprise workstation/vGPU features and professional driver/software ecosystem. It is not the passive NVIDIA L40S datacenter board.
- Preserve supported **two-way NVLink bridge** configurations and application-specific memory/compute scaling boundaries. Connecting two 48 GB cards does not automatically present a single coherent 96 GB GPU allocation to every LLM runtime, application or framework; software explicitly supporting sharded/distributed model execution is required.
- Distinguish RTX A6000's Ampere tensor precision capabilities from Ada/Blackwell FP8 or other newer generation tensor formats and from NVIDIA A100/H100/H200 datacenter accelerators with HBM memory; do not reuse mismatched architecture benchmark results.
- Keep lifecycle, resale availability, driver/CUDA framework compatibility, virtualization licensing, thermals, pricing and model throughput as mutable facts requiring versioned sources; do not imply that current official product documentation guarantees indefinite new-product sales.
- Attribute original physical GPU product and exact form-factor specification to NVIDIA and preserve reciprocal producer relations.

## Validation

- RTX A6000 Ampere is not conflated with RTX 6000 Ada (despite both having 48 GB GDDR6) or RTX PRO 6000 Blackwell.
- The 48 GB specification refers to one physical card; NVLink support does not imply universal pooled VRAM.
- Product source and `produced-by` / `produces` inverse agree on NVIDIA.
