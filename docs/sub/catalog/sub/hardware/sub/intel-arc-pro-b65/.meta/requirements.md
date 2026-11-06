# Documentation Requirements

## Requirements

- Preserve the exact product/system identity and distinguish variants and neighboring families.
- Use official manufacturer specifications for the scoped, SKU-specific facts:
- 32 GB GDDR6, 256-bit interface, published 608 GB/s bandwidth.
- 20 Xe-cores and 160 XMX engines.
- PCIe 5.0 x16 and 200 W total board power.
- B65 memory and PCIe interface are not B60's. Peak TOPS are theoretical, not measured tokens/s; verify host lanes, drivers and board cooling.
- Separate mutable price, availability, driver/OS support, performance and real inference results from static catalog identity.
- Maintain a `produced-by` relation and reciprocal producer link.

## Validation

- The identity, first-party source and variant boundary are explicit.
- No cross-SKU spec conflation, inferred pooled memory or TOPS-as-token-throughput claim.
- Catalog-wide CI, renderer, license audit and clean-group passes remain separate.
