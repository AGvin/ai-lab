# Documentation Requirements

## Requirements

- Identify Raspberry Pi AI HAT+ as the Raspberry Pi 5 M.2 HAT-form-factor AI accelerator product offered in Hailo-8L 13-TOPS and Hailo-8 26-TOPS variants.
- Preserve the Hailo-8L/Hailo-8 variant boundary and do not generalize one variant's throughput or supported networks to the other.
- Describe its current practical role as Hailo-8/8L neural-network acceleration, especially supported computer-vision pipelines, rather than as the Raspberry Pi generative-LLM product.
- Keep it distinct from the earlier Raspberry Pi AI Kit and from AI HAT+ 2/Hailo-10H.
- Do not imply Hailo-10H GenAI APIs, dedicated 8 GB accelerator memory, Hailo-Ollama, or current compiled LLM/VLM artifacts are capabilities of AI HAT+.
- Treat Raspberry Pi OS, HailoRT/package compatibility, model-zoo support, performance, availability, and pricing as mutable current facts.
- Render the standard `entity-relations` block and preserve Raspberry Pi Ltd as producer.

## Validation

- Hailo-8L 13 TOPS and Hailo-8 26 TOPS variants are not conflated.
- AI HAT+ is not described as having the AI HAT+ 2 onboard-memory/GenAI capability class.
- Product identity remains separate from Hailo accelerator silicon, HailoRT, model artifacts, and Raspberry Pi 5 itself.

## Scoped original-source acceptance — 2026-11-05

- Official source: https://www.raspberrypi.com/documentation/accessories/ai-hat-plus.html
- Raspberry Pi AI HAT+ for Raspberry Pi 5 is offered with Hailo-8L 13 TOPS INT8 and Hailo-8 26 TOPS INT8 variants, for supported NPU vision and related workloads using the host Raspberry Pi system RAM. It does not supply the Hailo-10H local 8 GB onboard RAM or supported GenAI/LLM/VLM path of AI HAT+ 2. TOPS are variant-dependent theoretical operations and do not establish application throughput, compiler compatibility, general GGUF portability or current price.
- Preserve SKU and chip-versus-system boundaries. Current runtime, model artifacts, availability, ownership/rights, robotics safety and deployment are not cleared by this source qualification. No full freshness/schema/CI/cache/render or physical testing performed.
