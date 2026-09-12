# Documentation Requirements

## Requirements

- Identify NVIDIA Rubin GPU as the concrete Rubin-generation data-center GPU component now in production.
- Keep the Rubin GPU distinct from Vera CPU, Vera Rubin NVL72, HGX/DGX Rubin systems, rack-scale platform identities, cloud instances, and CUDA/runtime software.
- Preserve memory technology/capacity, compute formats, interconnect, power, and other GPU facts only at the exact component scope supported by current first-party sources.
- Treat system shipping/ramp state, driver/runtime compatibility, cloud availability, pricing, and workload performance as mutable facts requiring current verification.
- Do not infer that every Vera Rubin system property is an intrinsic property of the Rubin GPU component.
- Render the standard `entity-relations` block and preserve NVIDIA as the producer.

## Validation

- Rubin GPU is not represented as Vera Rubin NVL72 or another complete system.
- Production status is backed by current first-party evidence and is not extrapolated to every downstream system configuration.
- The `produces` / `produced-by` relation pair resolves consistently to NVIDIA.
