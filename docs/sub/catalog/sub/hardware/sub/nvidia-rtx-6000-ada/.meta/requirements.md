# Documentation Requirements

## Requirements

- Identify NVIDIA RTX 6000 Ada Generation as a released professional PCIe workstation GPU based on Ada Lovelace with **48 GB ECC-capable GDDR6 VRAM**, distinct from the RTX A6000 Ampere, RTX PRO 6000 Blackwell 96 GB, and consumer GeForce RTX 4090 24 GB products.
- Preserve official exact-SKU form-factor, PCIe Gen 4 x16 interface, dual-slot active cooling and 300 W board power envelope; distinguish NVIDIA's workstation/virtualization licensing from ordinary local CUDA inference use.
- Scope driver lifecycle, supported CUDA versions, FP8 and other precision support, enterprise deployment, multi-GPU topology, virtualization and NVLink availability to documented hardware and software revision, not branding similarities.
- Do not equate 48 GB physical VRAM with usable model weight capacity independent of runtime, quantization, KV cache, context length, scratch memory and concurrent workloads.
- Attribute speed and energy comparisons to exact model/hardware/precision/runtime/host setup; peak vendor figures and unrelated rendering benchmarks are not universal LLM/VLM benchmarks.
- Preserve the canonical NVIDIA producer relation and inverse `produces`.

## Validation

- Ada workstation SKU is not confused with the Blackwell RTX PRO 6000 or consumer GeForce GPUs.
- 48 GB ECC-capable GDDR6 capacity and board envelope match the official exact product page.
- GPU feature and inference performance claims remain scoped and source-backed.
- Reciprocal NVIDIA producer provenance is present.
