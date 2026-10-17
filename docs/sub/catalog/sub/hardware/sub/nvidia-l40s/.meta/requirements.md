# Documentation Requirements

## Requirements

- Identify NVIDIA L40S as a released Ada Lovelace data-center GPU with **48 GB ECC-capable GDDR6**, designed for GPU AI/LLM inference, training, multimodal workflows, rendering, graphics and media workloads. Keep it distinct from the workstation RTX 6000 Ada and from new NVIDIA Blackwell workstation/server cards.
- Preserve its PCIe datacenter deployment, passive system-cooled server configuration, up to **350 W maximum power**, tensor-core FP8 support, graphics/video accelerators and GPU memory boundaries according to NVIDIA's source-backed product specification.
- Distinguish a single card's 48 GB from a multi-GPU machine's aggregate memory, CPU RAM and VRAM across model parallelism configurations; a model needing more than one GPU's memory may require sharding and communication, not merely multiple independently addressed cards.
- Preserve pricing/availability, instance access, vGPU/virtualization support, driver/CUDA framework compatibility and model-specific throughput as mutable release/environment facts.
- Do not extrapolate FP8 Tensor Core theoretical sparsity numbers to actual throughput across quantizations, batching, runtimes, multimodal and graphics workloads.
- Keep NVIDIA producer provenance reciprocal without representing CUDA/TensorRT/runtime stacks as part of the physical hardware entity.

## Validation

- L40S is not confused with RTX 6000 Ada or newer RTX PRO products merely because they share related GPU architecture and memory size.
- Its 48 GB memory and maximum system power are scoped to the actual datacenter GPU product.
- NVIDIA `produces` reciprocates this hardware identity.
