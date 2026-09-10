# Documentation Requirements

## Requirements

- Identify the exact huihui.ai repository as a concrete modified model derived from canonical Qwen3-Coder 30B-A3B Instruct.
- Preserve the `derived-from` relation to the canonical Qwen base model and `produced-by` relation to huihui.ai.
- Preserve text-generation role, Transformers/SafeTensors source form, Apache-2.0 license, and publisher-described abliteration/refusal-removal modification.
- Treat `uncensored` and `abliterated` as publisher labels/modification provenance rather than independent AI Lab quality or safety evidence.
- Avoid duplicating unchanged base-model architecture/parameter/context facts; link the canonical base model instead.
- Keep sampling/runtime setup, local memory fit, quantization quality, refusal-rate behavior, coding-agent suitability, and workload recommendations outside canonical model identity.
- Link reviewed artifacts without treating their conversion format as a separate trained model identity.

## Validation

- The derivative is represented as `model`, not `model-version` or `model-artifact`.
- Base-model technical facts are not silently changed by the derivative page without source evidence.
- Publisher behavior claims are not presented as independent benchmark evidence.
- GGUF conversions remain artifacts of this model.
