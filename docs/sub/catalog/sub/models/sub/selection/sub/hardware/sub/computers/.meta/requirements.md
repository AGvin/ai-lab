# Documentation Requirements

## Requirements

- Cover interactive general-purpose laptops, desktops, gaming PCs, creator/workstation-class personal machines, and mini PCs used as personal compute rather than dedicated servers.
- Route by the **effective local AI compute ecosystem**, not OEM: `apple/`, `nvidia/`, `amd/`, `intel/`, `qualcomm/`, or `cpu/`.
- When multiple accelerators exist, choose the child for the accelerator/runtime actually intended for inference; e.g. an Intel-CPU PC using an NVIDIA GPU follows `nvidia/`.
- Compare exact usable memory/headroom, runtime/backend support, artifact/quantization, context/cache, display/application contention, power/thermals, and measured performance.
- Keep GPU/PC purchasing outside; first measure the existing machine and identify a real capability/resource gap.

## Validation

- Direct children are the six selected compute routes.
- Workstation branding does not create a separate hardware class by itself.
- Integrated NPU/GPU presence is not treated as useful unless the intended runtime/model actually supports it.
