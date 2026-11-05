# Documentation Requirements

## Requirements

- Preserve the exact product/system identity and distinguish variants and neighboring families.
- Use official manufacturer specifications for the scoped, SKU-specific facts:
- 16 GB GDDR7, 256-bit memory interface.
- NVIDIA specifies 8,960 CUDA cores and fifth-generation Tensor Cores.
- PCIe Gen 5 support; exact power and dimensions depend on partner board.
- Keep Ti and non-Ti specifications in separate columns. Advertised AI TOPS are not measured serving latency; VRAM is local and not automatically pooled across cards.
- Separate mutable price, availability, driver/OS support, performance and real inference results from static catalog identity.
- Maintain a `produced-by` relation and reciprocal producer link.

## Validation

- The identity, first-party source and variant boundary are explicit.
- No cross-SKU spec conflation, inferred pooled memory or TOPS-as-token-throughput claim.
- Catalog-wide CI, renderer, license audit and clean-group passes remain separate.
