# Documentation Requirements

## Requirements

- Identify AMD Instinct MI300X as a released CDNA 3 datacenter OAM accelerator with **192 GB HBM3 memory** and up to **5.3 TB/s** peak theoretical per-module memory bandwidth, distinct from the later MI325X with 256 GB HBM3E and MI350/MI355 families.
- Separate the **per-GPU OAM module** from the eight-GPU MI300X Universal Baseboard (UBB) platform, whose aggregate HBM3 capacity and connectivity are not single-card specifications.
- Preserve OAM, 54 V UBB power, approximately 750 W board envelope, passive module cooling, Infinity Fabric and specialized server/cluster prerequisites. Do not imply ordinary consumer PCIe motherboard/workstation compatibility from the presence of PCIe interconnect semantics.
- Scope supported ROCm release, container/driver, framework/precision kernel support, networking/topology, GPU memory allocation and availability to dated official AMD documentation.
- Avoid unqualified performance or cost claims; AI workload throughput depends on precision, model, software/runtime, memory/cache, node layout and power configuration.
- Maintain AMD producer attribution and a reciprocal `produces` inverse.

## Validation

- MI300X and MI325X memory and bandwidth are not conflated.
- A module's published performance and memory are distinguished from the UBB system aggregate.
- Official references and reciprocal AMD relation resolve correctly.
