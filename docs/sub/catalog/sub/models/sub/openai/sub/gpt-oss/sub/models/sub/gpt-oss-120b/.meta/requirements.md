# Documentation Requirements

## Requirements

- Identify `gpt-oss-120b` as OpenAI's concrete 117B-total / 5.1B-active open-weight reasoning model.
- Preserve the current 131,072-token context and maximum-output limits, June 1 2024 knowledge cutoff, configurable low/medium/high reasoning effort, Apache 2.0 distribution, fine-tuning support, and text-only modality only while first-party documentation supports them.
- Treat provider/runtime statements such as fitting on one H100 as source-scoped deployment guidance rather than universal memory-fit evidence.
- Keep runtime-specific quantization, kernel/backend support, serving throughput, tool implementations, and hardware fit freshness-sensitive and outside intrinsic model identity.

## Validation

- The model remains a concrete gpt-oss family member rather than a hardware profile or hosted endpoint.
- Active parameters are not used as a residency estimate.
