# Documentation Requirements

## Requirements

- Preserve the exact product/system identity and distinguish variants and neighboring families.
- Use official manufacturer specifications for the scoped, SKU-specific facts:
- NVIDIA's marketplace describes 32 GB ECC GDDR7 graphics memory.
- NVIDIA specifies up to 896 GB/s memory bandwidth and 200 W maximum GPU power for the Workstation Edition.
- Workstation Edition is an active-cooled dual-slot board class.
- Board dimensions, clocks and power requirements may differ by NVIDIA partner SKU.
- 32 GB is local GPU memory, not pooled across cards. Validate board vendor, cooling, certified driver, CUDA runtime and actual model/precision compatibility.
- Separate mutable price, availability, driver/OS support, performance and real inference results from static catalog identity.
- Maintain a `produced-by` relation and reciprocal producer link.

## Validation

- The identity, first-party source and variant boundary are explicit.
- No cross-SKU spec conflation, inferred pooled memory or TOPS-as-token-throughput claim.
- Catalog-wide CI, renderer, license audit and clean-group passes remain separate.
