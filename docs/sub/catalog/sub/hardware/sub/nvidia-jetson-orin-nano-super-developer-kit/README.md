# NVIDIA Jetson Orin Nano Super Developer Kit

NVIDIA Jetson Orin Nano Super Developer Kit is an 8 GB Ampere-based development kit for local generative AI, vision and robotics prototyping. “Super” includes a software-enabled performance mode available to compatible existing Orin Nano developer kits; it does not establish a new production-module silicon identity.

## Deployment boundaries

NVIDIA lists 8 GB LPDDR5 memory, 102 GB/s memory bandwidth and a 7–25 W power range for the Super kit. Published theoretical compute depends on precision and sparsity and does not establish general LLM throughput. The developer kit includes a carrier-board environment; storage media, expansion devices and a production carrier require their own configuration decisions.

Confirm the required JetPack/firmware upgrade, power supply, cooling, boot storage and peripheral compatibility in the current user guide. Choose inference precision and runtime for the model, and budget memory for activations and cache as well as weights. Developer-kit availability and support do not substitute for production-module lifecycle commitments. Do not transfer specifications from AGX Orin, Orin NX or Thor modules to this kit.

## Producer

- Produced by [NVIDIA](../../../producers/sub/n/sub/nvidia/README.md).

## Official resources

- [Product and Super upgrade overview](https://www.nvidia.com/en-eu/autonomous-machines/embedded-systems/jetson-orin/nano-super-developer-kit/)
- [Developer-kit user guide](https://docs.nvidia.com/jetson/orin-nano-devkit/user-guide/latest/index.html)
