# Documentation Requirements

## Requirements

- Cover Radeon/Ryzen-AI personal computers when AMD GPU/APU/NPU acceleration is the intended local path.
- Begin with exact hardware and OS support matrix: GPU/APU generation, Windows/Linux/WSL, ROCm/Radeon Software/Windows ML or other backend, runtime version, and model precision/export.
- Do not transfer Linux ROCm support to native Windows, datacenter Instinct support to consumer Radeon, or one Radeon generation to another without current official evidence.
- Distinguish GPU, NPU, and CPU execution and record fallback/partition behavior when a model cannot remain on the intended accelerator.
- Measure usable memory/headroom, context/cache, latency/throughput, sustained thermals/power, and task quality for the exact runtime/artifact.
- Mark unsupported or unverified combinations Unknown instead of estimating fit from theoretical compute or VRAM alone.

## Validation

- OS/hardware/runtime matrix is explicit.
- Consumer Radeon/Ryzen AI and Instinct server routes remain distinct.
- The page does not imply ROCm support where AMD does not currently document it.
