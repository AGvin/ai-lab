# Documentation Requirements

## Requirements

- Identify NVIDIA L4 as the released Ada Lovelace low-profile, single-slot server accelerator for energy-efficient LLM/vision inference, audio/video AI, transcoding and virtualization, with **24 GB GDDR6**, **300 GB/s** peak memory bandwidth and **72 W maximum TDP** per card.
- Preserve the **PCIe Gen4 x16, half-height/half-length single-slot, passively cooled** device boundary; qualified server airflow and accelerator/driver support matter, so physical low-profile geometry alone does not guarantee arbitrary consumer chassis/PSU compatibility.
- Distinguish NVIDIA L4 from NVIDIA L40S (48 GB GDDR6, 350 W class), A100/H100/H200 HBM accelerators, its T4 predecessor, virtual GPU partitions and hosted GPU cloud-instance bundles.
- Preserve NVIDIA's published fourth-generation Tensor Core, FP8 theoretical sparsity, hardware AV1 encode/decode and media execution boundaries; do not extrapolate vendor-reported AI-video pipeline multipliers into universal LLM speedups or mixed workload power savings.
- Keep effective quantized model fit, host CPU/network overhead, memory bandwidth bottlenecks, batch throughput, virtualization, driver/runtime compatibility, regional instance availability, price and support as mutable evidence-dependent deployment properties.
- Preserve NVIDIA source attribution and an exact reciprocal producer relation.

## Validation

- Published 24 GB, 300 GB/s and 72 W values are per physical L4 GPU, not aggregate server or cloud system memory.
- L4 remains distinct from L40S and hosted vGPU profiles.
- NVIDIA producer `produces` inverses this physical hardware identity.
