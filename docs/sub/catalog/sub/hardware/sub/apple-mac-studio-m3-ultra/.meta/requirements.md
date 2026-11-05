# Documentation Requirements

## Requirements

- Preserve the exact product/system identity and distinguish variants and neighboring families.
- Use official manufacturer specifications for the scoped, SKU-specific facts:
- M3 Ultra base: 28-core CPU, 60-core GPU and 32-core Neural Engine; upgraded chip: 32-core CPU, 80-core GPU.
- Apple specifies 819 GB/s unified-memory bandwidth and 96 GB base unified memory.
- Historical March 2025 launch material advertised up to 512 GB unified memory; current build-to-order options require separate verification.
- Unified system memory is shared by CPU/GPU, not equivalent to dedicated VRAM or all available for model weights. macOS/Metal/MLX support and throughput differ from CUDA/ROCm; verify the actual configuration.
- Separate mutable price, availability, driver/OS support, performance and real inference results from static catalog identity.
- Maintain a `produced-by` relation and reciprocal producer link.

## Validation

- The identity, first-party source and variant boundary are explicit.
- No cross-SKU spec conflation, inferred pooled memory or TOPS-as-token-throughput claim.
- Catalog-wide CI, renderer, license audit and clean-group passes remain separate.
