# Documentation Requirements

## Requirements

- Identify `gpt-oss-20b` as OpenAI's concrete 21B-total / 3.6B-active open-weight reasoning model.
- Preserve the current 131,072-token context and maximum-output limits, June 1 2024 knowledge cutoff, configurable low/medium/high reasoning effort, Apache 2.0 distribution, fine-tuning support, and text-only modality only while first-party documentation supports them.
- Present local/low-latency/specialized-use positioning as OpenAI guidance rather than independent AI Lab ranking evidence.
- Keep runtime-specific quantization, kernel/backend support, serving throughput, tool implementations, and hardware fit freshness-sensitive and outside intrinsic model identity.

## Validation

- The model remains a concrete gpt-oss family member rather than a runtime/deployment preset.
- Active parameters are not used as a residency estimate.

## Source-scoped operating boundaries

- The model is not served in OpenAI’s API or ChatGPT, and OpenAI’s API fine-tuning service does not fine-tune these weights. The deployment operator supplies the runtime and tool-execution controls [Open-weight FAQ](https://help.openai.com/en/articles/11870455-openai-open-weight-models-gpt-oss).
- Active parameter count measures per-token computation, not the total weights that must be stored. It does not by itself establish VRAM, latency, or hardware fit.

## Source evidence

- [gpt-oss-20b model reference](https://developers.openai.com/api/docs/models/gpt-oss-20b).
- [Open-weight FAQ](https://help.openai.com/en/articles/11870455-openai-open-weight-models-gpt-oss).
