# Documentation Requirements

## Requirements

- Identify AMD Instinct MI455X as the concrete released MI400 Series data-center GPU product based on AMD's CDNA 5 generation.
- Keep the MI455X GPU distinct from AMD Helios rack-scale systems/reference designs, from CDNA 5 architecture concepts, cloud instances, and ROCm/runtime software.
- Preserve HBM4 memory, bandwidth, supported numeric formats, interconnect, power, and other product facts only at the applicable product/SKU scope and from current first-party sources.
- Treat system integration, driver/runtime compatibility, support lifecycle, availability, pricing, and workload performance as mutable facts requiring current verification.
- Render the standard `entity-relations` block and preserve Advanced Micro Devices, Inc. as the producer.

## Validation

- MI455X is not represented as the Helios system itself or as a generic MI400 family synonym.
- Announced future MI400 products are not implicitly treated as released because MI455X is released.
- The `produces` / `produced-by` relation pair resolves consistently to AMD.
