# Documentation Requirements

## Requirements

- Identify NVIDIA Vera CPU as the concrete NVIDIA data-center CPU product for agentic AI, reinforcement learning, data processing, and host-CPU workloads.
- Keep the CPU product distinct from Vera CPU Rack, Vera Rubin NVL72, complete server/system platforms, hosted cloud instances, and the reusable architectural concepts behind Olympus cores or NVLink-C2C.
- Preserve core/thread, cache, memory, interconnect, power, form-factor, and confidential-computing facts only at the exact scope supported by current first-party documentation.
- Treat shipping status, partner deployments, benchmark claims, configuration ranges, cloud availability, pricing, and software support as freshness-sensitive.
- Render the standard `entity-relations` block and preserve NVIDIA as the producer.

## Validation

- The entity represents the Vera CPU hardware product rather than a rack or cloud service.
- Mutable deployment/performance claims remain source-attributed and time-scoped.
- The `produces` / `produced-by` relation pair resolves consistently to NVIDIA.

## Scoped original-source acceptance — 2026-11-06

- NVIDIA Vera CPU is an 88-core custom Olympus data-center CPU with a vendor-published peak 1.2 TB/s memory bandwidth, distinct from Vera CPU Rack (256 CPUs) and Vera Rubin NVL72. NVIDIA's August 2026 delivery report documents early customer systems and shipping, not universal availability. Rack aggregates, single-CPU memory capacity, workload speedups, confidential-computing support and power modes need exact configuration and software verification.
- Original manufacturer source 1: https://www.nvidia.com/en-us/data-center/vera-cpu/
- Original manufacturer source 2: https://blogs.nvidia.com/blog/vera-cpu-delivery/
- Original manufacturer source 3: https://www.nvidia.com/en-us/data-center/products/vera-rack/
- This original-source review does not certify current inventory, software/runtime support, independent benchmarks, general licensing/ownership clearance, full schema/CI/cache/render or physical device tests.
