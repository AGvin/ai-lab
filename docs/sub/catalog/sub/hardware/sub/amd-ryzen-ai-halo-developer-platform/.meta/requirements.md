# Documentation Requirements

## Requirements

- Identify AMD Ryzen AI Halo Developer Platform as AMD's branded complete local-AI developer system, distinct from the Ryzen AI Max processors it contains and from OEM systems built around the same processor family.
- Preserve two separately specified and released platform configurations: Ryzen AI Max+ 395 / 128 GB LPDDR5x / Radeon 8060S / up to 50 NPU TOPS versus Ryzen AI Max+ PRO 495 / 192 GB LPDDR5x / Radeon 8065S / up to 55 NPU TOPS. AMD's current Halo page and its original 2026 launch documentation identify both; a US retailer listed the 192 GB Linux configuration on 2026-11-01. Store-level availability, price and availability outside the US require independent current checks.
- Keep system-level storage, networking, ports, OS support, pre-installed Developer Center/software, firmware/update workflow, memory allocation controls, pricing, and support facts with the complete platform rather than copying them to the processor node.
- Treat availability, regional sales channels, software/firmware images, ROCm support, validated playbooks, pre-installed models/tools, OS versions, driver/runtime support, and product pricing as freshness-sensitive.
- Treat provider claims about maximum model parameter counts, cloud-cost savings, performance, and comparisons with DGX Spark as AMD-supplied configuration-specific evidence; usable model size depends on precision, runtime, context/KV cache, system reservation, and application overhead.
- Distinguish *unified system memory* from memory assigned to the integrated GPU: AMD's up-to-160 GB graphics allocation and its 200B/300B model-parameter figures are configuration-specific vendor claims, not validated model memory fit or independently benchmarked inference.
- Keep the already-canonical Ryzen AI Max+ 395 processor separate from the complete Halo system; the Max+ PRO 495 is an independently specified different processor and needs its own source-backed canonical intake before claiming a separate component node. The system may have both configurations without inventing a second Halo platform.

## Validation

- The node remains the complete AMD-branded developer platform rather than the processor family or a generic mini-PC category.
- System-level specifications are not transferred to arbitrary Ryzen AI Max+ 395 OEM systems.
- Do not mislabel the currently US-retail-listed 192 GB Ryzen AI Max+ PRO 495 Linux configuration as merely coming soon, or extrapolate US stock and configurations to other regions or OS variants.
- Producer provenance resolves to AMD.
