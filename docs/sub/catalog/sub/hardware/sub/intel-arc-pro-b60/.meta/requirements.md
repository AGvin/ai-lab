# Documentation Requirements

## Requirements

- Preserve the exact product/system identity and distinguish variants and neighboring families.
- Use official manufacturer specifications for the scoped, SKU-specific facts:
- 24 GB GDDR6, 192-bit memory bus, up to 456 GB/s bandwidth.
- 20 Xe-cores and 160 XMX engines.
- PCIe 5.0 x8; 200 W nominal board power with lower-power board variants.
- Do not substitute B65 memory or PCIe figures. Real throughput depends on workload, firmware, cooling and supported software. Multiple discrete GPUs do not automatically pool VRAM.
- Separate mutable price, availability, driver/OS support, performance and real inference results from static catalog identity.
- Maintain a `produced-by` relation and reciprocal producer link.

## Validation

- The identity, first-party source and variant boundary are explicit.
- No cross-SKU spec conflation, inferred pooled memory or TOPS-as-token-throughput claim.
- Catalog-wide CI, renderer, license audit and clean-group passes remain separate.
