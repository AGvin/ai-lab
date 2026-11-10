# Documentation Requirements

## Requirements

- Identify NVIDIA Jetson Orin Nano Super Developer Kit as NVIDIA's compact 8 GB edge-AI/robotics developer kit operated in the current Super performance configuration.
- Preserve the important identity boundary that existing Jetson Orin Nano Developer Kits can gain the Super performance mode through software/firmware updates; do not misrepresent Super as a wholly different production module silicon.
- Keep developer-kit carrier board/storage/I/O facts separate from production Jetson Orin Nano modules and from Jetson T4000/T5000 Thor modules.
- Treat current AI TOPS, memory bandwidth, CPU clocks, power modes, JetPack/Jetson Linux release support, CUDA/TensorRT/cuDNN versions, storage/install method, camera/video support, frameworks, and lifecycle as freshness-sensitive.
- Treat generative-AI benchmark graphs and model performance as NVIDIA-provided configuration-specific evidence rather than universal model/device throughput.
- Present a concise Official Resources block using the applicable official product-page, documentation and release-note references of this entity.

## Validation

- The node represents the sold developer-kit product/configuration, not a separate Super production module.
- Software-enabled Super performance is not generalized to unsupported module/carrier configurations.
- Producer provenance resolves to NVIDIA.

## Scoped original-source acceptance — 2026-11-05

- Official source: https://www.nvidia.com/en-eu/autonomous-machines/embedded-systems/jetson-orin/nano-super-developer-kit/
- NVIDIA Jetson Orin Nano Super Developer Kit combines an 8 GB LPDDR5 Ampere-based development module/carrier with a software-enabled Super mode (up to 67 INT8 TOPS, 102 GB/s specified memory bandwidth, 7–25 W published power modes). Eligible older Orin Nano development kits can be updated to Super; Super is not a wholly separate production-module silicon SKU. Model compatibility, available memory, JetPack/firmware, boot storage, thermals and actual throughput require current validation.
- Preserve SKU and chip-versus-system boundaries. Current runtime, model artifacts, availability, ownership/rights, robotics safety and deployment are not cleared by this source qualification. No full freshness/schema/CI/cache/render or physical testing performed.
