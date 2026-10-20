# NVIDIA DGX Station

NVIDIA DGX Station is a complete deskside AI system based on the GB300 Grace Blackwell Ultra Desktop Superchip. It supports local development, fine-tuning, inference and persistent agent workloads. The system is distinct from the underlying chip, OEM implementations, DGX Spark, data-center DGX systems and DGX Cloud.

## Deployment boundaries

As checked on 2026-10-20, NVIDIA’s current product page directs customers to order DGX Station through OEM partners. The separate DGX Station for Windows announcement specifies expected availability in Q4 2026; that announcement does not establish general availability of the Windows configuration.

Confirm the particular OEM system’s OS, coherent-memory configuration, storage, networking, power and optional visualization GPU. Published model-capacity and compute figures remain NVIDIA claims subject to precision, sparsity, runtime and complete system configuration. Memory shared across the CPU and GPU is not interchangeable with an arbitrary discrete-GPU specification, and connecting multiple systems does not by itself establish application-level scaling. Region, delivery date, pricing and support require a current supplier check.

## Producer

- Produced by [NVIDIA](../../../producers/sub/n/sub/nvidia/README.md).

## Official resources

- [Current system and OEM options](https://www.nvidia.com/en-us/products/workstations/dgx-station/)
- [Windows configuration announcement, May 31, 2026](https://nvidianews.nvidia.com/news/nvidia-dgx-station-for-windows-puts-a-trillion-parameter-ai-supercomputer-on-every-enterprise-desk)
