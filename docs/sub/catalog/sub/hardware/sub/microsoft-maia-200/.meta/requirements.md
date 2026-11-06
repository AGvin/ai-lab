# Documentation Requirements

## Requirements

- Present Microsoft Maia 200 as Microsoft's second-generation first-party AI accelerator, purpose-built primarily for large-scale inference and already deployed in Microsoft's production datacenter fleet.
- Keep the hardware identity distinct from Azure/Microsoft Foundry service surfaces, datacenter systems, virtual-machine offerings, and the models that run on Maia 200.
- Preserve current architectural facts only when source-backed, including TSMC process, supported numeric formats, HBM capacity/bandwidth, on-chip SRAM, networking/topology, accelerator-scale figures, and deployment footprint.
- Treat throughput, performance-per-dollar, performance-per-watt, model workload examples, datacenter regions, customer availability, service exposure, and comparisons against competing accelerators as freshness-sensitive and benchmark-context-dependent.
- Do not infer public standalone hardware availability merely from Microsoft fleet deployment; distinguish internal/first-party deployment from customer-consumable Azure service surfaces.
- Include producer relations and official resources during scoped reader reconciliation. Repository-wide final rendering and cache/freshness certification remain separate final gates.

- Reconcile the reader with the source-backed identity, access and interpretation context in canonical `entity.identity_note`.
- Render the standard `entity-relations` block from the validated current-entity relation projection.

## Validation

- Maia 200 is not collapsed into Azure or Microsoft Foundry as a hosted service.
- Comparative performance claims retain their exact Microsoft-stated precision, workload, fleet, and time boundaries.
- Producer provenance resolves to Microsoft.

## Scoped original-source acceptance — 2026-11-05

- Original manufacturer source: https://blogs.microsoft.com/blog/2026/01/26/maia-200-the-ai-accelerator-built-for-inference/
- Microsoft Maia 200 is a Microsoft-fleet first-party inference accelerator with 216 GB HBM3e, 7 TB/s memory bandwidth, 272 MB on-chip SRAM, TSMC 3 nm silicon and a 750 W SoC TDP envelope. Microsoft's initial January 2026 deployment was US Central and its Maia SDK was a preview invitation, not general retail hardware availability or universal customer access. Reported per-dollar or competing-accelerator comparisons are manufacturer claims dependent on model, precision and fleet conditions, not independently benchmarked results.
- Preserve chip/card/system provenance and exact source limitations. No physical execution, current model/runtime benchmark, whole-catalog freshness/schema/CI/cache/render or full ownership/legal clearance was performed.
