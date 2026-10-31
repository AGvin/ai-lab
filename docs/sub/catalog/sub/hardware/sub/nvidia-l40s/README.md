# NVIDIA L40S GPU

NVIDIA L40S is an Ada Lovelace server GPU for AI inference and training, graphics and media workloads. NVIDIA specifies 48 GB ECC GDDR6 memory, PCIe Gen4 x16, passive cooling and 350 W maximum power. This is a physical data-center accelerator rather than an actively cooled RTX 6000 Ada workstation card.

## Deployment boundaries

The L40S specification lists no NVLink or MIG support. Its FP8 Tensor Core and media capabilities need workload-appropriate software; vendor theoretical compute includes stated sparsity conditions. Published video, rendering and LLM examples are workload-specific evidence rather than universal speedups.

A passive card needs qualified server airflow, power delivery and physical clearance. Check the exact server, firmware, driver, inference engine and virtualization configuration. The 48 GB memory figure is per physical device and must accommodate weights, cache and runtime overhead; a multi-card server does not automatically pool it. Distinguish L40S from L4, HBM-based accelerators and cloud/vGPU bundles. Software licensing, provider limits, current availability, support and pricing remain separate deployment questions.

## Producer

- Produced by [NVIDIA](../../../producers/sub/n/sub/nvidia/README.md).

## Official resources

- [Product and full GPU specifications](https://www.nvidia.com/en-us/data-center/l40s/)
