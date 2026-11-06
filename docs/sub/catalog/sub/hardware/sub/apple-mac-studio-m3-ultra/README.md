# Apple Mac Studio (M3 Ultra, 2025)

Apple Mac Studio 2025 configuration with M3 Ultra integrated SoC, not a standalone GPU or the M4 Max configuration.

## Manufacturer specifications

- M3 Ultra base: 28-core CPU, 60-core GPU and 32-core Neural Engine; upgraded chip: 32-core CPU, 80-core GPU.
- Apple specifies 819 GB/s unified-memory bandwidth and 96 GB base unified memory.
- Historical March 2025 launch material advertised up to 512 GB unified memory; current build-to-order options require separate verification.

## AI workload and deployment boundaries

Unified system memory is shared by CPU/GPU, not equivalent to dedicated VRAM or all available for model weights. macOS/Metal/MLX support and throughput differ from CUDA/ROCm; verify the actual configuration.

The listed specifications are manufacturer-published claims reviewed on 2026-11-05. They are not independent AI workload benchmarks, purchase availability checks or full driver compatibility testing.

## Producer

- Produced by [Apple Inc.](../../../producers/sub/a/sub/apple-inc/)

## Official resources

- [Official manufacturer product page](https://support.apple.com/en-gb/122211)
- [Apple March 2025 M3 Ultra launch statement](https://www.apple.com/newsroom/2025/03/apple-reveals-m3-ultra-taking-apple-silicon-to-a-new-extreme/)
