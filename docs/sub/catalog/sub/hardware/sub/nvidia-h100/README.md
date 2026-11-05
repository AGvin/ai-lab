# NVIDIA H100 Tensor Core GPU

**PROVENANCE/OWNERSHIP REVIEW PENDING.** Manufacturer attribution does not complete ownership/control-chain review or establish adoption clearance. See the [provenance policy](../../../../../project/sub/policies/sub/russia-linked-ai/).

NVIDIA H100 is NVIDIA's Hopper-architecture data-center Tensor Core GPU family for accelerated AI and HPC workloads.

## Hardware boundary

H100 remains distinct from the Hopper architecture itself, H200, HGX or DGX systems containing H100 GPUs, cloud instance products, and CUDA or TensorRT-LLM software. H100 SXM and H100 NVL or PCIe-class delivery have materially different memory, bandwidth, power, form-factor, and interconnect characteristics, so variant-specific specifications must stay attached to the correct form factor or SKU.

Driver/runtime compatibility, virtualization or MIG support, support lifecycle, cloud availability, pricing, and workload performance are mutable facts. Vendor performance comparisons remain meaningful only with their workload, precision, sparsity, system scale, latency, and other benchmark conditions.

## Relations

- Produced by [NVIDIA](../../../producers/sub/n/sub/nvidia/).

## Source interpretation

NVIDIA identifies H100 as a Hopper data-center GPU and documents distinct product/integration forms, including H100 NVL. H100, H200, complete HGX/DGX hosts and cloud instances are different identities. Confirm the delivered form factor, memory, interconnect and supported runtime rather than treating one H100 configuration as universal.

This bounded source review does not establish current pricing, local availability, full specification freshness, software entitlements or measured performance. No hardware or runtime validation was performed.

## Official resources

- [NVIDIA H100 Tensor Core GPU](https://www.nvidia.com/en-us/data-center/h100/)
- [NVIDIA Hopper architecture](https://www.nvidia.com/en-us/data-center/technologies/hopper-architecture/)
