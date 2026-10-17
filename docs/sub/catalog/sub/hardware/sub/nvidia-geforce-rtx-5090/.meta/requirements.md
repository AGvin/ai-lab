# Documentation Requirements

## Requirements

- Identify NVIDIA's released GeForce RTX 5090 consumer GPU based on Blackwell, with 32 GB GDDR7 VRAM.
- Distinguish the exact 32 GB consumer GeForce SKU from RTX 5080/5070 variants, RTX PRO 6000 Blackwell workstation/server editions, and NVIDIA GB10/DGX Spark systems. Its 32 GB GDDR7 VRAM and Blackwell GPU generation must not be projected onto other models.
- The standard memory capacity refers to the exact manufacturer's SKU specification; non-standard modifications, shared system RAM, multiple device placement, CPU offload, model quantization, and tensor partitioning are separate deployment considerations.
- Treat CUDA/kernel/runtime support, driver branches, FP4/FP8 availability in specific inference stacks, board-vendor power connectors and coolers, host fit, regional availability, pricing, and measured LLM/VLM performance as freshness-sensitive.
- Distinguish peak/vendor marketing throughput from measured model inference or fine-tuning performance; condition comparisons on precision/quantization, model, runtime, batching, context size, hardware/host configuration and power envelope.
- Preserve the NVIDIA producer relation and matching inverse `produces` link.

## Validation

- Product identity and VRAM capacity match the linked exact NVIDIA GeForce product page.
- The product is not conflated with other GeForce, workstation, cloud, or complete-system configurations.
- Unsupported inference-throughput claims are not imported from generic gaming benchmarks.
- Reciprocal NVIDIA provenance is present.
