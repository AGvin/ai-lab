# Documentation Requirements

## Requirements

- Identify NVIDIA A100 **80GB** as the released Ampere-generation datacenter accelerator with 80 GB HBM2e; distinguish it from the original 40 GB SKU and later H100/B200 GPUs.
- Preserve the form-factor split: A100 80GB PCIe and A100 80GB SXM have different power, memory bandwidth, thermal envelope, multi-GPU topology and integration requirements. Do not assume consumer desktop compatibility or interchangeable NVLink systems.
- Treat MIG partitioning (up to seven accelerator instances), supported CUDA/drivers, BF16/FP16/TF32/INT8, software/runtime matrix and deployment host requirements as hardware/release-specific and current where mutable.
- Separate physical GPU memory from aggregated node memory, MIG memory partitions, host RAM offload or model quantization. Ampere-generation precision support must not be assumed to provide Blackwell-generation FP4 behavior.
- Attribute measured inference speed and training benchmark results to exact hardware form factor, model, precision, inference runtime, batch, power and test methodology, not vendor peak compute figures.
- Preserve reciprocal NVIDIA producer attribution.

## Validation

- The exact 80 GB SKU is distinguished from A100 40 GB and newer datacenter GPUs.
- PCIe versus SXM support/thermal requirements are not conflated.
- NVIDIA `produces` inverses the `produced-by` relation.
