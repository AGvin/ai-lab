# Documentation Requirements

## Requirements

- Preserve the exact product/system identity and distinguish variants and neighboring families.
- Use official manufacturer specifications for the scoped, SKU-specific facts:
- 16 GB GDDR7 local graphics memory.
- NVIDIA reference specifications list 360 W total graphics power.
- PCIe Gen 5 interface; no NVLink on this GeForce model.
- Physical VRAM is not entirely available for model weights once context and runtime allocations are included. AI TOPS and gaming scores are not measured LLM inference throughput; check partner-board power and driver support.
- Separate mutable price, availability, driver/OS support, performance and real inference results from static catalog identity.
- Maintain a `produced-by` relation and reciprocal producer link.

## Validation

- The identity, first-party source and variant boundary are explicit.
- No cross-SKU spec conflation, inferred pooled memory or TOPS-as-token-throughput claim.
- Catalog-wide CI, renderer, license audit and clean-group passes remain separate.
