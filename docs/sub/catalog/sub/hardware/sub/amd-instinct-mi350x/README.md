# AMD Instinct MI350X

**PROVENANCE/OWNERSHIP REVIEW PENDING.** See the [provenance policy](../../../../../project/sub/policies/sub/russia-linked-ai/).

AMD Instinct MI350X is a CDNA 4 data-center GPU accelerator in the AMD Instinct MI350 Series for AI and HPC workloads.

## Hardware boundary

MI350X is an OAM server accelerator with 288 GB HBM3E and support for low-precision AI formats. It remains distinct from the broader MI350 Series, sibling MI355X, complete multi-accelerator platform or server products, cloud instances, and ROCm/runtime software. Exact clocks, bandwidth, power, throughput, topology, and feature support belong to the applicable product revision rather than the entire family.

Driver and ROCm compatibility, operating-system support, virtualization, lifecycle, cloud availability, pricing, and workload performance are mutable deployment facts.

## Relations

- Produced by [Advanced Micro Devices, Inc.](../../../producers/sub/a/sub/advanced-micro-devices-inc/).

## Source interpretation

AMD's MI350X is a CDNA 4 OAM accelerator with 288 GB HBM3E per GPU, distinct from its eight-accelerator platform and sibling SKU. AMD's microarchitecture documentation distinguishes MI350X air cooling from MI355X direct liquid cooling. The acceptance guide's HBM3 wording and MI355X overview's MI350X reference conflict with the SKU/product and architecture sources; use those sources for exact identity and memory type. ROCm/OS, firmware, power and cooling require configuration-specific validation. Ownership/control review remains pending; no runtime or adoption clearance.

No hardware tests, benchmarks or full specification freshness audit were performed.

## Official resources

- [AMD Instinct MI350X](https://www.amd.com/en/products/accelerators/instinct/mi350/mi350x.html)
- [AMD MI350X system acceptance documentation](https://instinct.docs.amd.com/projects/system-acceptance/en/latest/gpus/mi350x.html)

- [AMD MI350 architecture and cooling distinctions](https://rocmdocs.amd.com/en/latest/reference/gpu-arch/mi350.html)
