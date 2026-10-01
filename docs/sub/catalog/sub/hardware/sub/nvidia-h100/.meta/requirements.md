# Documentation Requirements

## Requirements

- Identify NVIDIA H100 as NVIDIA's Hopper-architecture data-center Tensor Core GPU family for accelerated AI and HPC workloads.
- Keep the H100 hardware identity distinct from the Hopper architecture itself, from HGX/DGX systems that contain H100 GPUs, from cloud instance products, and from CUDA/TensorRT-LLM or other software/runtime identities.
- Preserve variant boundaries. Current first-party material distinguishes H100 SXM and H100 NVL/PCIe-class delivery with materially different memory, bandwidth, power, form factor, and interconnect characteristics; exact values must be attached to the applicable variant rather than generalized across the family.
- Treat driver/runtime compatibility, virtualization/MIG support, support lifecycle, cloud availability, pricing, and workload performance as mutable facts requiring current verification.
- When vendor performance comparisons are referenced, preserve workload, precision, sparsity, system-scale, latency, and other benchmark conditions and do not present vendor projections as neutral cross-vendor evidence.
- Render the standard `entity-relations` block from validated current-entity relations and preserve NVIDIA as the producer.
- Include current official H100 product and Hopper architecture references.

## Validation

- H100 is not collapsed with Hopper, H200, DGX/HGX systems, or hosted GPU instances.
- Variant-specific specifications remain scoped to the correct H100 form factor/SKU.
- Mutable software/support/performance claims are not presented as timeless hardware identity facts.
- The `produces` / `produced-by` relation pair resolves consistently to NVIDIA.
