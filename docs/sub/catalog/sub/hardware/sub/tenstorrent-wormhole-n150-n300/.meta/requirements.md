# Documentation Requirements

## Requirements

- Present Tenstorrent Wormhole n150/n300 as Tenstorrent's released Wormhole-generation PCIe accelerator-card family represented by the current n150d/n150s/n300d/n300s product variants.
- Preserve variant boundaries for single- versus dual-ASIC topology, active versus passive cooling, memory capacity, board power, dimensions, and interconnect characteristics; do not generalize one variant's values to the entire family.
- Keep the Wormhole accelerator-card family distinct from Galaxy Wormhole systems, Galaxy Blackhole, Blackhole-generation cards/systems, TT-QuietBox/TT-LoudBox systems, cloud instances, TT-Metal/TT-Forge software, and reusable Tensix architecture concepts.
- Treat pricing, stock/shipping status, validated models, software compatibility, benchmarks, and product variants as freshness-sensitive.
- Render the standard `entity-relations` block from validated current-entity relations.

## Validation

- Current product availability and variant names resolve to Tenstorrent first-party product/documentation surfaces.
- Producer provenance resolves bidirectionally to Tenstorrent.
- The entity does not conflate Wormhole PCIe boards with Galaxy systems or Blackhole-generation hardware.

## Scoped original-source acceptance — 2026-11-05

- Original manufacturer source: https://docs.tenstorrent.com/aibs/wormhole/installation.html
- Tenstorrent's Wormhole PCIe n150/n300 family includes n150d/n150s and n300d/n300s with distinct single/dual ASIC and active/passive cooling configurations. Current first-party installation requirements give PCIe 4.0 x16 host, up to 160 W for n150 boards versus up to 300 W for n300 boards, and host-airflow requirements for boards without an active cooling kit. Do not transfer one card's power, HBM/ASIC count, throughput or firmware support to the family or Galaxy systems. Deployment requires supported host, cabling, OS, TT-Metal/TT-Forge and validated models.
- Preserve exact SKU, chip/card/system, host memory and runtime boundaries; source acceptance alone is not a complete availability, model execution, benchmark, ownership/legal or final schema/CI/cache/renderer audit.
