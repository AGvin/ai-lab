# NVIDIA A100 80GB Tensor Core GPU

NVIDIA A100 80GB Tensor Core GPU is the 80 GB HBM2e Ampere data-center accelerator for AI training, inference and scientific computing. It is distinct from the A100 40 GB variant and from Hopper or Blackwell products. The catalog identity includes materially different PCIe and SXM implementations.

## Deployment boundaries

NVIDIA lists 1,935 GB/s memory bandwidth and 300 W maximum TDP for the 80 GB PCIe variant, versus 2,039 GB/s and a standard 400 W configuration for SXM. Specialized thermal SKUs may differ. The published partitioning limit is up to seven 10 GB MIG instances, subject to the applicable system and software.

SXM requires a compatible system baseboard; PCIe packaging does not by itself establish consumer-workstation compatibility. Verify cooling, power, firmware, interconnect topology and runtime support for the actual server. NVLink bandwidth and multi-GPU server capacity are not single-device memory specifications. Quantized model fit and sustained performance depend on the workload and software; Ampere does not inherit newer GPU numeric-format acceleration. Cloud allocation, licensing, price and support are separate mutable properties.

## Producer

- Produced by [NVIDIA](../../../producers/sub/n/sub/nvidia/README.md).

## Official resources

- [PCIe/SXM comparison and technical resources](https://www.nvidia.com/en-us/data-center/a100/)
