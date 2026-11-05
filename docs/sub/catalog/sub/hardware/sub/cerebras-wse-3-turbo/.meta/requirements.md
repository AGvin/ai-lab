# Documentation Requirements

## Requirements

- Identify Cerebras WSE-3 Turbo (WSE-3T) as the current wafer-scale AI processor product in the WSE-3 generation.
- Keep the processor identity distinct from Cerebras CS-3/CS-4 systems, complete rack-scale platforms, and Cerebras hosted inference services.
- Preserve wafer-scale processor facts such as transistor count, core count, on-chip memory, and compute only at the exact product/version scope supported by current first-party sources.
- Treat shipping state, system integration, benchmark performance, pricing, software support, and deployment availability as freshness-sensitive.
- Render the standard `entity-relations` block from validated current-entity relations.

## Validation

- The hardware entity remains the processor product rather than a complete Cerebras system or service.
- Producer provenance resolves to Cerebras Systems Inc.

## Scoped original-source acceptance — 2026-11-05

- Cerebras WSE-3 Turbo is a single wafer-scale AI processor, distinct from the CS-4 rack system composed of three such wafers. Manufacturer specifications state four trillion transistors, 900,000 AI cores, 44 GB on-wafer SRAM, 250 PFLOPS peak compute and 43.2 PB/s on-chip memory bandwidth per wafer. Do not assign rack aggregate numbers or vendor inference comparisons to one processor. Availability, integration, runtime and independently measured application performance remain unverified.
- Source boundary: https://www.cerebras.ai/chip ; https://www.cerebras.ai/press-release/cerebras-unveils-cs-4-up-to-30-times-faster-than-gpu-based-solutions-3347356.
- Original manufacturer verification does not certify current shipping, performance, licensing, producer control, runtime, full schema/CI/cache or final rendering.
