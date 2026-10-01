# Documentation Requirements

## Requirements

- Identify Raspberry Pi AI HAT+ 2 as the Raspberry Pi 5 accelerator product built around Hailo-10H with 40 TOPS INT4-class compute and 8 GB dedicated onboard LPDDR4X memory.
- Preserve the dedicated-memory boundary: the Hailo-10H 8 GB is accelerator-local memory and is not pooled with Raspberry Pi 5 system RAM.
- Describe the product as adding current first-party supported local GenAI capability, including named LLM, VLM, speech, and vision artifacts, beyond the Hailo-8/8L AI HAT+ capability class.
- Preserve Raspberry Pi's approximate `up to ~6B parameters` statement only as product-level guidance; it is not a generic compatibility guarantee for every architecture below that size.
- Keep exact model compatibility, quantization/numerical scheme, compiled HEF artifact, context, HailoRT/Hailo-Ollama route, TTFT/TPS, and practical recommendation with the Raspberry Pi Hailo-10H model-selection owner rather than treating them as immutable hardware properties.
- Do not imply arbitrary GGUF/Ollama/Hugging Face checkpoint portability. Current Hailo-10H deployment depends on supported/compiled Hailo artifacts and compatible runtime/toolchain versions.
- Treat package/runtime/firmware support, model catalog, performance, availability, and pricing as mutable current facts.
- Render the standard `entity-relations` block and preserve Raspberry Pi Ltd as producer.

## Validation

- AI HAT+ 2 is not conflated with AI HAT+, Hailo-8/8L, or Raspberry Pi host RAM.
- `40 TOPS INT4` is not converted into a universal model-speed or compatibility claim.
- `~6B` is not converted into a generic parameter-count fit table.
- Practical model recommendations require exact current Hailo artifact/numerical-scheme/runtime evidence.
