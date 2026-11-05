# Documentation Requirements

## Requirements

- Identify NVIDIA Groq 3 LPU as the chip-level language-processing inference accelerator integrated into the NVIDIA Groq 3 LPX rack-scale system.
- Keep the LPU hardware identity distinct from the complete LPX rack/system, GroqCloud, the independent Groq company, and generic LPU architecture concepts.
- Record the non-exclusive Groq technology-license context only as provenance context; do not infer that Groq is the producer of NVIDIA's concrete Groq 3 LPU product.
- Preserve SRAM, bandwidth, interconnect, and accelerator facts only at the chip scope supported by first-party NVIDIA sources.
- Treat production/shipping state, LPX rack composition, benchmark results, partner adoption, pricing, and deployment support as freshness-sensitive.
- Render the standard `entity-relations` block and preserve NVIDIA as the producer.

## Validation

- The canonical entity is the LPU chip, not the excluded LPX complete rack-scale system.
- Technology licensing from independent Groq is not represented as corporate ownership or producer substitution.
- The `produces` / `produced-by` relation pair resolves consistently to NVIDIA.

## Scoped original-source acceptance — 2026-11-06

- NVIDIA describes Groq 3 LPU as the chip inside NVIDIA Groq 3 LPX, not the complete rack or independent Groq's cloud service. Each LPU has 500 MB compiler-managed SRAM; NVIDIA's complete LPX rack comprises 256 LPUs, so rack totals and NVIDIA/third-party latency demonstrations cannot be assigned to a single LPU. NVIDIA announced LPX production in August 2026; individual chip procurement, model runtime and independently tested throughput remain unverified.
- Official source 1: https://developer.nvidia.com/blog/inside-nvidia-groq-3-lpx-the-low-latency-inference-accelerator-for-the-nvidia-vera-rubin-platform/
- Official source 2: https://nvidianews.nvidia.com/news/nvidia-groq-3-lpx-now-in-full-production-with-world-class-speed-for-agentic-ai
- This scoped qualification does not establish full freshness, general stock, vendor-neutral benchmarks, framework support, ownership/legal clearance, schema/CI/cache/render or physical hardware testing.
