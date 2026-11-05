# Documentation Requirements

## Requirements

- Preserve the exact product/system identity and distinguish variants and neighboring families.
- Use official manufacturer specifications for the scoped, SKU-specific facts:
- 64 GB HBM2e, published bandwidth up to 1.6 TB/s.
- 104 compute units, PCIe 4.0 x16, up to three Infinity Fabric links.
- 300 W passive-cooled server accelerator.
- Passive cooling needs forced server airflow; Infinity Fabric requires compatible host topology and bridges. Each card has its own memory; check ROCm release and real workload throughput.
- Separate mutable price, availability, driver/OS support, performance and real inference results from static catalog identity.
- Maintain a `produced-by` relation and reciprocal producer link.

## Validation

- The identity, first-party source and variant boundary are explicit.
- No cross-SKU spec conflation, inferred pooled memory or TOPS-as-token-throughput claim.
- Catalog-wide CI, renderer, license audit and clean-group passes remain separate.

## Scoped original-source acceptance — 2026-11-05

- AMD's original MI210 acceptance guidance identifies a CDNA 2 PCIe Gen4 x16 server accelerator with 104 compute units, 64 GB HBM2e, up to 1.6 TB/s manufacturer memory bandwidth and 300 W passive cooling. Infinity Fabric direct card-to-card links require matching bridges; MI250/MI250X OAM hardware, pooled memory, ROCm compatibility and verified model throughput must not be inferred.
- First-party AMD acceptance source: https://instinct.docs.amd.com/projects/system-acceptance/en/latest/gpus/mi210.html.
- Static manufacturer specifications are not independent benchmarks, real inventory, licensing clearance or a complete current ROCm/OS support matrix. Full schema/CI/cache/render and runtime integration were not run.
