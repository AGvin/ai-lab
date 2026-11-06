# Documentation Requirements

## Requirements

- Identify AMD Instinct MI355X as the concrete MI350 Series data-center GPU product for accelerated AI and HPC workloads.
- Keep the MI355X GPU distinct from the eight-GPU MI355X Platform/system, from CDNA 4 architecture concepts, from cloud instances, and from ROCm/runtime software.
- Preserve product/SKU facts such as memory, bandwidth, supported numeric formats, interconnect, power, and form factor only at the applicable MI355X scope and from current first-party sources.
- Treat driver/runtime compatibility, support lifecycle, cloud availability, pricing, and workload performance as mutable facts requiring current verification.
- Render the standard `entity-relations` block and preserve Advanced Micro Devices, Inc. as the producer.

## Validation

- MI355X is not collapsed with MI350X, the MI355X Platform, or generic CDNA 4 hardware.
- Vendor performance claims preserve workload and system conditions and are not presented as neutral cross-vendor conclusions.
- The `produces` / `produced-by` relation pair resolves consistently to AMD.

## Scoped source interpretation — 2026-11-05

- Render the SKU and original-source discrepancy context from entity.identity_note. Prefer product and architecture evidence for HBM3E and exact SKU identity over copied acceptance-guide wording.
- Keep manufacturer attribution separate from pending ownership/control review. No full freshness audit or operational compatibility claim is implied.
