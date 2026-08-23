# Documentation Requirements

## Requirements

- Cover Linux-capable SBC/developer-board ecosystems whose board/SoC/accelerator stack creates a distinct local model route.
- Route current initial ecosystems to `raspberry-pi/`, `jetson/`, and `rockchip/`.
- Do not use `edge/` as the taxonomy parent: edge is deployment context that can also describe mini PCs, gateways, industrial PCs, or servers.
- Require exact board/SoC, RAM, OS/toolkit, accelerator, storage/IO, power/cooling, runtime, and sustained-load conditions.
- Distinguish CPU-only inference from NPU/GPU/accelerator-specific conversion/runtime paths.

## Validation

- Direct children are Raspberry Pi, Jetson, and Rockchip ecosystem routes.
- Board vendors sharing the same Rockchip SoC/RKNN route are not duplicated merely for branding.
- TOPS alone is never a model-compatibility or practical-fit claim.
