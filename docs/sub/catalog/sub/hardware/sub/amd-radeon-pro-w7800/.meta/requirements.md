# Documentation Requirements

## Requirements

- Preserve the exact product/system identity and distinguish variants and neighboring families.
- Use official manufacturer specifications for the scoped, SKU-specific facts:
- Original W7800: 32 GB GDDR6, 256-bit interface, published up to 576 GB/s.
- W7800 48GB: 48 GB GDDR6, 384-bit interface, published up to 864 GB/s.
- Both configurations are described by AMD as 70-compute-unit workstation cards.
- Keep 32 GB and 48 GB SKU characteristics separate. Real AI software support, power, board configuration and model fit must be checked per variant.
- Separate mutable price, availability, driver/OS support, performance and real inference results from static catalog identity.
- Maintain a `produced-by` relation and reciprocal producer link.

## Validation

- The identity, first-party source and variant boundary are explicit.
- No cross-SKU spec conflation, inferred pooled memory or TOPS-as-token-throughput claim.
- Catalog-wide CI, renderer, license audit and clean-group passes remain separate.

## Scoped original-source acceptance — 2026-11-05

- AMD Radeon PRO W7800 is an RDNA 3 workstation family with distinct 32 GB and 48 GB GDDR6 configurations. The 32 GB SKU has a 256-bit bus and 576 GB/s published memory bandwidth, while W7800 48GB has 384-bit and 864 GB/s. AMD lists 70 compute units and 260 W board power for both. Do not conflate capacities, claim VRAM pooling or infer current ROCm/model compatibility from peak GPU specifications.
- First-party 32 GB W7800: https://www.amd.com/en/products/graphics/workstations/radeon-pro/w7800.html.
- First-party 48 GB W7800: https://www.amd.com/en/products/graphics/workstations/radeon-pro/w7800-48gb.html.
- Product pages verify variant specifications only; software support, current procurement stock, licensing clearance, final render/cache/schema/CI and real application throughput remain unverified.
