# NVIDIA GeForce RTX 3090

**PROVENANCE/OWNERSHIP REVIEW PENDING.** Manufacturer attribution does not complete ownership/control-chain review or establish adoption clearance. See the [provenance policy](../../../../../project/sub/policies/sub/russia-linked-ai/).

NVIDIA GeForce RTX 3090 is an Ampere desktop graphics card with 24 GB GDDR6X memory. For AI work it is a local compute device whose practical inference and development capacity depends on the model, precision and software stack. RTX 3090 Ti, later GeForce generations and professional RTX cards are separate products.

## Deployment boundaries

NVIDIA’s specifications distinguish the RTX 3090 from the Ti variant, including their different power requirements. Use the exact board vendor’s dimensions, connectors, cooling and PSU guidance, especially when evaluating a used card. An available product page does not establish current retail supply, warranty coverage or future driver support.

Ampere support does not imply the same accelerated numeric paths as Ada or Blackwell. Validate CUDA, framework and quantization compatibility before sizing a workload. The 24 GB figure is physical memory per card; model weights, cache and runtime allocations share it. NVLink support does not automatically expose multiple cards as one memory allocation: application parallelism and topology remain separate requirements. Gaming or rendering results are not LLM performance evidence.

## Producer

- Produced by [NVIDIA](../../../producers/sub/n/sub/nvidia/README.md).

## Source interpretation

The manufacturer identifies this as the desktop Ampere RTX 3090 with 24 GB GDDR6X, distinct from RTX 3090 Ti and professional RTX A6000. Card memory is per device. Board-specific power, cooling, connector and driver requirements still apply; NVLink does not make arbitrary applications pool memory. Historical product-page presence does not prove current retail supply or warranty.

This bounded source review does not establish current pricing, local availability, full specification freshness, software entitlements or measured performance. No hardware or runtime validation was performed.

## Official resources

- [RTX 3090 family and per-model specifications](https://www.nvidia.com/en-eu/geforce/graphics-cards/30-series/rtx-3090/)
