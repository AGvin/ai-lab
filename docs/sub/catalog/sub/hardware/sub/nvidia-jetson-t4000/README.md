# NVIDIA Jetson T4000

NVIDIA Jetson T4000 is a released 64 GB Blackwell production module for robotics and edge AI in the Jetson Thor family. NVIDIA announced its availability on January 5, 2026. It is a module rather than a complete developer kit and remains distinct from the 128 GB T5000, Jetson Orin products and the IGX line.

## Deployment boundaries

NVIDIA’s current module table lists 64 GB LPDDR5X memory, 273 GB/s memory bandwidth and a 40–70 W configurable power range. Use the T4000 column when sizing the deployment; specifications for the T5000 or AGX Thor developer kit do not automatically apply.

A working system also needs a compatible carrier, storage, power delivery, cooling and the appropriate JetPack/runtime stack. Numeric-format support and headline AI compute are conditional on the chosen software and precision. Measure representative model fit, sensor throughput and sustained latency rather than inferring them from peak compute. Check current lifecycle, distributor availability and supported software combinations for the intended production date.

## Producer

- Produced by [NVIDIA](../../../producers/sub/n/sub/nvidia/README.md).

## Official resources

- [Release announcement, January 5, 2026](https://nvidianews.nvidia.com/news/nvidia-releases-new-physical-ai-models-as-global-partners-unveil-next-generation-robots)
- [Thor module specifications](https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-thor/)
- [Module lifecycle](https://developer.nvidia.com/embedded/lifecycle)

## Scoped original-source qualification — 2026-11-06

NVIDIA Jetson T4000 is a released Blackwell-based 64 GB LPDDR5X production module, not the T5000 or a complete Jetson AGX Thor Developer Kit. NVIDIA lists 273 GB/s memory bandwidth, configurable 40-70 W module power, January 2026 availability and lifecycle through January 2036. An embedded system needs its own carrier, cooling, storage, drivers and real robotics inference validation; peak FP4 compute figures are precision/implementation-dependent.

- [Official source 1](https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-thor/)
- [Official source 2](https://nvidianews.nvidia.com/news/nvidia-releases-new-physical-ai-models-as-global-partners-unveil-next-generation-robots)
- [Official source 3](https://developer.nvidia.com/embedded/lifecycle)

Manufacturer specifications and performance claims are not independent workload tests, procurement clearance, complete software support matrices or full catalog validation. Verify exact configuration and current original sources before deployment.
