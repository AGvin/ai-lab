# AMD Instinct MI210

AMD CDNA 2 PCIe server accelerator, distinct from MI250 OAM and later Instinct MI300/MI400 families.

## Manufacturer specifications

- 64 GB HBM2e, published bandwidth up to 1.6 TB/s.
- 104 compute units, PCIe 4.0 x16, up to three Infinity Fabric links.
- 300 W passive-cooled server accelerator.

## AI workload and deployment boundaries

Passive cooling needs forced server airflow; Infinity Fabric requires compatible host topology and bridges. Each card has its own memory; check ROCm release and real workload throughput.

The listed specifications are manufacturer-published claims reviewed on 2026-11-05. They are not independent AI workload benchmarks, purchase availability checks or full driver compatibility testing.

## Producer

- Produced by [Advanced Micro Devices, Inc.](../../../producers/sub/a/sub/advanced-micro-devices-inc/)

## Official resources

- [Official manufacturer product page](https://www.amd.com/en/products/accelerators/instinct/mi200/mi210.html)
- [AMD MI210 system acceptance guidance](https://instinct.docs.amd.com/projects/system-acceptance/en/latest/gpus/mi210.html)

## Scoped source qualification — 2026-11-05

AMD's original MI210 acceptance guidance identifies a CDNA 2 PCIe Gen4 x16 server accelerator with 104 compute units, 64 GB HBM2e, up to 1.6 TB/s manufacturer memory bandwidth and 300 W passive cooling. Infinity Fabric direct card-to-card links require matching bridges; MI250/MI250X OAM hardware, pooled memory, ROCm compatibility and verified model throughput must not be inferred.

Verified against the linked AMD original acceptance guidance. This is not an independent inference benchmark, a procurement/availability check or current driver/OS certification.
