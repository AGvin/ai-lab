# Documentation Requirements

## Requirements

- Cover Raspberry Pi 5 with AI HAT+ 2/Hailo-10H-class acceleration and keep it distinct from Hailo-8/8L.
- Preserve the current official boundary: AI HAT+ 2 uses Hailo-10H with onboard memory and adds supported local LLM/VLM/GenAI routes; Raspberry Pi currently documents LLM/VLM support and an approximate supported scale boundary that must be rechecked with runtime/model updates.
- Identify exact HAT/firmware/runtime (`hailo-h10-all` or current successor), supported Hailo model artifact, host Pi/RAM, accelerator-local memory, context, and host/accelerator work split.
- Treat Raspberry Pi/Hailo example models and current supported exports as provider-documented compatibility; evaluate task quality and latency separately.
- Measure prompt/decode latency, context/cache limits, accelerator/host memory, sustained thermals/power, and end-to-end application latency.
- Do not assume every small Hugging Face model can be converted/run; unsupported architecture/operator/tokenizer/export remains Unknown.

## Validation

- LLM/VLM claims are tied to Hailo-10H/current software, not generic AI HAT branding.
- Current supported scale is treated as mutable provider documentation, not a universal parameter-count rule.
- Host and accelerator resource costs are both accounted for.
