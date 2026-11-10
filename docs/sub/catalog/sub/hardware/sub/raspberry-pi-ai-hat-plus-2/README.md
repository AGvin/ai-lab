# Raspberry Pi AI HAT+ 2

**PROVENANCE/OWNERSHIP REVIEW PENDING.** See the [provenance policy](../../../../../project/sub/policies/sub/russia-linked-ai/).

Raspberry Pi AI HAT+ 2 is a Raspberry Pi 5 accelerator product built around Hailo-10H with 40 TOPS INT4-class compute and 8 GB dedicated onboard LPDDR4X memory.

## Hardware boundary

The 8 GB Hailo-10H memory is accelerator-local and is not pooled with Raspberry Pi 5 system RAM. AI HAT+ 2 adds first-party-supported local GenAI capability beyond the Hailo-8 or Hailo-8L AI HAT+ class, but Raspberry Pi's approximate `up to ~6B parameters` statement is product guidance rather than a universal compatibility guarantee. Exact model compatibility depends on the numerical scheme, compiled Hailo artifact, context, runtime route, and compatible HailoRT/toolchain versions; arbitrary GGUF, Ollama, or Hugging Face checkpoint portability must not be assumed.

Runtime and firmware support, the model catalog, performance, availability, and pricing are mutable current facts.

## Relations

- Produced by [Raspberry Pi](../../../producers/sub/r/sub/raspberry-pi/).

## Official resources

- [Raspberry Pi AI HAT+ 2](https://www.raspberrypi.com/products/ai-hat-plus-2/)
- [Raspberry Pi AI HAT documentation](https://www.raspberrypi.com/documentation/accessories/ai-hat-plus.html)
- [Introducing Raspberry Pi AI HAT+ 2](https://www.raspberrypi.com/news/introducing-the-raspberry-pi-ai-hat-plus-2-generative-ai-on-raspberry-pi-5/)

## Scoped original-source acceptance — 2026-11-05

Raspberry Pi AI HAT+ 2 for Raspberry Pi 5 is a Hailo-10H NPU board with 40 TOPS INT4-class theoretical throughput and its own 8 GB accelerator-local RAM, which is not pooled with Raspberry Pi system memory. The product adds supported compiled local LLM and VLM options beyond the Hailo-8/8L AI HAT+ class; advertised ~6B parameter scope is approximate product guidance, not universal checkpoint or runtime compatibility. Validate supported Hailo artifact, quantization, HailoRT version and intended model before recommending deployment.

No hardware execution, repository-wide source freshness/schema/CI/cache/render, independent benchmark or ownership/legal clearance was performed.
