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
