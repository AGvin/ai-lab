# Documentation Requirements

## Requirements

- Identify NVIDIA's released GeForce RTX 4090 consumer GPU based on Ada Lovelace, with 24 GB GDDR6X VRAM.
- Distinguish this exact 24 GB Ada Lovelace GPU from Ampere RTX 3090, Blackwell RTX 5090, professional RTX 6000 variants, and RTX 4090-branded complete systems. Do not infer multi-GPU VRAM sharing or NVLink support from other NVIDIA GPUs.
- The standard memory capacity refers to the exact manufacturer's SKU specification; non-standard modifications, shared system RAM, multiple device placement, CPU offload, model quantization, and tensor partitioning are separate deployment considerations.
- Treat CUDA/kernel compatibility, power connectors and thermal limits, power supply and PCIe/host fit, workload performance, secondhand availability, and retail price as configuration-dependent and freshness-sensitive.
- Distinguish peak/vendor marketing throughput from measured model inference or fine-tuning performance; condition comparisons on precision/quantization, model, runtime, batching, context size, hardware/host configuration and power envelope.
- Preserve the NVIDIA producer relation and matching inverse `produces` link.
- Present a concise Official Resources block using the applicable official product-page, documentation and release-note references of this entity.

## Validation

- Product identity and VRAM capacity match the linked exact NVIDIA GeForce product page.
- The product is not conflated with other GeForce, workstation, cloud, or complete-system configurations.
- Unsupported inference-throughput claims are not imported from generic gaming benchmarks.
- Reciprocal NVIDIA provenance is present.

## Scoped source interpretation — 2026-11-05

- Render the exact product/configuration and source-specific deployment distinctions from the current entity note.
- Do not transfer system totals, toolkit-specific requirements or family/edition claims to an individual GPU.
- Keep ownership/control review pending. This bounded identity/source qualification is not a full freshness audit, OEM compatibility approval, benchmark or software-license entitlement.
