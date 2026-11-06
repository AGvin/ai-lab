# Documentation Requirements

## Requirements

- Preserve the exact product/system identity and distinguish variants and neighboring families.
- Use official manufacturer specifications for the scoped, SKU-specific facts:
- 12 GB GDDR6, 192-bit bus, published 456 GB/s memory bandwidth.
- 20 Xe-cores and 160 XMX engines.
- 190 W total board power; PCIe 4.0 x8.
- Consumer driver features and 12 GB VRAM differ from Arc Pro models. Peak INT8 figures are not independently measured inference speed; verify model fit and supported software.
- Separate mutable price, availability, driver/OS support, performance and real inference results from static catalog identity.
- Maintain a `produced-by` relation and reciprocal producer link.

## Validation

- The identity, first-party source and variant boundary are explicit.
- No cross-SKU spec conflation, inferred pooled memory or TOPS-as-token-throughput claim.
- Catalog-wide CI, renderer, license audit and clean-group passes remain separate.
