# NVIDIA B200 Tensor Core GPU

**PROVENANCE/OWNERSHIP REVIEW PENDING.** Manufacturer attribution does not complete ownership/control-chain review or establish adoption clearance. See the [provenance policy](../../../../../project/sub/policies/sub/russia-linked-ai/).

NVIDIA B200 is a concrete Blackwell-generation data-center Tensor Core GPU product.

## Hardware boundary

B200 remains distinct from the Blackwell architecture concept, GB200 superchip identity, HGX and DGX systems, NVL72 rack systems, cloud instances, and CUDA or TensorRT software. Memory, compute capability, numeric formats, partitioning or MIG, interconnect, power, and form-factor facts apply only to the relevant B200 product or SKU scope.

Driver/runtime compatibility, lifecycle, cloud availability, pricing, and workload performance are mutable deployment facts.

## Relations

- Produced by [NVIDIA](../../../producers/sub/n/sub/nvidia/).

## Source interpretation

NVIDIA's versioned CUTLASS 4.3.1 table identifies B200 with compute capability 10.0 and a CUDA 12.8 minimum for that CUTLASS support table, not a universal framework minimum. The current HGX page states B200 systems are shipping; its eight-GPU memory/throughput totals are not single-B200 specifications. MIG profiles must match the B200 product, not GB200.

This bounded source review does not establish current pricing, local availability, full specification freshness, software entitlements or measured performance. No hardware or runtime validation was performed.

## Official resources

- [NVIDIA CUTLASS architecture overview](https://docs.nvidia.com/cutlass/4.3.1/overview.html)
- [NVIDIA MIG supported profiles](https://docs.nvidia.com/datacenter/tesla/mig-user-guide/supported-mig-profiles.html)
- [NVIDIA Blackwell tuning guide](https://docs.nvidia.com/cuda/archive/12.9.2/blackwell-tuning-guide/index.html)

- [Manufacturer supporting documentation](https://www.nvidia.com/en-us/data-center/hgx/)
