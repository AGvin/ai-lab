# Tenstorrent Wormhole n150/n300

**PROVENANCE/OWNERSHIP REVIEW PENDING.** See the [provenance policy](../../../../../project/sub/policies/sub/russia-linked-ai/).

Tenstorrent Wormhole n150/n300 is the released Wormhole-generation PCIe accelerator-card family documented in n150d, n150s, n300d and n300s variants.

Single- and dual-ASIC variants, cooling arrangements, memory, board power, dimensions and interconnect characteristics must be evaluated for the selected board. Follow the corresponding installation guide for chassis airflow, clearance, PCIe and power requirements; values for one variant are not family-wide specifications.

These PCIe boards remain distinct from Galaxy Wormhole systems, Galaxy Blackhole, Blackhole-generation hardware, TT-QuietBox/TT-LoudBox systems, cloud instances and TT-Metal/TT-Forge software. Recheck ordering availability, supported workloads, software compatibility and performance for the intended configuration. Documentation availability alone does not establish current stock or shipment timing.

## Relations

- Produced by: [Tenstorrent](../../../producers/sub/t/sub/tenstorrent/)

## Official resources

- <https://docs.tenstorrent.com/aibs/wormhole/>
- <https://open.tenstorrent.com/hardware/wormhole>

## Scoped original-source acceptance — 2026-11-05

Tenstorrent's Wormhole PCIe n150/n300 family includes n150d/n150s and n300d/n300s with distinct single/dual ASIC and active/passive cooling configurations. Current first-party installation requirements give PCIe 4.0 x16 host, up to 160 W for n150 boards versus up to 300 W for n300 boards, and host-airflow requirements for boards without an active cooling kit. Do not transfer one card's power, HBM/ASIC count, throughput or firmware support to the family or Galaxy systems. Deployment requires supported host, cabling, OS, TT-Metal/TT-Forge and validated models.

No hardware execution, repository-wide source freshness/schema/CI/cache/render, independent benchmark or ownership/legal clearance was performed.
