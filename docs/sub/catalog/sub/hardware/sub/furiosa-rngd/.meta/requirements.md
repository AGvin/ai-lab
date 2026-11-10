# Documentation Requirements

## Requirements

- Identify RNGD as FuriosaAI's second-generation neural-processing accelerator for LLM, multimodal, and vision inference.
- Keep the accelerator identity distinct from complete server systems, hosted inference services, and generic Tensor Contraction Processor architecture concepts.
- Preserve memory capacity/bandwidth, supported numeric formats, form factor, power envelope, and virtualization features only at the exact product scope supported by first-party documentation.
- Treat availability, production/shipping state, benchmark performance, software/runtime support, and deployment packaging as freshness-sensitive.
- Render the standard `entity-relations` block from validated current-entity relations.

## Validation

- RNGD remains a concrete hardware-product identity.
- Producer provenance resolves to FuriosaAI.

## Scoped original-source acceptance — 2026-11-06

- FuriosaAI RNGD is a 48 GB HBM3 PCIe Gen5 x16 inference NPU built around a Tensor Contraction Processor. Official 2026 developer documentation states a 150 W TDP, while Furiosa's product specification page states 180 W; treat this discrepancy as unresolved for host cooling and power budgeting. INT4/INT8 peak figures and SR-IOV capability are vendor specifications, not independent inference throughput.
- Official source 1: https://developer.furiosa.ai/v2026.1.0-rc2/en/overview/rngd.html
- Official source 2: https://furiosa.ai/renegade-spec
- This scoped qualification does not establish full freshness, general stock, vendor-neutral benchmarks, framework support, ownership/legal clearance, schema/CI/cache/render or physical hardware testing.
