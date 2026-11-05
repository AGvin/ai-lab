# NVIDIA B300 Tensor Core GPU

**PROVENANCE/OWNERSHIP REVIEW PENDING.** Manufacturer attribution does not complete ownership/control-chain review or establish adoption clearance. See the [provenance policy](../../../../../project/sub/policies/sub/russia-linked-ai/).

NVIDIA B300 is a concrete Blackwell Ultra-generation data-center Tensor Core GPU product.

## Hardware boundary

B300 remains distinct from B200, Blackwell Ultra architecture concepts, HGX or DGX B300 systems, NVL72 rack-scale platforms, cloud instances, and CUDA/runtime software. Memory, compute capability, numeric formats, interconnect, partitioning, power, and form-factor facts apply only to the relevant B300 product or SKU scope and must not be inferred from system-level specifications.

Driver/runtime compatibility, lifecycle, cloud availability, pricing, and workload performance are mutable deployment facts.

## Relations

- Produced by [NVIDIA](../../../producers/sub/n/sub/nvidia/).

## Source interpretation

NVIDIA's versioned CUTLASS 4.3.1 table identifies B300 with compute capability 10.3 and a CUDA 13.0 minimum for that CUTLASS support table. The current HGX page states B300 systems are shipping; HGX B300 is an eight-GPU system, not this individual GPU identity. Preserve Blackwell Ultra versus B200 and validate exact runtime builds instead of transferring a family-wide compatibility claim.

This bounded source review does not establish current pricing, local availability, full specification freshness, software entitlements or measured performance. No hardware or runtime validation was performed.

## Official resources

- [NVIDIA CUTLASS architecture overview](https://docs.nvidia.com/cutlass/4.3.1/overview.html)
- [NVIDIA NIM reward-model documentation](https://docs.nvidia.com/nim/large-language-models/latest/reward-model.html)

- [Manufacturer supporting documentation](https://www.nvidia.com/en-us/data-center/hgx/)
