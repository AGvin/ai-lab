# Documentation Requirements

## Requirements

- Present Intel Gaudi 3 as Intel's current third-generation Gaudi AI accelerator hardware family/product identity, including released PCIe/OAM/system forms without splitting every board/system configuration into a peer identity by default.
- Preserve exact accelerator form factor/SKU, accelerator count, HBM capacity/bandwidth, supported precisions, networking/topology, software release, model artifact, workload, context, batch/concurrency, and benchmark methodology whenever performance/model-fit claims are recorded.
- Treat comparative performance, software/runtime support, pricing, availability, partner systems, and benchmark numbers as freshness- and configuration-sensitive.
- Render the standard `entity-relations` block from validated current-entity relations.

## Validation

- Hardware facts resolve to current Intel first-party product/technical sources.
- Producer provenance resolves to Intel.

## Scoped original-source acceptance — 2026-11-05

- Original manufacturer source: https://www.intel.com/content/www/us/en/content-details/817488/intel-gaudi-3-ai-accelerator-hl-338-pcie-add-in-card-product-brief.html
- Intel Gaudi 3 is an accelerator product family with configuration-specific packaging. Official HL-338 PCIe 5.0 x16 card documentation specifies 128 GB HBM2e with 3.7 TB/s peak bandwidth, 96 MB SRAM and 600 W air-cooled card TDP; a four-card top-board topology is not one accelerator's memory. Other Gaudi 3 OAM/system forms have different thermal and topology envelopes. Intel model/runtime support, actual throughput, ownership and legal clearance remain unverified.
- Preserve chip/card/system provenance and exact source limitations. No physical execution, current model/runtime benchmark, whole-catalog freshness/schema/CI/cache/render or full ownership/legal clearance was performed.
