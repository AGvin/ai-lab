# NVIDIA Groq 3 LPU

NVIDIA Groq 3 LPU is a chip-level language-processing inference accelerator integrated into the NVIDIA Groq 3 LPX rack-scale system.

## Hardware boundary

The LPU chip remains distinct from the complete LPX rack or system, GroqCloud, the independent Groq company, and generic LPU architecture concepts. NVIDIA's product uses licensed Groq technology, but that licensing relationship does not make Groq the producer of NVIDIA's concrete Groq 3 LPU. SRAM, bandwidth, interconnect, and accelerator specifications apply only at the chip scope supported by NVIDIA sources.

Production and shipping state, LPX rack composition, benchmark results, partner adoption, pricing, and deployment support are freshness-sensitive.

## Relations

- Produced by [NVIDIA](../../../producers/sub/n/sub/nvidia/).

## Official resources

- [NVIDIA Groq 3 LPX](https://www.nvidia.com/en-eu/data-center/lpx/)
- [NVIDIA Groq 3 LPX production announcement](https://nvidianews.nvidia.com/news/nvidia-groq-3-lpx-now-in-full-production-with-world-class-speed-for-agentic-ai)
- [NVIDIA Vera Rubin announcement](https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Vera-Rubin-Opens-Agentic-AI-Frontier/)

## Scoped original-source qualification — 2026-11-06

NVIDIA describes Groq 3 LPU as the chip inside NVIDIA Groq 3 LPX, not the complete rack or independent Groq's cloud service. Each LPU has 500 MB compiler-managed SRAM; NVIDIA's complete LPX rack comprises 256 LPUs, so rack totals and NVIDIA/third-party latency demonstrations cannot be assigned to a single LPU. NVIDIA announced LPX production in August 2026; individual chip procurement, model runtime and independently tested throughput remain unverified.

- Official source 1: https://developer.nvidia.com/blog/inside-nvidia-groq-3-lpx-the-low-latency-inference-accelerator-for-the-nvidia-vera-rubin-platform/
- Official source 2: https://nvidianews.nvidia.com/news/nvidia-groq-3-lpx-now-in-full-production-with-world-class-speed-for-agentic-ai

These manufacturer/source facts are not independent workload benchmarks, availability assurances, legal/ownership clearance or full schema/CI/cache/render and runtime verification.
