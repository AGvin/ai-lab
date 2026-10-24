# Documentation Requirements

## Requirements

- Identify AMD Ryzen AI Max+ 395 as the concrete non-PRO Strix Halo Ryzen AI Max 300-series processor for laptops/desktops with CPU, integrated Radeon graphics, NPU, and shared-memory system architecture relevant to local AI workloads.
- Preserve the exact 395 SKU boundary separately from Ryzen AI Max+ PRO 395, lower Max/Max PRO SKUs, complete OEM systems, and cloud instances.
- Treat CPU/GPU/NPU configuration, maximum supported memory and memory allocation behavior, memory bandwidth, AI TOPS, supported numeric formats, TDP/cTDP, driver/runtime support, ROCm/DirectML/ONNX compatibility, firmware, and OEM implementation limits as freshness-sensitive.
- Do not infer usable model size from nominal system memory alone; exact OS reservation, GPU allocation, runtime/precision, KV cache, context, and application overhead matter.
- Attribute AMD AI-performance/efficiency claims to AMD and avoid unmatched cross-vendor ranking.

## Validation

- The node remains one concrete processor SKU rather than a laptop/workstation system.
- PRO-only features are not copied onto the non-PRO SKU.
- Local-model fit claims remain configuration-specific.
