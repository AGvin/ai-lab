# Documentation Requirements

## Requirements

- Identify NVIDIA B200 as the concrete Blackwell-generation data-center Tensor Core GPU product.
- Keep the B200 GPU distinct from the Blackwell architecture concept, GB200 superchip identity, HGX/DGX systems, NVL72 rack systems, cloud instances, and CUDA/TensorRT software.
- Preserve memory, compute capability, supported numeric formats, partitioning/MIG, interconnect, power, and form-factor facts only at the applicable B200 product/SKU scope.
- Treat driver/runtime compatibility, support lifecycle, cloud availability, pricing, and workload performance as mutable facts requiring current verification.
- Render the standard `entity-relations` block and preserve NVIDIA as the producer.

## Validation

- B200 is not collapsed with GB200, HGX/DGX Blackwell systems, or generic Blackwell architecture.
- Variant- or system-specific specifications are not generalized to the GPU without source support.
- The `produces` / `produced-by` relation pair resolves consistently to NVIDIA.
