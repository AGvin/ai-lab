# Documentation Requirements

## Requirements

- Identify NVIDIA Jetson T5000 as the current 128 GB production module in the Jetson Thor / Jetson AGX Thor series for physical-AI, robotics, and edge-AI systems.
- Keep the production module distinct from the Jetson AGX Thor Developer Kit, Jetson T4000, IGX Thor/T5000 products, discrete RTX/Blackwell GPUs, and complete partner systems.
- Preserve module-level Blackwell GPU, Arm CPU, memory, power-envelope, AI-performance, I/O, lifecycle, and form-factor facts only at the exact T5000 scope and from current first-party documentation.
- Treat JetPack/Jetson Linux support, CUDA/TensorRT/cuDNN versions, camera/video support, SDK compatibility, regional SKUs, availability, pricing, and benchmark results as freshness-sensitive deployment facts.
- Do not transfer developer-kit storage, carrier-board I/O, peripherals, or dGPU assumptions to the production module.
- Attribute NVIDIA performance/efficiency comparisons to NVIDIA and preserve the compared generation/power/software configuration.
- Present a concise Official Resources block using the applicable official product-page, documentation and release-note references of this entity.

## Validation

- The node remains the T5000 production module rather than the developer kit or generic Jetson Thor family.
- Module specifications and software support are not generalized to Jetson T4000.
- Producer provenance resolves to NVIDIA.

## Scoped original-source acceptance — 2026-11-06

- NVIDIA Jetson T5000 is a 128 GB LPDDR5X Blackwell production module with 273 GB/s published memory bandwidth and 40-130 W configurable module power. It differs from the 64 GB T4000 and the complete AGX Thor Developer Kit (carrier, storage and exposed I/O). NVIDIA lists its commercial-module lifecycle through August 2035. JetPack support, peripheral integration, power/cooling and actual model latency require exact-module validation.
- Original manufacturer source 1: https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-thor/
- Original manufacturer source 2: https://developer.nvidia.com/embedded/lifecycle
- This original-source review does not certify current inventory, software/runtime support, independent benchmarks, general licensing/ownership clearance, full schema/CI/cache/render or physical device tests.
