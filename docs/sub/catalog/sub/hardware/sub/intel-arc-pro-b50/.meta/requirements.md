# Documentation Requirements

## Requirements

- Preserve the exact product/system identity and distinguish variants and neighboring families.
- Use official manufacturer specifications for the scoped, SKU-specific facts:
- 16 GB GDDR6, 128-bit bus, published 224 GB/s memory bandwidth.
- 16 Xe-cores, 128 XMX engines, nominal 70 W total board power.
- PCIe 5.0 x8; vendor specifies ECC support.
- The nominal board-power figure is not whole-system draw. Peak dense INT8 TOPS are not validated LLM tokens/s; check model, precision, driver, host, cooling and framework support.
- Separate mutable price, availability, driver/OS support, performance and real inference results from static catalog identity.
- Maintain a `produced-by` relation and reciprocal producer link.

## Validation

- The identity, first-party source and variant boundary are explicit.
- No cross-SKU spec conflation, inferred pooled memory or TOPS-as-token-throughput claim.
- Catalog-wide CI, renderer, license audit and clean-group passes remain separate.
