# NVIDIA Jetson T5000

NVIDIA Jetson T5000 is the 128 GB production module in the Jetson Thor family for on-device robotics, multimodal inference and sensor processing. NVIDIA’s module specification identifies a Blackwell GPU, Arm CPU and LPDDR5X memory. It is distinct from the complete Jetson AGX Thor developer kit, Jetson T4000 and the IGX product line.

## Deployment boundaries

The published T5000 module table lists 273 GB/s memory bandwidth and a configurable 40–130 W power range. These are module specifications; the carrier board, storage, interfaces exposed by a finished system and its cooling solution require separate validation.

Choose a carrier and power/thermal design for the exact module and deployment. JetPack, CUDA, inference-engine versions and supported numeric formats must match the workload. NVIDIA peak FP4 compute or comparative efficiency figures do not establish application latency or model fit. Production availability, lifecycle commitments, regional supply and supported software combinations are mutable and should be checked against the current module documentation before deployment.

## Producer

- Produced by [NVIDIA](../../../producers/sub/n/sub/nvidia/README.md).

## Official resources

- [Thor module specifications](https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-thor/)
- [Module lifecycle](https://developer.nvidia.com/embedded/lifecycle)
