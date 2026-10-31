# Documentation Requirements

## Requirements

- Identify `perplexity-ai/pplx-decider-flash-v1.2` as a separate released small PPLX Decider model, not as a quantization of the 27B V1.2 checkpoint.
- Preserve its source-backed Qwen3.5-4B base, distillation from the larger decision models, text/image input, joint request protocol, calibration and Apache-2.0 boundary.
- Keep the GGUF repository as a packaging/quantization artifact of this model rather than a second trained-model identity.
- Keep checkpoint-specific accuracy, grouping recommendations, memory, compilation and provider access contextual rather than family-wide guarantees.

## Validation

- Flash V1.2 remains distinct from V1.2, V1.1 and the GGUF packaging repository.
- Do not invent a canonical `derived-from` edge until the exact Qwen3.5-4B base identity exists in the catalog.
