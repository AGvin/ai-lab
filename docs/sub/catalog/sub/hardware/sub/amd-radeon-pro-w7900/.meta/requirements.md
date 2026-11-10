# Documentation Requirements

## Requirements

- Preserve the exact product/system identity and distinguish variants and neighboring families.
- Use official manufacturer specifications for the scoped, SKU-specific facts:
- 48 GB GDDR6, 384-bit interface, published up to 864 GB/s bandwidth.
- 96 compute units and 192 AI accelerators.
- 295 W total board power and PCIe 4.0 x16 interface.
- Peak performance metrics and pro-graphics certifications are not proof of supported ROCm kernels or LLM serving performance. Verify exact card, PSU, driver, OS and memory budget.
- Separate mutable price, availability, driver/OS support, performance and real inference results from static catalog identity.
- Maintain a `produced-by` relation and reciprocal producer link.

## Validation

- The identity, first-party source and variant boundary are explicit.
- No cross-SKU spec conflation, inferred pooled memory or TOPS-as-token-throughput claim.
- Catalog-wide CI, renderer, license audit and clean-group passes remain separate.

## Scoped original-source acceptance — 2026-11-05

- AMD Radeon PRO W7900 is an RDNA 3 workstation card distinct from W7800 and the Instinct CDNA family. AMD lists 48 GB GDDR6, a 384-bit interface with up to 864 GB/s memory bandwidth, 96 compute units, 192 AI accelerators, PCIe 4.0 x16 and 295 W total board power. Published peak matrix TOPS do not establish ROCm compatibility, real inference throughput, model fit or procurement availability.
- Original AMD product specifications: https://www.amd.com/en/products/graphics/workstations/radeon-pro/w7900.html.
- Manufacturer peak figures are not independent AI benchmarks, software support or current stock evidence. Full schema/CI/cache/render, legal/provenance clearance and runtime integration were not run.
