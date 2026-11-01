# Documentation Requirements

## Requirements

- Identify NVIDIA Jetson AGX Thor Developer Kit as the separately purchasable released development computer, distinct from the Jetson T5000 128 GB production module, Jetson T4000, Jetson AGX Orin Developer Kit, and automotive DRIVE AGX Thor Developer Kit.
- NVIDIA announced general availability on 25 August 2025. The kit includes a T5000 module with 128 GB memory mounted on the developer carrier board, plus an original integrated 1 TB M.2 NVMe and other developer connectivity; a bare production module does not inherit all of these contents.
- Source kit-specific carrier I/O from NVIDIA's developer-kit technical table, including 5GbE RJ45, QSFP28 connectivity, M.2 PCIe slots, USB and debug interfaces; do not misstate supported transceivers, bundled peripherals or full integration guarantees.
- Scope the published up-to-2070 FP4 TFLOPS and 40-130 W figures to the module and its specified precision/power configuration. Those maxima are not measured end-to-end inference latency, full-kit wall power, an all-model suitability guarantee or a cross-vendor performance comparison.
- Keep cooling, power adapter, ventilation, memory available to workloads, storage endurance, network deployment, firmware/driver/JetPack compatibility, and robotics safety validation as separate deployment constraints. Developer hardware and AI acceleration do not remove required physical actuator supervision/emergency-stop controls.
- NVIDIA's official FAQ distinguishes developer-kit development-use warranty from production module warranty and lists region/SKU-specific variants. Current pricing, regional availability, export restrictions, lifecycle and software support can change; do not hardcode a timeless selling price or transfer module lifecycle commitments to the kit.
- Attribute NVIDIA's comparison with Orin to the publisher and the original test boundary; no independent AI Lab hardware benchmarking or physical execution was performed.
- Preserve NVIDIA as the producer with one reciprocal canonical relation; include official developer-kit page, original release announcement, carrier/specification blog, current NVIDIA FAQ and current JetPack/Jetson Linux support reference.
- Product manufacturer/publication attribution does not independently establish complete beneficial ownership, all indirect holdings or sanctions status. Avoid unsupported nationality/control classifications.

## Validation

- One complete developer-kit hardware identity, no duplicate T5000 learned/compute module identity or automotive kit conflation.
- NVIDIA produced-by / produces relations resolve and direct index/producer links have canonical targets.
- Scoped content/link/relation checks do not constitute full-current-head JSON Schema, cache, CI, final rendering, measured throughput or two clean catalog-wide research passes.
