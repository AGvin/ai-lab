# AMD Ryzen AI Max+ PRO 495

AMD Ryzen AI Max+ PRO 495 is a released **Gorgon Halo** processor in the Ryzen AI Max PRO 400 series. It combines **16 Zen 5 CPU cores / 32 threads**, integrated **Radeon 8065S** graphics with **40 RDNA 3.5 compute units**, and an **XDNA 2 NPU** rated by AMD at up to **55 TOPS**. This processor is distinct from the non-PRO **Ryzen AI Max+ 395** (Strix Halo / Radeon 8060S) and from any complete workstation or Ryzen AI Halo Developer Platform.

## Shared-memory and local AI boundaries

The processor supports up to **192 GB LPDDR5x-8533 system memory** through a **256-bit interface**. This is a supported system-memory ceiling, **not dedicated GPU VRAM** or an assurance that an OEM device ships with 192 GB. Its graphics allocation uses dynamic and reserved/carved-out portions of shared memory. CPU/OS allocations, GPU buffers, model weights, KV cache, context size, batch size, quantization and inference implementation all limit realistic model fit. AMD claims of large-model capacity and peak compute are vendor demonstrations rather than independent throughput or fit benchmarks.

AMD specifies a **55 W default TDP** and **45–120 W configurable TDP** for the processor; these are not measurements of total system power or sustained inference performance. Memory implementation, chassis thermal capacity and OEM firmware can limit realized performance. The separately documented **Ryzen AI Halo 192 GB** computer is one product built around this processor and has its own storage, I/O, software, OS and support boundaries.

## Software support and operational checks

AMD lists Radeon 8065S as **RDNA 3.5 / `gfx1151`** and documents Ryzen AI Max+ PRO 495 support in ROCm 10.1.0. The usable GPU stack depends on the exact ROCm release, OS, kernel fixes and supported inference frameworks. AMD notes minimum Linux kernel patch levels for Ryzen AI Max devices; do not infer that every older Ubuntu image or third-party build works. NPU TOPS are not directly interchangeable with GPU LLM performance; PRO manageability features are configuration-dependent. No physical testing or independently matched LLM benchmarks were performed for this entry.

## Producer

- Produced by [Advanced Micro Devices, Inc.](../../../producers/sub/a/sub/advanced-micro-devices-inc/README.md).

## Official resources

- [AMD Ryzen AI Max+ PRO 495 processor specifications](https://www.amd.com/en/products/processors/laptop/ryzen-pro/ai-max-pro-400-series/amd-ryzen-ai-max-plus-pro-495.html)
- [AMD Ryzen AI Max PRO 400 series announcement](https://www.amd.com/en/blogs/2026/amd-powers-next-generation-agent-computers-with-new-ryzen-ai-hal.html)
- [AMD ROCm 10.1.0 hardware support](https://rocm.docs.amd.com/en/docs-10.1.0/about/release-notes.html)
- [AMD RDNA 3.5 APU kernel requirements](https://rocm.docs.amd.com/en/latest/reference/system-optimization/rdna3-5.html)
