# Documentation Requirements

## Requirements

- Identify AMD Ryzen AI Halo Developer Platform as AMD's branded complete local-AI developer system, distinct from the Ryzen AI Max processors it contains and from OEM systems built around the same processor family.
- Distinguish the current AMD-listed Ryzen AI Max+ 395 / 128 GB LPDDR5x / Radeon 8060S / up to 50 NPU TOPS configuration from the Ryzen AI Max+ PRO 495 / 192 GB LPDDR5x / Radeon 8065S / up to 55 NPU TOPS variant. AMD's current Halo product page labels the 192 GB variant **Coming Soon**; a previously recorded 2026-11-01 US retailer listing is conflicting evidence, not proof of shipment or current stock. Do not claim both systems are currently shipping without a separate date-stamped availability check.
- Keep system-level storage, networking, ports, OS support, pre-installed Developer Center/software, firmware/update workflow, memory allocation controls, pricing, and support facts with the complete platform rather than copying them to the processor node.
- Treat availability, regional sales channels, software/firmware images, ROCm support, validated playbooks, pre-installed models/tools, OS versions, driver/runtime support, and product pricing as freshness-sensitive.
- Treat provider claims about maximum model parameter counts, cloud-cost savings, performance, and comparisons with DGX Spark as AMD-supplied configuration-specific evidence; usable model size depends on precision, runtime, context/KV cache, system reservation, and application overhead.
- Distinguish *unified system memory* from memory assigned to the integrated GPU: AMD's up-to-160 GB graphics allocation and its 200B/300B model-parameter figures are configuration-specific vendor claims, not validated model memory fit or independently benchmarked inference.
- Keep the already-canonical Ryzen AI Max+ 395 processor separate from the complete Halo system; the Max+ PRO 495 is an independently specified different processor and needs its own source-backed canonical intake before claiming a separate component node. The Max+ PRO 495 now has a separate canonical processor node; it is not a second Halo platform.

## Validation

- The node remains the complete AMD-branded developer platform rather than the processor family or a generic mini-PC category.
- System-level specifications are not transferred to arbitrary Ryzen AI Max+ 395 OEM systems.
- Preserve the manufacturer 'Coming Soon' label for the 192 GB system and the conflicting historical third-party listing as separate evidence; do not assert current availability, stock or supported regions without reconciling both.
- Producer provenance resolves to AMD.

## Scoped original-source acceptance — 2026-11-05

- Manufacturer source: https://www.amd.com/en/products/processors/desktops/ryzen/ryzen-ai-halo.html
- Complete developer system with separately specified 128 GB Max+ 395 and 192 GB Max+ PRO 495 shared-memory configurations, not a standalone processor.
- Preserve producer attribution separately from ultimate-control rights. No complete freshness, host/runtime benchmark, ownership/legal clearance, schema/CI/cache or renderer audit was performed.
