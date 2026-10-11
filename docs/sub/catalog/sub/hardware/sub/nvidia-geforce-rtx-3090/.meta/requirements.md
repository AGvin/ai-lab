# Documentation Requirements

## Requirements

- Identify NVIDIA's released GeForce RTX 3090 consumer GPU based on Ampere, with 24 GB GDDR6X VRAM.
- Preserve the distinction from GeForce RTX 3090 Ti, RTX 4090, RTX 5090, Quadro/RTX professional parts, and whole-system products. The RTX 3090 exposes Ampere-generation Tensor Cores and a 24 GB memory capacity; do not confuse those with newer FP8/FP4 support on other GPU generations.
- The standard memory capacity refers to the exact manufacturer's SKU specification; non-standard modifications, shared system RAM, multiple device placement, CPU offload, model quantization, and tensor partitioning are separate deployment considerations.
- Keep current CUDA, kernel/runtime compatibility, driver lifecycle, power, cooling, used-market condition, NVLink configuration, host-slot requirements, availability and prices freshness-sensitive.
- Distinguish peak/vendor marketing throughput from measured model inference or fine-tuning performance; condition comparisons on precision/quantization, model, runtime, batching, context size, hardware/host configuration and power envelope.
- Preserve the NVIDIA producer relation and matching inverse `produces` link.

## Validation

- Product identity and VRAM capacity match the linked exact NVIDIA GeForce product page.
- The product is not conflated with other GeForce, workstation, cloud, or complete-system configurations.
- Unsupported inference-throughput claims are not imported from generic gaming benchmarks.
- Reciprocal NVIDIA provenance is present.
