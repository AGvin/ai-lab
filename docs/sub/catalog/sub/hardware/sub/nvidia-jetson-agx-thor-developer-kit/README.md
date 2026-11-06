# NVIDIA Jetson AGX Thor Developer Kit

**PROVENANCE/OWNERSHIP REVIEW PENDING.** See the [provenance policy](../../../../../project/sub/policies/sub/russia-linked-ai/).

The NVIDIA Jetson AGX Thor Developer Kit is a released Blackwell-based reference development computer for robotics, edge inference and physical-AI prototyping. [NVIDIA announced general availability on 25 August 2025](https://nvidianews.nvidia.com/news/nvidia-blackwell-powered-jetson-thor-now-available-accelerating-the-age-of-general-robotics). It is a complete developer-board configuration built around the 128 GB [Jetson T5000 production module](../nvidia-jetson-t5000/), not a second T5000 module or a production-system qualification.

## Included platform and boundaries

The [NVIDIA developer-kit technical specification](https://developer.nvidia.com/blog/introducing-nvidia-jetson-thor-the-ultimate-platform-for-physical-ai) lists the T5000 module, a developer carrier board and a populated 1 TB NVMe on M.2. Developer I/O includes 5GbE RJ45, QSFP28 networking, additional M.2 expansion, USB, debug and display connectors. The exact port configuration belongs to the kit; a bare T5000 module and a custom carrier do not supply those same ports or storage by default.

NVIDIA lists up to 2,070 FP4 TFLOPS and a configurable 40–130 W *module* power range. Such theoretical arithmetic performance is precision- and workload-dependent and does not state measured model throughput, entire-kit wall power, or guaranteed support for a particular model. Keep the Jetson AGX Thor Developer Kit distinct from automotive DRIVE AGX Thor developer hardware.

## Use, support and safety

Confirm current [JetPack/Jetson Linux support](https://developer.nvidia.com/embedded/jetpack/downloads) for the exact kit, runtime, drivers, sensors and container images. Plan power, cooling, ventilation, storage and networking for actual sustained loads, not peak AI marketing figures. Robot/actuator deployments still need appropriate human supervision, physical safety boundaries and emergency-stop controls; no AI Lab hardware execution or safety certification was performed.

NVIDIA's [official FAQ](https://developer.nvidia.com/embedded/faq) identifies region-dependent SKUs and a developer-kit warranty intended for development use. It must not be confused with the standalone production module's lifecycle or warranty. Prices, export/regional availability and supported software combinations are mutable and should be verified for a real purchase.

## Provenance

- Produced by: [NVIDIA](../../../producers/sub/n/sub/nvidia/).

## Official resources

- [Jetson developer kits](https://developer.nvidia.com/embedded/jetson-developer-kits)
- [2025 general-availability announcement](https://nvidianews.nvidia.com/news/nvidia-blackwell-powered-jetson-thor-now-available-accelerating-the-age-of-general-robotics)
- [Module and developer-kit specifications](https://developer.nvidia.com/blog/introducing-nvidia-jetson-thor-the-ultimate-platform-for-physical-ai)
- [Developer-kit FAQ and regional SKUs](https://developer.nvidia.com/embedded/faq)
- [JetPack SDK compatibility and release downloads](https://developer.nvidia.com/embedded/jetpack/downloads)

## Scoped original-source acceptance — 2026-11-05

This is a complete Blackwell-based Jetson AGX Thor Developer Kit containing a T5000 128 GB module on a development carrier, distinct from a standalone T5000 production module and T4000. NVIDIA quotes up to 2070 FP4 TFLOPS and a 130 W envelope for specified module compute and power conditions, not measured application inference or complete-system wall power. Robotics use requires independent safety controls, qualified power and cooling, JetPack validation and workload-specific testing. Vendor launch and kit descriptions are not adoption or ownership clearance.

No physical tests, whole-catalog source freshness/schema/CI/cache/render, model execution or ownership/legal clearance were performed.
