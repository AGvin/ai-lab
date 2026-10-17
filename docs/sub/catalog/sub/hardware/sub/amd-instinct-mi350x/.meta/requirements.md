# Documentation Requirements

## Requirements

- Identify AMD Instinct MI350X as an AMD Instinct MI350 Series data-center GPU accelerator built on AMD CDNA 4 for AI and HPC workloads.
- Keep MI350X distinct from the broader MI350 Series, sibling MI355X, complete 8-accelerator MI350 platform/server products, cloud instance offerings, and ROCm or other software/runtime identities.
- Preserve stable product-level facts only at the correct SKU/form-factor boundary. Current first-party specifications identify MI350X as an OAM server accelerator with 288 GB HBM3E and support for low-precision AI formats; exact clocks, bandwidth, power, precision throughput, platform topology, and feature support must remain source-backed to the applicable product revision.
- Treat driver/ROCm compatibility, supported operating systems, virtualization, support lifecycle, cloud availability, pricing, and workload performance as mutable facts requiring current verification.
- When vendor performance comparisons are referenced, preserve workload, precision, sparsity, system-scale, software-stack, and benchmark conditions and do not treat vendor comparison claims as neutral cross-vendor evidence.
- Render the standard `entity-relations` block from validated current-entity relations and preserve Advanced Micro Devices, Inc. as the producer.
- Include current official product and system-acceptance documentation references.

## Validation

- MI350X is not collapsed with MI355X, the MI350 Series platform, CDNA 4 as an architecture, or ROCm software.
- Exact specifications remain attached to MI350X rather than generalized to every MI350-family product.
- Mutable compatibility/support/performance claims are not presented as timeless hardware identity facts.
- The `produces` / `produced-by` relation pair resolves consistently to Advanced Micro Devices, Inc.
