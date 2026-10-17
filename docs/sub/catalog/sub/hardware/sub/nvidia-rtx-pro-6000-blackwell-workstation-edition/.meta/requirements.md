# Documentation Requirements

## Requirements

- Identify NVIDIA RTX PRO 6000 Blackwell Workstation Edition as the concrete active-cooled workstation GPU in the RTX PRO 6000 Blackwell family.
- Preserve the Workstation Edition boundary separately from Server Edition and Max-Q Workstation Edition, which differ materially in thermal design, power, and intended deployment despite sharing 96 GB GDDR7 ECC memory.
- Treat GPU memory/bandwidth, Tensor/RT/CUDA core generations, FP4/FP8/BF16/FP16 support, PCIe, display/encode features, power, form factor, MIG/virtualization support, driver branch, CUDA/TensorRT/runtime support, and application certification as freshness-sensitive.
- Keep complete workstation/server products, cloud instances, RTX PRO Server platforms, and Blackwell architecture concepts with their own owners.
- Do not infer LLM/VLM throughput solely from memory capacity or vendor AI TOPS; runtime, precision, batch/context, kernels, power, and host configuration materially affect results.

## Validation

- The node remains the exact Workstation Edition GPU rather than the whole RTX PRO 6000 family.
- Server/Max-Q specifications are not transferred to this SKU.
- Performance claims remain workload/configuration scoped.
