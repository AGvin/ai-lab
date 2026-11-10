# AMD Instinct MI355X

**PROVENANCE/OWNERSHIP REVIEW PENDING.** See the [provenance policy](../../../../../project/sub/policies/sub/russia-linked-ai/).

AMD Instinct MI355X is a concrete MI350 Series data-center GPU product for accelerated AI and HPC workloads.

## Hardware boundary

MI355X remains distinct from MI350X, the complete eight-GPU MI355X Platform or other systems, CDNA 4 architecture concepts, cloud instances, and ROCm/runtime software. Memory, bandwidth, supported numeric formats, interconnect, power, and form factor belong to the applicable MI355X product or SKU scope rather than every MI350-family configuration.

Driver/runtime compatibility, support lifecycle, cloud availability, pricing, and workload performance are mutable deployment facts.

## Relations

- Produced by [Advanced Micro Devices, Inc.](../../../producers/sub/a/sub/advanced-micro-devices-inc/).

## Source interpretation

AMD's MI355X is a CDNA 4 OAM accelerator with 288 GB HBM3E per GPU, distinct from its eight-accelerator platform and sibling SKU. AMD's microarchitecture documentation distinguishes MI350X air cooling from MI355X direct liquid cooling. The acceptance guide's HBM3 wording and MI355X overview's MI350X reference conflict with the SKU/product and architecture sources; use those sources for exact identity and memory type. ROCm/OS, firmware, power and cooling require configuration-specific validation. Ownership/control review remains pending; no runtime or adoption clearance.

No hardware tests, benchmarks or full specification freshness audit were performed.

## Official resources

- [AMD Instinct MI355X](https://www.amd.com/en/products/accelerators/instinct/mi350/mi355x.html)
- [AMD MI355X system acceptance documentation](https://instinct.docs.amd.com/projects/system-acceptance/en/latest/gpus/mi355x.html)

- [AMD MI350 architecture and cooling distinctions](https://rocmdocs.amd.com/en/latest/reference/gpu-arch/mi350.html)
