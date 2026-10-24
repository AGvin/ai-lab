# NVIDIA DGX Spark

NVIDIA DGX Spark is a compact, complete personal AI system built around the GB10 Grace Blackwell Superchip. Its role is local model development, inference, fine-tuning, agent execution and desktop experimentation; the product identity covers the system rather than a discrete GPU or the GB10 chip alone.

## Deployment boundaries

As checked on 2026-10-20, NVIDIA describes the existing 128 GB configuration and an announced 64 GB configuration. The latter is scheduled for partner availability on October 23, 2026, so it is not treated here as already shipping. Both configurations belong to DGX Spark; partner branding does not create an additional NVIDIA product identity.

DGX Station, DGX data-center systems and DGX Cloud have separate deployment and commercial boundaries. Confirm the selected system’s storage, networking, region, software image and support terms. NVIDIA model-size and compute guidance depends on precision, model, runtime and workload; unified-memory capacity or multi-system networking alone does not establish usable model capacity, latency or transparent memory pooling.

## Producer

- Produced by [NVIDIA](../../../producers/sub/n/sub/nvidia/README.md).

## Official resources

- [Product and configuration overview](https://www.nvidia.com/en-us/products/workstations/dgx-spark/)
- [64 GB configuration announcement, October 2, 2026](https://blogs.nvidia.com/blog/local-ai-dgx-spark-64gb-sync/)
