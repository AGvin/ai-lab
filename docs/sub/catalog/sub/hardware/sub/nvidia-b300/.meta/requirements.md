# Documentation Requirements

## Requirements

- Identify NVIDIA B300 as the concrete Blackwell Ultra-generation data-center Tensor Core GPU product.
- Keep the B300 GPU distinct from Blackwell Ultra architecture concepts, HGX/DGX B300 systems, NVL72 rack-scale platforms, cloud instances, and CUDA/runtime software.
- Preserve memory, compute capability, supported numeric formats, interconnect, partitioning, power, and form-factor facts only at the applicable B300 product/SKU scope.
- Treat driver/runtime compatibility, support lifecycle, cloud availability, pricing, and workload performance as mutable facts requiring current verification.
- Render the standard `entity-relations` block and preserve NVIDIA as the producer.

## Validation

- B300 is not collapsed with B200 or complete Blackwell Ultra systems.
- System-specific specifications are not generalized to the individual GPU without evidence.
- The `produces` / `produced-by` relation pair resolves consistently to NVIDIA.
