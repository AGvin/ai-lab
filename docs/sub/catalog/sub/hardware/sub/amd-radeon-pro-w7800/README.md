# AMD Radeon PRO W7800 family

AMD RDNA 3 workstation GPU family including distinct 32 GB and 48 GB Radeon PRO W7800 variants; they are not one interchangeable memory SKU.

## Manufacturer specifications

- Original W7800: 32 GB GDDR6, 256-bit interface, published up to 576 GB/s.
- W7800 48GB: 48 GB GDDR6, 384-bit interface, published up to 864 GB/s.
- Both configurations are described by AMD as 70-compute-unit workstation cards.

## AI workload and deployment boundaries

Keep 32 GB and 48 GB SKU characteristics separate. Real AI software support, power, board configuration and model fit must be checked per variant.

The listed specifications are manufacturer-published claims reviewed on 2026-11-05. They are not independent AI workload benchmarks, purchase availability checks or full driver compatibility testing.

## Producer

- Produced by [Advanced Micro Devices, Inc.](../../../producers/sub/a/sub/advanced-micro-devices-inc/)

## Official resources

- [Official manufacturer product page](https://www.amd.com/en/products/graphics/workstations/radeon-pro/w7800.html)
- [AMD separate 48 GB W7800 SKU](https://www.amd.com/en/products/graphics/workstations/radeon-pro/w7800-48gb.html)

## Scoped source qualification — 2026-11-05

AMD Radeon PRO W7800 is an RDNA 3 workstation family with distinct 32 GB and 48 GB GDDR6 configurations. The 32 GB SKU has a 256-bit bus and 576 GB/s published memory bandwidth, while W7800 48GB has 384-bit and 864 GB/s. AMD lists 70 compute units and 260 W board power for both. Do not conflate capacities, claim VRAM pooling or infer current ROCm/model compatibility from peak GPU specifications.

Both original AMD pages were checked independently. SKU features are not transferable, and no multi-GPU memory pooling, AI framework support or independent runtime performance is implied.
