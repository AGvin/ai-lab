# Raspberry Pi AI HAT+

**PROVENANCE/OWNERSHIP REVIEW PENDING.** See the [provenance policy](../../../../../project/sub/policies/sub/russia-linked-ai/).

Raspberry Pi AI HAT+ is a Raspberry Pi 5 M.2 HAT-form-factor AI accelerator offered in Hailo-8L 13-TOPS and Hailo-8 26-TOPS variants.

## Hardware boundary

The Hailo-8L and Hailo-8 variants remain distinct and their throughput or supported networks must not be generalized across variants. AI HAT+ primarily adds Hailo-8 or Hailo-8L neural-network acceleration, especially supported computer-vision pipelines; it is distinct from the earlier Raspberry Pi AI Kit and from AI HAT+ 2/Hailo-10H. Hailo-10H GenAI APIs, dedicated 8 GB accelerator memory, Hailo-Ollama, and current compiled LLM or VLM artifacts are not AI HAT+ capabilities.

Raspberry Pi OS, HailoRT/package compatibility, model-zoo support, performance, availability, and pricing are mutable current facts.

## Relations

- Produced by [Raspberry Pi](../../../producers/sub/r/sub/raspberry-pi/).

## Official resources

- [Raspberry Pi AI HAT+](https://www.raspberrypi.com/products/ai-hat/)
- [Raspberry Pi AI HAT documentation](https://www.raspberrypi.com/documentation/accessories/ai-hat-plus.html)

## Scoped original-source acceptance — 2026-11-05

Raspberry Pi AI HAT+ for Raspberry Pi 5 is offered with Hailo-8L 13 TOPS INT8 and Hailo-8 26 TOPS INT8 variants, for supported NPU vision and related workloads using the host Raspberry Pi system RAM. It does not supply the Hailo-10H local 8 GB onboard RAM or supported GenAI/LLM/VLM path of AI HAT+ 2. TOPS are variant-dependent theoretical operations and do not establish application throughput, compiler compatibility, general GGUF portability or current price.

No physical tests, whole-catalog source freshness/schema/CI/cache/render, model execution or ownership/legal clearance were performed.
