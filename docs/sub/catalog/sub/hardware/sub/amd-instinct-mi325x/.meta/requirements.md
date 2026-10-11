# Documentation Requirements

## Requirements

- Identify AMD Instinct MI325X as the released CDNA 3 datacenter OAM accelerator SKU with 256 GB HBM3E and approximately 6 TB/s peak memory bandwidth, distinct from the complete eight-accelerator MI325X Platform and successor MI350X/MI355X products.
- Preserve exact OAM/UBB system requirements, host connectivity, typical board power, thermal conditions and Infinity Fabric configuration; do not imply that a 256 GB OAM module is an off-the-shelf PCIe workstation graphics card.
- Treat ROCm release and framework support, interconnect/multi-GPU provisioning, FP8/BF16/FP16 formats, capacity, availability and validated performance as version-sensitive and deployment-specific.
- Separate the per-accelerator 256 GB HBM3E memory figure from the eight-module UBB system total; preserve any bandwidth and power figures with their module-versus-platform unit scope.
- Do not transform AMD vendor-vs-competitor peak marketing metrics into cross-vendor workload conclusions absent matched independent benchmarks.
- Preserve AMD as the canonical producer with the matching inverse `produces` relation.

## Validation

- The exact SKU and memory capacity match the official AMD product specification.
- Hardware form factors and system-level specifications are not mixed between workstations and datacenters.
- Driver compatibility and performance claims are constrained to the applicable release, environment and model workload.
- Producer provenance is reciprocal.
