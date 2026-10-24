# NVIDIA L4 Tensor Core GPU

NVIDIA L4 is an Ada Lovelace server accelerator for AI inference, graphics, audio/video processing and virtualization. Its published specifications are 24 GB GDDR6 memory, 300 GB/s peak memory bandwidth and 72 W maximum TDP per physical card. The PCIe Gen4 x16 card is half-height, half-length, single-slot and passively cooled.

## Deployment boundaries

This low-profile form factor still requires qualified system airflow and host/driver support. It does not guarantee compatibility with an arbitrary desktop chassis or PSU. L4 remains distinct from the 48 GB L40S, T4, HBM-based A100/H100/H200 accelerators and any cloud or virtual-GPU bundle.

Fourth-generation Tensor Cores, FP8 and AV1 media execution have specific software and precision conditions. NVIDIA theoretical Tensor Core figures include sparsity, while its video pipeline comparisons use named hardware and software; neither establishes universal LLM speedups or energy savings. Effective model capacity, cache, batch throughput and CPU/network overhead need workload testing. Virtualization entitlements, instance availability, pricing and lifecycle support require separate current verification.

## Producer

- Produced by [NVIDIA](../../../producers/sub/n/sub/nvidia/README.md).

## Official resources

- [Product and performance conditions](https://www.nvidia.com/en-us/data-center/l4/)
- [L4 product brief, March 2023](https://www.nvidia.com/content/dam/en-zz/Solutions/Data-Center/l4/PB-11316-001_v01.pdf)
