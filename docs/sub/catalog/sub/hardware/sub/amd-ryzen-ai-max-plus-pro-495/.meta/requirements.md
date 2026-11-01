# Documentation Requirements

## Requirements

- Identify the released AMD Ryzen AI Max+ PRO 495 processor as a commercial Gorgon Halo Ryzen AI Max PRO 400-series SKU with 16 Zen 5 cores / 32 threads, 40-CU Radeon 8065S (RDNA 3.5), and an AMD XDNA 2 NPU with up to 55 vendor NPU TOPS.
- Preserve distinctions from the non-PRO Ryzen AI Max+ 395 (Strix Halo, Radeon 8060S, up to 128 GB) and from the full Ryzen AI Halo 192 GB developer system, partner PCs, 490/485 lower PRO SKUs and separate GPU cards.
- Source the processor's 256-bit LPDDR5x-8533 supported memory interface and **up to 192 GB system memory**, 55 W default TDP and configurable 45–120 W to the exact AMD SKU page. These are processor specifications: they are not guaranteed assembled-system options or dedicated GPU VRAM, nor a measured system power draw.
- Distinguish dynamic/carved-out Radeon graphics memory from total unified system memory and account for CPU/OS reservations, model weights, KV cache, batch/context size, model quantization, drivers and inference runtime. Do not represent vendor 160 GB graphics allocation and 300B-model fit claims as independent benchmarks.
- AMD's ROCm documentation identifies Radeon 8065S as RDNA 3.5 / `gfx1151` and lists this APU in ROCm 10.1.0 supported hardware; verify applicable per-release OS/kernel requirements and software features. The integrated NPU is a separate compute engine, not automatically an acceleration target for GPU-specific ROCm engines.
- Respect mutable commercial/PRO manageability support, OEM firmware and memory configurations, OS compatibility, GPU/CPU power limits, driver availability, model software support, stock/pricing and security advisories. Do not infer real measured throughput, data residency, ultimate beneficial ownership or Russian partial ownership clearance from branding.
- Keep one direct `produced-by` AMD relation and the exact reciprocal producer `produces` edge. Keep official references to AMD's processor specs, announced availability and ROCm support.

## Validation

- Exactly one original 495 processor identity, not an extra whole-system or model/software/service entity.
- 192 GB is a processor-supported shared system-memory ceiling, not a claim of 192 GB GPU memory.
- Producer reciprocal relation, local reader navigation and source-claim boundaries resolve.
- Source-backed scoped documentation checks do not imply executed local AI workloads, whole-catalog render/CI, full owner-control review or a completed clean research pass.
