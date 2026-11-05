# NVIDIA GeForce RTX 5090

**PROVENANCE/OWNERSHIP REVIEW PENDING.** Manufacturer attribution does not complete ownership/control-chain review or establish adoption clearance. See the [provenance policy](../../../../../project/sub/policies/sub/russia-linked-ai/).

NVIDIA GeForce RTX 5090 is a Blackwell desktop graphics card with 32 GB GDDR7 memory. Its local AI role is model development and inference within the capacity of the card, host and selected software. It is distinct from RTX PRO 6000 Blackwell, DGX Spark/GB10 and hosted GPU services.

## Deployment boundaries

The physical 32 GB memory capacity is per GPU, not an assured model-weight budget: cache, activations and runtime allocations also consume it. Blackwell FP4/FP8 capability requires compatible kernels, model formats and driver/runtime versions; theoretical AI compute does not predict end-to-end LLM latency.

Use the exact board specification to confirm chassis clearance, power delivery, connector fit and cooling. Host CPU, PCIe topology and data movement can affect sustained throughput. Multi-GPU operation needs an explicit parallelism strategy rather than an assumption of transparent memory pooling. Compare performance only with matched models, precision, context length, batch size and software. Region, price, retail availability, warranty and current software compatibility require current verification.

## Producer

- Produced by [NVIDIA](../../../producers/sub/n/sub/nvidia/README.md).

## Source interpretation

The manufacturer identifies the desktop Blackwell RTX 5090 with 32 GB GDDR7. Keep laptop variants, RTX PRO models and complete multi-GPU systems separate. GPU memory must also hold runtime allocations and cache; gaming/AI TOPS marketing does not measure a particular LLM. Verify the chosen board's power, cooling and runtime support.

This bounded source review does not establish current pricing, local availability, full specification freshness, software entitlements or measured performance. No hardware or runtime validation was performed.

## Official resources

- [Product and system requirements](https://www.nvidia.com/en-us/geforce/graphics-cards/50-series/rtx-5090/)
