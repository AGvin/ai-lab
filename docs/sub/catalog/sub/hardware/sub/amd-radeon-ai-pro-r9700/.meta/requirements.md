# Documentation Requirements

## Requirements

- Identify AMD Radeon AI PRO R9700 as a released RDNA 4 workstation/local-AI GPU with 32 GB GDDR6, distinct from Radeon RX 7900 XTX 24 GB, AMD Instinct accelerator modules, and complete workstation systems.
- Preserve the actual 32 GB VRAM capacity, AI-accelerator generation, workstation deployment form factor, current drivers, board-vendor cooling and power requirements under the exact SKU boundary.
- Treat AMD ROCm/consumer graphics and kernel/backend support, supported Windows/Linux versions, inference runtime compatibility, supported precisions and model workload throughput as freshness-sensitive.
- Separate launch and availability of partner workstations from standalone GPU board retail availability; do not infer a current shop inventory or local price from the 2025 availability announcement.
- Keep model capacity and quantization conclusions tied to actual VRAM allocation, runtime, KV cache, context length and workload; nominal AI TOPS is not representative of LLM/VLM tokens/s.
- Preserve AMD as the canonical producer with the matching inverse `produces` relation.

## Validation

- The exact SKU and memory capacity match the official AMD product specification.
- Hardware form factors and system-level specifications are not mixed between workstations and datacenters.
- Driver compatibility and performance claims are constrained to the applicable release, environment and model workload.
- Producer provenance is reciprocal.
