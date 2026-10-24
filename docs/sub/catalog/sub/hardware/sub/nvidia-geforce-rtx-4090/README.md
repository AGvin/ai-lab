# NVIDIA GeForce RTX 4090

NVIDIA GeForce RTX 4090 is an Ada Lovelace desktop graphics card with 24 GB GDDR6X memory. It can serve as local AI compute when the model and runtime fit the card and host. The identity is separate from RTX 3090, RTX 5090, professional RTX products and cloud instances containing these GPUs.

## Deployment boundaries

The 24 GB specification applies to each physical GPU and includes memory needed by weights, activations, attention cache and the runtime. A multi-card system does not provide an automatically pooled memory space; RTX 3090 NVLink capabilities must not be transferred to the RTX 4090.

Verify the exact board’s dimensions, cooling, power connector and PSU requirements together with the host’s PCIe arrangement. CUDA, driver, inference-engine and quantization support must be checked for the chosen versions. Ada Tensor Core features alone do not establish acceleration for every operator or model. Published gaming, graphics and theoretical compute results are not measured LLM throughput. Availability, support, pricing and any cloud provider’s instance limits are mutable deployment facts.

## Producer

- Produced by [NVIDIA](../../../producers/sub/n/sub/nvidia/README.md).

## Official resources

- [Product and system requirements](https://www.nvidia.com/en-us/geforce/graphics-cards/40-series/rtx-4090/)
