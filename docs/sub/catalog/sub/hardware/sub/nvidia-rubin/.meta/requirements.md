# Documentation Requirements

## Requirements

- Identify NVIDIA Rubin GPU as the concrete Rubin-generation data-center GPU component now in production.
- Keep the Rubin GPU distinct from Vera CPU, Vera Rubin NVL72, HGX/DGX Rubin systems, rack-scale platform identities, cloud instances, and CUDA/runtime software.
- Preserve memory technology/capacity, compute formats, interconnect, power, and other GPU facts only at the exact component scope supported by current first-party sources.
- Treat system shipping/ramp state, driver/runtime compatibility, cloud availability, pricing, and workload performance as mutable facts requiring current verification.
- Do not infer that every Vera Rubin system property is an intrinsic property of the Rubin GPU component.
- Render the standard `entity-relations` block and preserve NVIDIA as the producer.

## Validation

- Rubin GPU is not represented as Vera Rubin NVL72 or another complete system.
- Production status is backed by current first-party evidence and is not extrapolated to every downstream system configuration.
- The `produces` / `produced-by` relation pair resolves consistently to NVIDIA.

## Scoped original-source acceptance — 2026-11-06

- NVIDIA Rubin GPU is the individual Rubin-generation data-center GPU, not the Vera CPU or complete Vera Rubin NVL72 rack. NVIDIA's July 2026 engineering article describes up to 288 GB HBM4, 22 TB/s of bandwidth and up to 50 petaflops of NVFP4 per GPU. May full-production/ramp announcements apply to the platform supply chain; system comparisons and initial partner deliveries do not prove broad current stock or independent per-GPU application throughput.
- Original manufacturer source 1: https://developer.nvidia.com/blog/inside-nvidia-rubin-gpu-architecture-powering-the-era-of-agentic-ai/
- Original manufacturer source 2: https://nvidianews.nvidia.com/news/vera-rubin-full-production-agentic-ai-factory
- This original-source review does not certify current inventory, software/runtime support, independent benchmarks, general licensing/ownership clearance, full schema/CI/cache/render or physical device tests.
