# Documentation Requirements

## Requirements

- Preserve the exact product/system identity and distinguish variants and neighboring families.
- Use official manufacturer specifications for the scoped, SKU-specific facts:
- NVL72 combines 72 Rubin GPUs with 36 Vera CPUs.
- NVIDIA lists 20.7 TB aggregate HBM4 GPU memory across the rack.
- Sixth-generation NVLink fabric connects rack-scale components.
- Rack aggregate memory, interconnect and marketed throughput cannot be attributed to a single GPU. Deployment requires datacenter power, liquid cooling, network, OEM integration and verified delivery/support.
- Separate mutable price, availability, driver/OS support, performance and real inference results from static catalog identity.
- Maintain a `produced-by` relation and reciprocal producer link.

## Validation

- The identity, first-party source and variant boundary are explicit.
- No cross-SKU spec conflation, inferred pooled memory or TOPS-as-token-throughput claim.
- Catalog-wide CI, renderer, license audit and clean-group passes remain separate.
